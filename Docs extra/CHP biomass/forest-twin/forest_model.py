#!/usr/bin/env python3
"""Mitsue Forest Twin -- simple 50-year simulator (stdlib only).

Three loops, as discussed:
  1. Forest  : grow sugi, convert X% of area/year to broadleaf, see wood out.
  2. Carbon  : standing C, C locked in timber products, C avoided vs fossil fuel.
  3. Money   : revenue (logs, power, heat, credits) vs costs.

Run:  python3 forest_model.py
Out :  prints a yearly table + summary, writes results.csv

All assumptions live in CONFIG below with source notes. Numbers are
order-of-magnitude defaults for a Mitsue-scale sugi plantation -- tune them,
don't trust them blindly.
"""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# CONFIG  (edit these)
# ---------------------------------------------------------------------------
CONFIG = {
    "sim_years": 50,

    # Harvest regime:
    #   "convert"  = clearfell X%/yr of area, replant broadleaf (one-way, FINITE fuel)
    #   "rotation" = sustained yield: harvest area/rotation_age per yr, replant sugi
    #                so stands re-enter the cycle -> perpetual fuel (Mishima-style)
    #   "mixed"    = split: convert_fraction goes to broadleaf, rest sustained sugi
    "regime": "rotation",
    "harvest_pct_per_year": 0.02,   # used by "convert"/"mixed" for the broadleaf conversion
    "rotation_age": 45,             # sugi harvest age for sustained yield (yr)
    "convert_fraction": 0.30,       # "mixed": share of forest permanently -> broadleaf
    "replant_species": "konara_broadleaf",

    # Wood product split of harvested volume (must sum to 1.0)
    "alloc_sawlog": 0.40,   # construction timber -> stored 80 yr
    "alloc_chp":    0.40,   # gasifier fuel       -> burned now (biogenic)
    "alloc_biochar":0.10,   # -> stored ~500 yr
    "alloc_loss":   0.10,   # bark/needles/decay

    "product_life_sawlog_yr": 80,
    "product_life_biochar_yr": 500,

    # CHP / gasifier  (NEDO biomass gasification, typical small-scale CHP)
    "fuel_moisture": 0.30,          # green chips, fraction water
    "elec_efficiency": 0.13,        # fuel energy -> NET electricity (calibrated to
                                    # Mishima Fukushima: ~750 green t/yr -> ~50 kWe @ 70% CF.
                                    # small gasifier-genset net elec eff is ~12-15%, not 22%)
    "heat_efficiency": 0.45,        # fuel energy -> usable heat
    "biochar_yield_t_per_t": 0.20,  # dry tonnes biochar per dry tonne feed (if pyrolysis)

    # Avoided fossil emissions
    "grid_co2_kg_per_kwh": 0.45,    # Japan grid average
    "heat_fossil_kg_per_gj": 60.0,  # displacing LPG/oil boilers

    # Carbon
    "co2_per_c": 44.0 / 12.0,       # CO2 mass / carbon mass

    # Economics (JPY)
    "elec_price_yen_kwh": 35.0,     # FIT-ish / avoided retail
    "heat_price_yen_gj": 2000.0,    # vs LPG
    "biochar_price_yen_t": 40000.0,
    "carbon_credit_yen_t_co2": 3000.0,  # J-Credit-ish

    # --- harvest supply-chain costs (素材生産費, JFA cost surveys) ---
    "felling_yarding_yen_m3": 4500.0,   # cut + drag to roadside (labour+machine)
    "transport_yen_m3_km": 150.0,       # truck haul, per m3 per km
    "transport_distance_km": 5.0,       # forest -> CHP/mill (Mitsue max ~5 km)
    "chipping_yen_m3": 2000.0,          # only on wood that is chipped (CHP+biochar)
    "drying_yen_m3": 1000.0,            # drying CHP fuel to usable moisture
    "road_maint_yen_year": 800000.0,    # forest road upkeep / yr

    "planting_cost_yen_ha": 700000.0,

    # --- CHP sizing (capex/O&M derived from fuel flow, not guessed) ---
    "chp_size_auto": True,               # size the unit to the wood supply
    "chp_capacity_factor": 0.80,         # fraction of year run at rated load
    "chp_install_yen_per_kwe": 700000.0, # installed cost of gasifier-genset / kWe
    "chp_om_yen_per_kwe_year": 60000.0,  # O&M / kWe / yr
    # Manual fallback (used only when chp_size_auto is False):
    "chp_om_yen_year": 3000000.0,
    "chp_capex_yen": 30000000.0,
}

