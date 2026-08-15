<!-- Version: v1.1 | Last modified: 2026-08-14 -->

# FAQ: Community Participation in Data Center Compute (not just forest/energy)

Questions from a friend, 2026-07-20.

## Q1: How will Mitsue residents and landowners participate in what runs on the data center, not just the forest and energy parts?

- Reserve a fixed compute quota (e.g. 10–15%) for community/local-benefit workloads, priced at cost or free — mirrors how FIP treats grid export as "overflow"; community use becomes the overflow-of-compute equivalent.
- Landowners whose forest feeds the CHP get compute credits, not just biomass payment — ties their land directly to a tangible service (e.g. free storage/hosting for a family business site).

## Q2: Do you imagine any role for residents, farmers, foresters, teachers, kids, etc. in proposing or co-running data-center projects (local mapping, environmental monitoring, educational tools)?

- The tree-survey app (bilingual FastAPI+DuckDB field-data tool) is a template — same pattern could extend to disaster/weather monitoring, wildlife cams, elderly check-in systems.
- Concrete asks: foresters propose forest-health/trail-condition dashboards; farmers propose irrigation/frost-alert tools; teachers co-design a "kids build something on the village computer" unit (ties into existing school outreach thread).
- Structure as a lightweight proposal process — anyone pitches a small project, village decides which get compute time — rather than a top-down approved list.

## Q3: Will you publish per-tenant/per-project usage data, so the community can see how it's serving local needs vs. outside orgs?

- Yes — a public dashboard showing % compute to local vs. outside tenants defuses the "outsiders extracting village resources" worry before it's even asked, especially given current outside-investor optics (Mizuho, more trees).
- Keep it simple: a monthly one-pager (energy in, jobs run, local/outside split), not raw logs — avoids tenant confidentiality issues.

## Q4: How will you tie data-center metrics (energy, workloads, uptime) back to things villagers care about day-to-day? And manage these requests?

- Translate kWh/uptime into felt terms: "ran X hours of school computer time," "powered the onsen's heat pump," "covered village hall for a day" — same instinct as the CHP framing (dispatchable baseload beats the abstract "renewable" label).
- Route project requests through 御杖村森林組合/Mitsue Village Forest Association or the village office (existing 請願/陳情 channel) rather than an ad hoc queue — gives proposals legitimacy and keeps them inside a process officials already recognize.
