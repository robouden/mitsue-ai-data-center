<p align="right">Version: v1.5 | Last modified: 2026-10-15</p>

# Kiri (Paulownia) vs Sugi vs Hinoki — Green Moisture and Drying

Purpose: first-pass comparison for the SANSEI kiri discussion (2026-10-22) and fuel-chain planning. **Literature check only; no Mitsue measurements. No Japanese-kiri green-wood figure was found.**

MC convention: **wet basis** (water ÷ total mass) unless marked "dry basis". Conversion: wet % = d ÷ (1 + d), where d = dry-basis MC as a fraction.

## 1. Comparison table

| | Kiri (Paulownia) | Sugi (スギ) | Hinoki (ヒノキ) |
|---|---|---|---|
| Green MC, stem (wet basis) | **~55–62%** (≈120–165% dry basis) | **~53–68%** (≈115–209% dry basis; very variable) | Not found in sources; reported **lower than sugi** (heartwood and sapwood) |
| Heartwood vs sapwood | Not separated in sources found | Sapwood ≈209%, heartwood ≈115% dry basis in large logs (mean total ≈162% = ~62% wet). Black heartwood (黒心) holds ≈2× the water of red heartwood | Sapwood MC peaks ~4–6 m up the stem |
| Variability | Young trees: branches ~100%, leaves >300% dry basis, so fuel from tops is much wetter than stem | High; CV 0.41 in heartwood; uneven drying | Lower than sugi (qualitative) |
| Wood density (dry) | Very low (light wood) | ~314 kg/m³ chips basis (project figure); ~0.9–1.1 g/cm³ green sapwood | Higher than sugi |
| Dry basic density | **~335 kg/m³** (3 hybrids, Croatia); air-dry reports 231–273 kg/m³ for other clones. Wide range | **~314 kg/m³** (project figure, Forest Twin) | Not found in sources; higher than sugi (general knowledge, unverified) |
| Heating value, dry (HHV) | **17.2–19.7 MJ/kg** (wood 19.3 Croatia; 18.6 / 17.2 Polish-Spanish hybrid; 16.7–17.8 other studies) | **~22.1 MJ/kg** (Kanagawa, 5,274 kcal/kg; basis not stated, my conversion, **probably not comparable**) | ~22.4 MJ/kg (heartwood 5,346 kcal/kg, same Kanagawa survey, same caveat) |
| Net energy per fresh tonne | Lower at ~60% MC: water takes ~2.45 GJ/t of water to evaporate | Similar at ~50–60% MC | Similar or slightly better (lower MC) |
| Fuel per m³ of stem | Roughly equal to sugi if density ~335; **less** if density ~230–270 | Baseline (314 kg/m³) | More than sugi |
| Fuel per ha | Depends on yield: ~560 kg dry-ish biomass/tree at 7.5 yr (Fukushima, basis unclear); no per-ha stand data found | Slow growth, but long established stand volumes | Slowest growing of the three |
| Drying speed (lumber/log) | Fast: green → 20% in **39 days** air-dried lumber (Kentucky, ≈3.5 MC points/day) | Slow: log + 葉枯らし (leaf-drying) + yard stacking reached **45% in ~4 months** (Tottori, chip logs); ~1.2 MC points/day (Gifu 1981), fastest in the first month | Debarking and stacking with stickers speeds log drying (Nagasaki); no day count found |
| Natural-drying floor | Equilibrium ~15% in Japan | 15–17% is the practical limit for air-dried lumber (Nara); needs kiln for ≤15% | Same |
| Standing-tree trick | Not found | 巻き枯らし (girdling) gave chips ≤42% MC (Kagoshima Univ.) | Not found |

## 2. What this means for fuel

- **Gasifier limits** (from [fuel demand doc](mitsue_50kwe_prototype_fuel_demand.md)): Volter ≤15%, Entrenco ≤12%, ESPE ≤45%, Esperia ≤40%. Fresh kiri at ~60% needs drying for every unit.
- **Kiri dries faster than sugi per the lumber data**, but the comparison is lumber (kiri) vs. logs in the yard (sugi). **Not like-for-like.**
- **Only sugi has a tested path to ~45%**: 葉枯らし + a sunny, ventilated yard, ~4 months. Forest-interior landings barely dried the logs.
- **Kiri tops and leaves are far wetter than the stem.** A kiri crop harvested in one lump (year ~5, per SANSEI) would need storage and drying capacity sized for the whole harvest.
- Drying heat at 50% → 15% is ≈2.0 GJ per t dry wood (~30% of CHP heat, before losses) per the fuel demand doc. Kiri at ~60% would need more.