# ---------------------------------------------------------------------------
def load_species(path):
    sp = {}
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            for k, v in r.items():
                if k != "species":
                    r[k] = float(v)
            sp[r["species"]] = r
    return sp


def load_stands(path):
    stands = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            stands.append({"id": r["stand_id"], "species": r["species"],
                           "area": float(r["area_ha"]), "age": float(r["age"])})
    return stands


def volume_per_ha(sp, age):
    """Logistic standing-volume growth curve (m3/ha)."""
    return sp["vmax_m3_ha"] / (1.0 + math.exp(-sp["growth_r"] * (age - sp["growth_t0"])))


def standing_carbon_t(sp, area, age):
    """Above + below ground carbon (tonnes C) for a stand."""
    vol = volume_per_ha(sp, age) * area                 # m3
    agb_t = vol * sp["wood_density_kg_m3"] / 1000.0     # oven-dry biomass tonnes
    total_bio = agb_t * (1.0 + sp["root_shoot_ratio"])
    return total_bio * sp["carbon_fraction"]


def eco_indices(stands):
    """APPROXIMATE biodiversity & water-retention indices (0-1). Directional
    proxies, NOT measured: broadleaf and mixed-age forest score higher than dense
    sugi monoculture (well-established in the literature; calibrate later).
      - biodiversity: driven by broadleaf area share + age-class diversity
      - water:        infiltration / low landslide risk, driven by broadleaf share
    """
    live = [s for s in stands if s["area"] > 0]
    total = sum(s["area"] for s in live) or 1.0
    bl_frac = sum(s["area"] for s in live if s["species"] != "sugi") / total
    # age-class diversity: spread of stand ages, normalised 0-1
    ages = [s["age"] for s in live]
    age_div = 0.0
    if len(ages) > 1:
        mean = sum(ages) / len(ages)
        sd = (sum((a - mean) ** 2 for a in ages) / len(ages)) ** 0.5
        age_div = min(1.0, sd / 25.0)
    biodiversity = min(1.0, 0.25 + 0.55 * bl_frac + 0.20 * age_div)
    water = min(1.0, 0.30 + 0.70 * bl_frac)
    return biodiversity, water


