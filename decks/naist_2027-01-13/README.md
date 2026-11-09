<p align="right">Version: v0.1 | Last modified: 2026-11-09</p>

# NAIST seminar, 13 Jan 2027: slide deck

Working deck for the 40-minute NAIST seminar (Kinjo Rie, James Hill, Rob Oudendijk).
Style follows the Komatsu draft deck; the content is new.

## Files

| File | What |
|---|---|
| `Mitsue_NAIST_Seminar_v0.1.pptx` | The deck (28 slides). Edit this. |
| `Mitsue_NAIST_Seminar_v0.1.pdf` | Quick-look PDF of the same version |
| `src/build_deck.py` | Script that generated v0.1 (python-pptx). Reference only once the pptx is hand-edited |
| `src/title_illustration.png` | Title-slide picture |

## Structure

1. Slides 1–3: title, who is talking, 40-minute plan
2. **Slides 4–13: History (10 slides), James.** Skeleton from `docs/energy-forest/history/naist_timeline_history_to_1958.md`. Replace, merge or re-order freely. Every history slide has speaker notes with sources and a note for James.
3. Slides 14–15: Today (Kinjo-san's part, placeholder + village facts)
4. Slides 16–22: the problem, the idea, first numbers, energy
5. Slides 23–26: precedents, homework done, open questions, where we stand
6. Slides 27–28: closing, Q&A

Terracotta "STILL RESEARCHING" tags mark slides where we show work in progress on purpose.
All money figures are placeholders from the model v1.2 and not a forecast.

## Versioning (so we can roll back and forward)

- One file per version name: `Mitsue_NAIST_Seminar_v<major>.<minor>.pptx`. Do not overwrite an older version's file; save a new name, commit, tag.
- Suggested: `v0.x` = drafts, `v1.0` = first version shown to NAIST, `v1.x` = fixes after review.
- Commit message: `NAIST deck vX.Y: <what changed>`. Tag with `naist-deck-vX.Y`.
- Update the version in the footer text of the slides and in this README's header.

## Open items for v0.2

- [ ] James: rework history slides 4–13 (data for the planted-area vs firewood/charcoal chart on slide 11)
- [ ] Kinjo-san: replace slide 14 with her material; check the numbers on slides 15 and 17 with her
- [ ] Confirm dress-code idea (slide 2) and Rob's birth-year line (slide 13) with the people concerned
- [ ] One verified sentence per precedent on slide 23
- [ ] Refresh the open-questions table (slide 25) right before the talk
- [ ] Japanese version (decide: bilingual slides or separate deck)
