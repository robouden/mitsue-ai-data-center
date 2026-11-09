<p align="right">Version: v0.2 | Last modified: 2026-11-09</p>

# NAIST seminar, 13 Jan 2027: slide deck

Working deck for the 40-minute NAIST seminar. **Presenters: James Hill (history) and Rob Oudendijk.** Kinjo-san is not presenting (decided 2026-11-09).

## Files

| File | What |
|---|---|
| `Mitsue_NAIST_Seminar_v0.2.pptx` | **Current deck (29 slides). Edit this.** |
| `Mitsue_NAIST_Seminar_v0.2.pdf` | Quick-look preview. Rendered with substitute fonts, so spacing differs from PowerPoint |
| `Mitsue_NAIST_Seminar_v0.1.*` | Earlier, plainer version (kept for roll-back) |
| `src/build_deck_v02.py` | Script that generated v0.2 (python-pptx). Reference only once the pptx is hand-edited |
| `src/img/` | Photos used (from the project funding deck; check rights and who is shown before the talk) |

## Look

Same as the website mitsue.it: cream paper, deep green, clay accent; headlines in **Cormorant Garamond** with an italic emphasis, body in **IBM Plex Sans**, labels in **IBM Plex Mono**, Japanese in **Noto Serif JP**. These are free Google Fonts: **install them before opening the deck**, or PowerPoint substitutes other fonts and the layout shifts.
Palette (hex): paper `F5F1EA`, ink `1C1C1A`, deep green `1F3423`, green `39553F`, clay `9D6F48`, rule `D8D2C5`.

## Structure

1. 1–3: title, the two presenters, the 40-minute path
2. **4–13: History (10 slides), James.** Skeleton from `docs/energy-forest/history/naist_timeline_history_to_1958.md`. Replace, merge or re-order freely. Speaker notes carry sources. Two charts (slides 9, 11) are **schematic, not data**: James to replace with real series.
3. 14–16: today (village facts, three problems, thinning wood left in the forest)
4. 17–23: the idea (pull not push, A/B/C/D wood, replanting), first numbers, four unknowns, energy sizing
5. 24–27: precedents, homework done, open questions, where we stand
6. 28–29: closing slogan, Q&A

Terracotta-outlined "STILL RESEARCHING" tags mark slides where we show work in progress on purpose. All money figures are placeholders from model v1.2, not a forecast.

## Versioning (roll back and forward)

- One file per version: `Mitsue_NAIST_Seminar_v<major>.<minor>.pptx`. Never overwrite an older version's file: save under the new name, commit, tag.
- `v0.x` = drafts, `v1.0` = first version shown to NAIST, `v1.x` = fixes after review.
- Commit message `NAIST deck vX.Y: <what changed>`; tag `naist-deck-vX.Y` (`git tag`, then `git push --tags`). Roll back with `git checkout naist-deck-v0.1 -- decks/naist_2027-01-13/`.
- Update the version in the slide header text and in this README.

## Open items for v0.3

- [ ] James: rework history slides 4–13 (real planted-area vs firewood/charcoal series; price series for slide 12)
- [ ] Rob: confirm the 1958 / birth-year line on slide 13, and photo rights/captions (slides 16, 24, 25)
- [ ] One verified sentence per precedent on slide 24
- [ ] Refresh the open-questions table (slide 26) right before the talk
- [ ] Japanese version: decide bilingual slides or separate deck