### 2b. Energy and weight: bottom line

- **Per dry kilogram, kiri is slightly lower than sugi, not equal:** same-lab bomb calorimeter, Tochigi paper (Table 5): kiri wood 18.9 MJ/kg vs sugi 20.2 MJ/kg (about 6% lower). Across other kiri studies the range is 16.7–19.7 MJ/kg, so older notes saying "about the same" are only true within that spread.
- **Kiri's weight per m³ is low:** 231–335 kg/m³ dry across studies; the Japanese 4-year trees measured 209 kg/m³ at the butt-to-top mean of 255, against 302 for sugi. Its advantage is growth rate, not fuel density.
- **Fresh weight is mostly water.** At ~60% MC one fresh tonne holds only ~0.4 t dry wood, whichever species. Moisture matters more than species for hauling and drying cost.
- **Expert view (Sugimoto Kazuya, Tenkawa, 2026-10-15, personal opinion):** kiri wood is very low density, so he considers it low in energy and unsuitable for biomass. The Tochigi paper agrees on the per-m³ point (4.0 vs 6.1 GJ/m³ for sugi): more hauling, handling and storage per MWh.
- **Direct kiri-vs-sugi comparison (Nezu et al., BioEnergy Research 19:6, 2026; full paper read; copy in docs/energy-forest/source-scans/s12155-025-10943-8.pdf; funded by NEDO).** 15 four-year-old Paulownia (Mashiko, Tochigi), planted July 2020 at 3×3 m on **abandoned flat farmland with annual fertilizer, weeding, pest control, pruning**. Mean stem 15.6 cm diameter, 9.7 m tall, 0.0828 m³/tree. Compared with 9 Japanese species (Tables 5, 6, 7):

  | | Paulownia (4 yr) | Sugi |
  |---|---|---|
  | Gross calorific value, wood | 18.9 MJ/kg | 20.2 MJ/kg |
  | Basic density (oven-dry/green vol.) | 209 kg/m³ (stem mean 255) | 302 kg/m³ |
  | Energy per m³ of wood | **4.0 GJ/m³ (lowest of all 10 species; 66% of sugi)** | 6.1 GJ/m³ |
  | Ash, wood | **1.7% (JWBA chip class 3)** | 0.4% (class 1) |
  | Ash, bark | 4.5% (class 4) | 0.5% |
  | Potassium | 0.4% wood, 1.5% bark (clinker risk) | not measured |
  | Moisture, fresh (wet basis) | mean 58.2%; 70.5% at butt down to 47.6% at top | n/a in paper |
  | Annual yield per ha | 4.9 t/ha/yr, 93 GJ/ha/yr (whole stem) | 5.0 t/ha/yr, 101 GJ/ha/yr (48-yr stand) |

  Authors' conclusion: per m³ kiri is the worst fuel tested, but per hectare per year it roughly matches sugi because it grows fast, so it could work in short rotation. They note JWBA grading calls chips over 55% moisture unsuitable, so drying is required; upper-stem wood is drier, and using the lower stem for solid wood cuts drying cost. **Caveats for Mitsue:** per-ha figures are extrapolated from 15 average trees × 1,055 trees/ha on managed, flat farmland, with no deer or steep slope; the sugi comparator is a 48-year stand; one site, one age. Whole-stem yield falls to 47 GJ/ha/yr if the butt log goes to solid wood.