# ---------------------------------------------------------------------------
def simulate(species, stands, cfg):
    total_area = sum(s["area"] for s in stands)
    regime = cfg["regime"]
    if regime == "convert":
        annual_harvest_ha = total_area * cfg["harvest_pct_per_year"]
    else:  # rotation / mixed -> sustained-yield area per year
        annual_harvest_ha = total_area / cfg["rotation_age"]
    product_pools = []   # list of dicts: {created, carbon_t, life}
    rows = []

    for year in range(1, cfg["sim_years"] + 1):
        # --- grow ---
        for s in stands:
            s["age"] += 1

        # --- harvest oldest sugi up to target area ---
        remaining = annual_harvest_ha
        harvest_vol = 0.0
        replant_area = 0.0
        for s in sorted(stands, key=lambda x: -x["age"]):
            if remaining <= 0:
                break
            if s["species"] != "sugi" or s["area"] <= 0:
                continue
            take = min(s["area"], remaining)
            harvest_vol += volume_per_ha(species[s["species"]], s["age"]) * take
            s["area"] -= take
            replant_area += take
            remaining -= take
        # --- replant: species depends on regime (sustained sugi re-enters cycle) ---
        if replant_area > 0:
            if regime == "convert":
                bl_area, sugi_area = replant_area, 0.0
            elif regime == "rotation":
                bl_area, sugi_area = 0.0, replant_area
            else:  # mixed
                bl_area = replant_area * cfg["convert_fraction"]
                sugi_area = replant_area - bl_area
            if bl_area > 0:
                stands.append({"id": f"B{year}", "species": cfg["replant_species"],
                               "area": bl_area, "age": 0.0})
            if sugi_area > 0:
                stands.append({"id": f"R{year}", "species": "sugi",
                               "area": sugi_area, "age": 0.0})

        # --- wood product allocation ---
        sp_h = species["sugi"]
        c_per_m3 = sp_h["wood_density_kg_m3"] / 1000.0 * sp_h["carbon_fraction"]  # tC/m3
        sawlog_vol = harvest_vol * cfg["alloc_sawlog"]
        chp_vol    = harvest_vol * cfg["alloc_chp"]
        biochar_vol= harvest_vol * cfg["alloc_biochar"]

        if sawlog_vol > 0:
            product_pools.append({"created": year, "carbon_t": sawlog_vol * c_per_m3,
                                  "life": cfg["product_life_sawlog_yr"]})

        # --- CHP energy from chp_vol ---
        dry_t = chp_vol * sp_h["wood_density_kg_m3"] / 1000.0
        fuel_energy_gj = dry_t * sp_h["heat_value_gj_t_dry"] * (1 - cfg["fuel_moisture"] * 0.3)
        elec_gj = fuel_energy_gj * cfg["elec_efficiency"]
        elec_kwh = elec_gj * 277.778
        heat_gj = fuel_energy_gj * cfg["heat_efficiency"]

        # --- biochar (stored carbon) ---
        biochar_dry_t = biochar_vol * sp_h["wood_density_kg_m3"] / 1000.0 * cfg["biochar_yield_t_per_t"]
        biochar_c = biochar_dry_t * 0.80   # biochar ~80% carbon
        if biochar_c > 0:
            product_pools.append({"created": year, "carbon_t": biochar_c,
                                  "life": cfg["product_life_biochar_yr"]})

        # --- carbon pools this year ---
        standing_c = sum(standing_carbon_t(species[s["species"]], s["area"], s["age"])
                         for s in stands if s["area"] > 0)
        product_c = sum(p["carbon_t"] for p in product_pools
                        if year - p["created"] < p["life"])
        avoided_co2_t = (elec_kwh * cfg["grid_co2_kg_per_kwh"]
                         + heat_gj * cfg["heat_fossil_kg_per_gj"]) / 1000.0
        biodiversity, water = eco_indices(stands)

        # --- economics ---
        revenue = (sawlog_vol * sp_h["log_price_yen_m3"]
                   + elec_kwh * cfg["elec_price_yen_kwh"]
                   + heat_gj * cfg["heat_price_yen_gj"]
                   + biochar_dry_t * cfg["biochar_price_yen_t"]
                   + avoided_co2_t * cfg["carbon_credit_yen_t_co2"])
        chipped_vol = chp_vol + biochar_vol
        # costs excluding CHP capex/O&M (added in a 2nd pass once the unit is sized)
        costs_excl_chp = (
            harvest_vol * cfg["felling_yarding_yen_m3"]
            + harvest_vol * cfg["transport_yen_m3_km"] * cfg["transport_distance_km"]
            + chipped_vol * cfg["chipping_yen_m3"]
            + chp_vol * cfg["drying_yen_m3"]
            + replant_area * cfg["planting_cost_yen_ha"]
            + (cfg["road_maint_yen_year"] if harvest_vol > 0 else 0.0)
        )

        rows.append({
            "year": year,
            "harvest_m3": harvest_vol,
            "standing_C_t": standing_c,
            "product_C_t": product_c,
            "avoided_CO2_t": avoided_co2_t,
            "elec_kwh": elec_kwh,
            "elec_MWh": elec_kwh / 1000.0,
            "heat_GJ": heat_gj,
            "biodiversity": biodiversity,
            "water_index": water,
            "revenue_M_yen": revenue / 1e6,
            "_costs_excl_chp": costs_excl_chp,
        })

    # --- 2nd pass: size the CHP to peak fuel flow, set capex + O&M ---
    peak_kwh = max((r["elec_kwh"] for r in rows), default=0.0)
    chp_built = peak_kwh > 0 and cfg["alloc_chp"] > 0
    nameplate_kwe = peak_kwh / (cfg["chp_capacity_factor"] * 8760.0) if chp_built else 0.0
    if cfg["chp_size_auto"]:
        capex = nameplate_kwe * cfg["chp_install_yen_per_kwe"]
        om_year = nameplate_kwe * cfg["chp_om_yen_per_kwe_year"]
    else:
        capex = cfg["chp_capex_yen"] if chp_built else 0.0
        om_year = cfg["chp_om_yen_year"] if chp_built else 0.0
    capex_annual = capex / cfg["sim_years"]

    for r in rows:
        costs = r.pop("_costs_excl_chp")
        del r["elec_kwh"]
        if chp_built:
            costs += om_year + capex_annual
        r["cost_M_yen"] = costs / 1e6
        r["profit_M_yen"] = r["revenue_M_yen"] - costs / 1e6
    meta = {"nameplate_kwe": nameplate_kwe, "capex_yen": capex, "om_year_yen": om_year}
    return rows, meta


