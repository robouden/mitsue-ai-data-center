<!-- Version: v1.0 | Last modified: 2026-08-10 -->

# Biomass CHP — Steam (Rankine) vs. Gasification+Engine

Comparison of the two conversion pathways for turning wood into electricity, and why
gasification+engine is the better fit for Mitsue's ≤1 MWe scale.

## Table

| Pathway | Steps | Typical el. efficiency | Complexity/CAPEX | Scale fit |
|---|---|---|---|---|
| Wood→heat→steam→turbine→power (Rankine) | Combustion boiler → steam → steam turbine/ORC → generator | 10–20% (small ORC ~15%; large steam ~25–30%) | High (boiler, steam system, safety) | Best >1 MWe; poor <500 kWe |
| Wood→gasification→syngas→engine→power | Gasifier → gas cleanup → ICE (or CHP genset) → generator | 20–30% | Lower CAPEX at small scale, but gas cleaning is finicky | Good fit 50 kWe–1 MWe (matches Mitsue's scale) |

## Notes

- Gasification+engine gives higher electrical efficiency at small scale — steam-Rankine
  only gets efficient once you're at industrial (>MW) size.
- Steam path yields high-grade steam/heat as a byproduct (good if process heat is needed);
  gasification yields lower-grade waste heat (engine jacket/exhaust, ~60–80°C) — fine for
  onsen but not process steam.
- Gasification engines are more sensitive to fuel moisture/particle size (need dry, sized
  chips); steam boilers tolerate wetter/rougher fuel.
- Domestic gasifier+engine makers (中外炉, ネオナイト) fit the Japanese-manufacturer policy
  better than steam-turbine packages at this scale.
- **Conclusion for Mitsue's ≤1 MWe scale: gasification→engine is the stronger fit** —
  consistent with the Tier A/B maker lists in `mitsue_chp_maker_shortlist.md`, which are all
  gasification (or Stirling at prototype scale), not steam-Rankine.

## Related docs
- `mitsue_chp_maker_shortlist.md` — CHP maker shortlist (Tier A prototype / Tier B commercial)
- 日本語版: `mitsue_chp_steam_vs_gasification_ja.md`