- **Croatian study (Vusić et al., GREEN 2018, Zagreb forestry faculty):** three hybrids (9501, Shang Tong, OXI); fresh MC 62.4 ± 1.7%, basic density 335 ± 27 kg/m³; also measured ash, CHNS and heating value for wood and bark. It does not compare with sugi. Source: [CROSBI 947148](https://www.bib.irb.hr/947148). The 19.3 MJ/kg figure above was not re-confirmed.
- **Ash:** Tochigi 1.7% (wood) vs sugi 0.4% (same method, same paper). Other kiri studies: 0.4% (COTEVISA-2, Springer 2024), 0.89% (trihybrid). Ash and potassium matter for gasifiers; kiri ash is higher than sugi in the one direct comparison.
- **Not found:** direct kiri-vs-sugi test on one site, sugi dry density from a primary source, hinoki density. Kiri tops/leaves have a higher ash/moisture load (unmeasured).

**Growing note:** kiri is frost-sensitive and needs good protection against bear and deer. Sugi and hinoki are established local species and are not frost-limited at Mitsue. Protection cost belongs in any kiri-vs-sugi fuel cost comparison.

## 3. Gaps — to measure or ask

1. Fresh MC of **京都皇帝早生桐** stemwood, at 5 and 7 years (ask SANSEI on 10/22; they may hold data).
2. Hinoki green MC (no number found); hinoki is not a priority fuel here.
3. Kiri chip/log drying time under Mitsue weather (Tottori's 4 months applies to sugi only).
4. **Gasification of kiri (searched 2026-10-15, English and Japanese): no gasifier test of Paulownia/kiri found.** Only lab properties (above), slow pyrolysis of Paulownia wood (Yorgun & Yıldız 2015, J. Anal. Appl. Pyrolysis; max conversion 77.4% at 773 K, liquid 54 wt%), and an unreviewed green-methanol concept article. No ash-fusion data for Paulownia. Risks for a downdraft gasifier (K-rich ash slagging, low bulk density feeding/bridging, moisture ~58%) are inferences from general biomass gasification and the Tochigi paper, not kiri tests. Ask CHP makers (Volter, Entrenco, ESPE, etc.) and Hokkaido FPRI (林産試験場, which tests species in downdraft gasifiers) whether they have run kiri.
5. Oven-dry MC tests (EN ISO 18134-2 method) on a few local sugi logs now, for a baseline.

## 4. Sources

- Kiri fresh MC 62.4% (hybrids, Croatia): [CROSBI — Fuel properties of Paulownia biomass](https://www.bib.irb.hr/947148)
- Kiri tree-part MC (trunk ~55%, branches ~100%, leaves >300%): found via the same search; the primary paper was not opened, **verify before citing** ([search result list](https://www.bib.irb.hr/947148))
- Kiri lumber drying (39 days to 20%): [Univ. of Kentucky — Quality of air-dried paulownia lumber](https://scholars.uky.edu/en/publications/quality-of-air-dried-paulownia-lumber/)
- Kiri dry calorific value ~16.7–17.8 MJ/kg: [BioResources 16(3) Paulownia sawdust](https://bioresources.cnr.ncsu.edu/wp-content/uploads/2021/05/BioRes_16_3_5083_Spirchez_JLB_Briquettes_Pellets_Paulownia_Sawdust_18793.pdf)
- Sugi large-log MC (162/115/209% dry basis): [J Wood Science, Matsumura et al. 2013 tables](https://jwoodscience.springeropen.com/articles/10.1007/s10086-013-1332-8/tables/2)
- Sugi/hinoki field MC and transpirational drying: [Hokkaido Univ. repository PDF](https://eprints.lib.hokudai.ac.jp/repo/huscap/all/21287/46(2)_P223-247.pdf)
- Sugi chip-log drying (葉枯らし, 4 months to 45%): [Tottori Prefecture R02-3-5](https://www.pref.tottori.lg.jp/secure/1253729/R02-3-5.pdf)
- Drying speed 1.2%/day, black vs red heartwood: [Ishikawa Prefecture 葉枯らし](https://www.pref.ishikawa.lg.jp/ringyo/publish/documents/sugihagarasi_1.pdf)
- Girdled sugi chips ≤42%: [Kagoshima Univ. paper](https://ir.kagoshima-u.ac.jp/record/2001572/files/10593065_paper.pdf)
- Kiri density 335 kg/m³ and HHV 19.3 MJ/kg: [CROSBI](https://www.bib.irb.hr/947148); air-dry density 273 kg/m³: [Dialnet PDF](https://dialnet.unirioja.es/descarga/articulo/8781137.pdf); 231 kg/m³: [Springer 2020](https://link.springer.com/article/10.1007/s00107-020-01497-x); heat of combustion 18.6 / 17.2 MJ/kg: [Springer 2024](https://link.springer.com/10.1007/s00107-024-02108-9)
- Sugi/hinoki heating value (5,274 / 5,346 kcal/kg): Kanagawa tree survey, as quoted in a search result; the underlying page was not opened, so **verify**. Related: [Yamagata biomass report](https://www.pref.yamagata.jp/documents/3843/h26mokushitubaio.pdf)
- Natural-drying limit 15–17%, sugi initial MC higher than hinoki: [Nara Prefecture 10kansou.pdf](https://www.pref.nara.jp/secure/237303/10kansou.pdf), [Nara 02kansou.pdf](https://www.pref.nara.jp/secure/238894/02kansou.pdf)
- Hinoki debarking/stacking: [Nagasaki Prefecture S-30-29](https://www.pref.nagasaki.jp/e-nourin/nougi/theme/result/H30seika-jouhou/shidou/S-30-29.pdf)
- Equilibrium MC ~15%: [Mie Prefecture](https://www.pref.mie.lg.jp/ringi/hp/000237699.htm)