# ---------------------------------------------------------------------------
# Scenarios for --compare : name -> CONFIG overrides
SCENARIOS = {
    "A: rotation (sustained sugi)":   {"regime": "rotation"},
    "B: convert (1-way broadleaf)":   {"regime": "convert", "harvest_pct_per_year": 0.02},
    "C: mixed (30% broadleaf)":       {"regime": "mixed", "convert_fraction": 0.30},
    "D: leave forest (no harvest)":   {"regime": "convert", "harvest_pct_per_year": 0.0},
}


def run_scenario(overrides):
    cfg = dict(CONFIG)
    cfg.update(overrides)
    species = load_species(os.path.join(HERE, "data", "species.csv"))
    stands = load_stands(os.path.join(HERE, "data", "stands.csv"))
    rows, meta = simulate(species, stands, cfg)
    return {
        "avoided_CO2_t": sum(r["avoided_CO2_t"] for r in rows),
        "product_C_t": rows[-1]["product_C_t"],
        "standing_C_t": rows[-1]["standing_C_t"],
        "elec_MWh": sum(r["elec_MWh"] for r in rows),
        "profit_M_yen": sum(r["profit_M_yen"] for r in rows),
        "nameplate_kwe": meta["nameplate_kwe"],
        "capex_M_yen": meta["capex_yen"] / 1e6,
        "biodiversity": rows[-1]["biodiversity"],
        "water_index": rows[-1]["water_index"],
    }


def compare():
    print(f"\nScenario comparison -- {CONFIG['sim_years']} year totals (CHP auto-sized)\n")
    print(f"  {'scenario':<28} {'kWe':>5} {'avoidCO2':>9}"
          f" {'prodC':>7} {'profit M¥':>10} {'biodiv':>7} {'water':>6}")
    for name, ov in SCENARIOS.items():
        s = run_scenario(ov)
        print(f"  {name:<28} {s['nameplate_kwe']:>5.0f}"
              f" {s['avoided_CO2_t']:>9,.0f} {s['product_C_t']:>7,.0f}"
              f" {s['profit_M_yen']:>10,.1f} {s['biodiversity']:>7.2f} {s['water_index']:>6.2f}")
    print("\n  profit=cumulative 50-yr  biodiv/water=approx index 0-1 (end state)\n")


