<p align="right">Version: v0.6 | Last modified: 2026-11-09</p>

# NAIST seminar, 13 Jan 2027: slide deck

Working deck for the 40-minute NAIST seminar. **20 slides: James Hill 1–10 (history), Rob Oudendijk 11–20.** The two presenters refer to each other's slides (tags like `→ ROB · 12`, `← JAMES · 9`, and `ASK` prompts), so the talk is a conversation. Hand-off cues are in the speaker notes. Kinjo-san is not presenting (decided 2026-11-09).

## Files

| File | What |
|---|---|
| `Mitsue_NAIST_Seminar_v0.6.pptx` | **Current deck (20 slides). Edit this.** |
| `Mitsue_NAIST_Seminar_v0.6.pdf` | Quick-look preview. Rendered with substitute fonts, so spacing differs from PowerPoint |
| `Mitsue_NAIST_Seminar_v0.5.*` (29 slides, has the cut slides: precedents, range sliders, push/pull diagram), `v0.4.*`, `v0.3.*`, `v0.2.*`, `v0.1.*` | Earlier versions (kept for roll-back) |
| `src/build_deck_v06.py` | Script that generated v0.6 (older scripts kept next to it) (python-pptx). Reference only once the pptx is hand-edited |
| `src/img/` | Photos used (from the project funding deck; check rights and who is shown before the talk). `rob_born_1958_upscaled.jpg` = Rob's newborn photo, upscaled by Rob to 1184×608 (original: `rob_born_1958.jpg`), OK'd by Rob for the public repo |

## Look

Same as the website mitsue.it: cream paper, deep green, clay accent; headlines in **Cormorant Garamond** with an italic emphasis, body in **IBM Plex Sans**, labels in **IBM Plex Mono**, Japanese in **Noto Serif JP**. These are free Google Fonts: **install them before opening the deck**, or PowerPoint substitutes other fonts and the layout shifts.
Palette (hex): paper `F5F1EA`, ink `1C1C1A`, deep green `1F3423`, green `39553F`, clay `9D6F48`, rule `D8D2C5`.

## Structure

**James (1–10):** 1 title and who is talking · 2 three centuries in one strip · 3 tenure and the Yoshino method · 4 Kan/Min · 5 Goryōrin · 6 cutover crisis · 7 postwar plans · 8 two curves cross · 9 seeds and the price crash · 10 the 1958 hinge (Rob's newborn photo).
**Rob (11–20):** 11 today · 12 three problems · 13 thinning wood left in the forest · 14 the idea (pull, don't push) · 15 what a tree is worth + replant · 16 first numbers and four unknowns · 17 energy sizing · 18 homework + open questions · 19 where we stand · 20 closing slogan + Q&A.
Charts on slides 6 and 8 are **schematic, not data**: James to replace with real series. Precedents (Tenkawa, Aizu, Buena Vista, IIJ Matsue) are now in the speaker notes of slide 14.

Terracotta-outlined "STILL RESEARCHING" tags mark slides where we show work in progress on purpose. All money figures are placeholders from model v1.2, not a forecast.

## Versioning (roll back and forward)

- One file per version: `Mitsue_NAIST_Seminar_v<major>.<minor>.pptx`. Never overwrite an older version's file: save under the new name, commit, tag.
- `v0.x` = drafts, `v1.0` = first version shown to NAIST, `v1.x` = fixes after review.
- Commit message `NAIST deck vX.Y: <what changed>`; tag `naist-deck-vX.Y` (`git tag`, then `git push --tags`). Roll back with `git checkout naist-deck-v0.1 -- decks/naist_2027-01-13/`.
- Update the version in the slide header text and in this README.

## Open items for v0.7

- [ ] James: rework history slides 1–10 (real planted-area vs firewood/charcoal series; price series for slide 9)
- [x] v0.3: newborn photo of Rob on the 1958 slide (13), approved by Rob
- [x] v0.6: cut from 29 to 20 slides (10 + 10) with cross-references between the presenters
- [x] v0.4: Rob's comment under it: "We are all born without clothes. We are all the same. Humans."
- [x] v0.5: upscaled newborn photo (Rob)
- [ ] Rob: photo rights/captions for the team photo (slides 13, 15) and the school photo (v0.5 only)
- [ ] One verified sentence per precedent on slide 24
- [ ] Refresh the open-questions table (slide 26) right before the talk
- [ ] Japanese version: decide bilingual slides or separate deck