def sweep():
    """Grid-search harvest rate x capacity factor; profit (M¥), CHP auto-sized."""
    harvest_grid = [0.01, 0.02, 0.03, 0.04, 0.06, 0.08]
    cf_grid = [0.50, 0.65, 0.80, 0.90]
    print(f"\nProfit sweep -- cumulative {CONFIG['sim_years']}-yr profit (M¥), CHP auto-sized")
    print("  rows = harvest %/yr,  cols = CHP capacity factor\n")
    print("         " + "".join(f"{c:>10.0%}" for c in cf_grid))
    best = None
    for h in harvest_grid:
        cells = []
        for cf in cf_grid:
            s = run_scenario({"harvest_pct_per_year": h, "chp_capacity_factor": cf})
            p = s["profit_M_yen"]
            cells.append(p)
            if best is None or p > best[0]:
                best = (p, h, cf)
        print(f"  {h:>5.0%}  " + "".join(f"{p:>10,.0f} " for p in cells))
    print(f"\n  best: {best[0]:,.0f} M¥  at harvest {best[1]:.0%}/yr, capacity factor {best[2]:.0%}\n")


# ---------------------------------------------------------------------------
def main():
    species = load_species(os.path.join(HERE, "data", "species.csv"))
    stands = load_stands(os.path.join(HERE, "data", "stands.csv"))
    rows, meta = simulate(species, stands, CONFIG)

    print(f"\nMitsue Forest Twin -- {CONFIG['sim_years']} year simulation")
    print("  (convert {:.0%} of area/yr, sugi -> broadleaf)\n".format(CONFIG["harvest_pct_per_year"]))
    print("  yr  harvest   standC  prodC  avoidCO2  elecMWh  profit(M¥)")
    for r in rows:
        if r["year"] % 5 == 0 or r["year"] == 1:
            print("  {year:>3} {harvest_m3:>8.0f} {standing_C_t:>8.0f} {product_C_t:>6.0f}"
                  " {avoided_CO2_t:>8.0f} {elec_MWh:>8.1f} {profit_M_yen:>10.1f}".format(**r))

    cum_avoided = sum(r["avoided_CO2_t"] for r in rows)
    cum_profit = sum(r["profit_M_yen"] for r in rows)
    cum_product = rows[-1]["product_C_t"]
    avg_kwe = sum(r["elec_MWh"] for r in rows) * 1000 / len(rows) / 8760
    print("\nCHP (auto-sized to fuel flow):")
    print(f"  Nameplate              : {meta['nameplate_kwe']:>10,.0f} kWe  (avg load ~{avg_kwe:,.0f} kWe)")
    print(f"  Derived capex          : {meta['capex_yen']/1e6:>10,.1f} M¥")
    print(f"  Derived O&M            : {meta['om_year_yen']/1e6:>10,.2f} M¥/yr")
    print("\nAfter {} years:".format(CONFIG["sim_years"]))
    print(f"  CO2 avoided (fossil)   : {cum_avoided:>10,.0f} tCO2")
    print(f"  Carbon in timber/char  : {cum_product:>10,.0f} tC  ({cum_product*CONFIG['co2_per_c']:,.0f} tCO2e)")
    print(f"  Standing forest carbon : {rows[-1]['standing_C_t']:>10,.0f} tC")
    print(f"  Cumulative profit      : {cum_profit:>10,.1f} M¥")
    print(f"  Biodiversity index*    : {rows[0]['biodiversity']:>10.2f} -> {rows[-1]['biodiversity']:.2f}")
    print(f"  Water-retention index* : {rows[0]['water_index']:>10.2f} -> {rows[-1]['water_index']:.2f}")
    print("  (* approximate 0-1 proxy: broadleaf share + age diversity, not measured)")

    out = os.path.join(HERE, "results.csv")
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nFull yearly results -> {out}\n")


if __name__ == "__main__":
    import sys
    if "--compare" in sys.argv:
        compare()
    elif "--sweep" in sys.argv:
        sweep()
    else:
        main()
