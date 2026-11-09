#!/usr/bin/env python3
"""Build the NAIST 13 Jan 2027 seminar deck (python-pptx).

Run from anywhere:  python3 build_deck.py
Output: ../Mitsue_NAIST_Seminar_v<VERSION>.pptx
Style: same as the Komatsu draft deck (dark green / cream / terracotta,
Georgia titles, Arial body, Courier New labels). Content is new.
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION

VERSION = "0.1"
DATE = "2026-11-09"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", f"Mitsue_NAIST_Seminar_v{VERSION}.pptx")
ILLUSTRATION = os.path.join(HERE, "title_illustration.png")

# palette (taken from the Komatsu draft deck)
GREEN = RGBColor(0x2F, 0x4A, 0x37)
GREEN2 = RGBColor(0x3A, 0x7A, 0x5A)
CREAM = RGBColor(0xF3, 0xEC, 0xE0)
CARD = RGBColor(0xEC, 0xE3, 0xD3)
TERRA = RGBColor(0xC4, 0x66, 0x3A)
INK = RGBColor(0x1F, 0x2A, 0x24)
GREY = RGBColor(0x4C, 0x55, 0x4F)
SERIF, SANS, MONO = "Georgia", "Arial", "Courier New"

FOOT = f"NAIST SEMINAR · 13 JAN 2027 · v{VERSION} DRAFT · WORK IN PROGRESS"

prs = Presentation()
prs.slide_width = Emu(18288000)   # 20 in
prs.slide_height = Emu(10287000)  # 11.25 in
BLANK = prs.slide_layouts[6]
pagers = []  # (textbox, index)


# ---------------------------------------------------------------- helpers
def rect(s, x, y, w, h, fill, shape=MSO_SHAPE.RECTANGLE):
    r = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    r.fill.solid()
    r.fill.fore_color.rgb = fill
    r.line.fill.background()
    r.shadow.inherit = False
    return r


def text(s, x, y, w, h, paras, font=SANS, size=22, color=INK, bold=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, spacing=1.12, after=6,
         italic=False):
    """paras: str | list of str | list of list-of-(text, overrides) runs."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    if isinstance(paras, str):
        paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        p.space_after = Pt(after)
        runs = [(para, {})] if isinstance(para, str) else para
        for t, o in runs:
            r = p.add_run()
            r.text = t
            f = r.font
            f.name = o.get("font", font)
            f.size = Pt(o.get("size", size))
            f.bold = o.get("bold", bold)
            f.italic = o.get("italic", italic)
            f.color.rgb = o.get("color", color)
    return tb


def notes(s, body):
    s.notes_slide.notes_text_frame.text = body


def base(section, title, dark=False, sources=None):
    """Standard content slide with the project header/footer."""
    s = prs.slides.add_slide(BLANK)
    rect(s, 0, 0, 20, 11.25, GREEN if dark else CREAM)
    fg = CREAM if dark else GREEN
    text(s, 0.9, 0.5, 0.9, 0.9, "御", font="Noto Serif JP", size=40, color=fg)
    text(s, 1.8, 0.62, 8, 0.4, "MITSUE PROJECT", font=MONO, size=13, color=GREY if not dark else CARD)
    text(s, 1.8, 1.0, 12, 0.4, section, font=MONO, size=15, color=TERRA)
    text(s, 0.9, 1.75, 18.2, 1.7, title, font=SERIF, size=44, bold=True,
         color=CREAM if dark else INK, anchor=MSO_ANCHOR.TOP, spacing=1.0)
    text(s, 0.9, 10.55, 14, 0.4, FOOT, font=MONO, size=13, color=GREY if not dark else CARD)
    pg = text(s, 16.3, 10.55, 2.8, 0.4, "", font=MONO, size=13,
              color=GREY if not dark else CARD, align=PP_ALIGN.RIGHT)
    pagers.append(pg)
    if sources:
        text(s, 0.9, 10.15, 18, 0.4, "Sources: " + sources, font=MONO, size=11, color=GREY)
    return s


def stamp(s, label="STILL RESEARCHING", x=16.0, y=0.55, w=3.1):
    """Terracotta outlined tag: we did the homework, we are not done."""
    b = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(0.5))
    b.fill.background()
    b.line.color.rgb = TERRA
    b.line.width = Pt(1.75)
    b.shadow.inherit = False
    tf = b.text_frame
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = label
    r.font.name, r.font.size, r.font.bold = MONO, Pt(13), True
    r.font.color.rgb = TERRA


def card(s, x, y, w, h, head, body, accent=GREEN, fill=CARD, head_color=None,
         body_size=21, head_size=24):
    rect(s, x, y, w, h, fill)
    rect(s, x, y, 0.09, h, accent)
    text(s, x + 0.3, y + 0.2, w - 0.5, 0.7, head, font=SERIF, size=head_size,
         bold=True, color=head_color or accent)
    text(s, x + 0.3, y + 0.95, w - 0.5, h - 1.1, body, size=body_size, after=8)


def dark_card(s, x, y, w, h, head, body, fill=GREEN, head_color=CREAM, body_color=CREAM,
              body_size=21, head_size=26):
    rect(s, x, y, w, h, fill)
    text(s, x + 0.3, y + 0.25, w - 0.6, 0.9, head, font=SERIF, size=head_size,
         bold=True, color=head_color)
    text(s, x + 0.3, y + 1.15, w - 0.6, h - 1.3, body, size=body_size, color=body_color, after=8)


def history(idx, era, title, rows, why, src, note):
    """History slide: dated rows on the left, 'why it matters' card on the right."""
    s = base(f"HISTORY {idx:02d} / 10 · {era}", title, sources=src)
    stamp(s, "JAMES · TO EXPAND", x=15.6, w=3.5)
    y = 3.35
    rh = 1.68 if len(rows) >= 4 else 2.05
    for d, h, b in rows:
        rect(s, 0.9, y, 11.6, rh - 0.15, CARD)
        rect(s, 0.9, y, 0.09, rh - 0.15, TERRA)
        text(s, 1.2, y + 0.1, 2.1, 0.5, d, font=MONO, size=14, bold=True, color=TERRA)
        text(s, 3.4, y + 0.08, 9.0, 0.5, h, font=SERIF, size=21, bold=True, color=GREEN)
        text(s, 3.4, y + 0.52, 9.0, rh - 0.65, b, size=16, color=INK, spacing=1.0, after=0)
        y += rh
    dark_card(s, 12.9, 3.35, 6.2, y - 3.5, "Why it matters here", why, body_size=20, head_size=26)
    notes(s, note + "\n\nFor James: this slide is a skeleton from "
          "docs/energy-forest/history/naist_timeline_history_to_1958.md. "
          "Replace or expand freely; keep the layout or change it.")
    return s


# ---------------------------------------------------------------- 1 title
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, 20, 11.25, GREEN)
text(s, 0.9, 0.5, 0.9, 0.9, "御", font="Noto Serif JP", size=40, color=CREAM)
text(s, 1.8, 0.62, 8, 0.4, "MITSUE PROJECT", font=MONO, size=13, color=CARD)
text(s, 1.8, 1.0, 14, 0.4, "NAIST SEMINAR · 御杖村 · NARA PREFECTURE", font=MONO, size=15, color=TERRA)
text(s, 0.9, 2.3, 11.2, 3.2, "Planted for a market that no longer exists", font=SERIF, size=54,
     bold=True, color=CREAM, spacing=1.0)
text(s, 0.9, 5.4, 10.5, 1.4,
     ["A forest, a village, and a sideways idea:", "history, today, and what we are still working out"],
     size=25, color=CREAM)
text(s, 0.9, 7.2, 11, 1.2,
     ["Wednesday 13 January 2027 · NAIST", "Kinjo Rie (Mitsue Kanko) · James Hill · Rob Oudendijk (Mitsue-it)"],
     font=MONO, size=16, color=TERRA)
text(s, 0.9, 10.55, 14, 0.4, f"v{VERSION} DRAFT · {DATE} · WORK IN PROGRESS", font=MONO, size=13, color=CARD)
pg = text(s, 16.3, 10.55, 2.8, 0.4, "", font=MONO, size=13, color=CARD, align=PP_ALIGN.RIGHT)
pagers.append(pg)
s.shapes.add_picture(ILLUSTRATION, Emu(10424160), Emu(1828800), Emu(6949440), Emu(6177280))
notes(s, "Title is a working title. The hook line is from the history segment: the sugi standing in Mitsue today were "
         "planted for a timber and firewood economy that fossil fuels had started dismantling by 1950.")

# ---------------------------------------------------------------- 2 intro
s = base("§ 00 · WHO IS TALKING", "Three people, one forest, some trees very close to the front door")
card(s, 0.9, 3.5, 5.7, 4.9, "Kinjo Rie", [
    "Mitsue Kanko. Lives and works in the village; knows what the forest looks like on a Tuesday, not just in a plan.",
    "Takes the middle of the talk: the situation on the ground today."], body_size=23, accent=GREEN2)
card(s, 6.9, 3.5, 5.7, 4.9, "James Hill", [
    "Forest history researcher. Walks us through how Japan ended up with this much sugi, and why.",
    "Takes the first part of the talk."], body_size=23, accent=GREEN)
card(s, 12.9, 3.5, 6.2, 4.9, "Rob Oudendijk", [
    "Dutch engineer. Built his own house in the Mitsue forest, so the trees are 3 m from the front door.",
    "If the talk goes badly, blame the neighbours.",
    ], body_size=23, accent=TERRA)
text(s, 0.9, 8.7, 18, 0.6, "Dress-code idea (pending Kinjo-san's OK): she in green, new growth; he in grey, fully grown. Together: one forest.",
     font=MONO, size=14, color=TERRA)
notes(s, "Intro ~3 min. Dress-code gag is NOT confirmed: ask Kinjo before keeping it. Check James's own bio line with him.")

# ---------------------------------------------------------------- 3 agenda
s = base("§ 00 · THE PLAN FOR 40 MINUTES", "History, today, a sideways idea, and what we have not figured out yet")
items = [("1", "History", "Japanese forestry, from the Tokugawa to 1958", "James", GREEN),
         ("2", "Today", "The forest and village as they are now", "Kinjo-san", GREEN2),
         ("3", "The problem", "Three problems with one shape", "Rob", GREEN),
         ("4", "The idea", "Pull, don't push: wood, power, replanting", "Rob", TERRA),
         ("5", "Homework", "What we checked, and what we still do not know", "All", GREEN)]
y = 3.5
for n, h, b, who, c in items:
    rect(s, 0.9, y, 18.2, 1.05, CARD)
    rect(s, 0.9, y, 1.2, 1.05, c)
    text(s, 0.9, y, 1.2, 1.05, n, font=SERIF, size=34, bold=True, color=CREAM,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 2.4, y + 0.05, 3.6, 0.95, h, font=SERIF, size=28, bold=True, color=GREEN, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 6.2, y + 0.05, 9.5, 0.95, b, size=23, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 16.4, y + 0.05, 2.5, 0.95, who, font=MONO, size=16, color=TERRA, anchor=MSO_ANCHOR.MIDDLE)
    y += 1.2
text(s, 0.9, 9.7, 18, 0.5, "Tone: light, not academic. Big scary problems sometimes have weirdly simple solutions, if you look at them sideways.",
     font=MONO, size=14, color=GREY)
notes(s, "40 min total, split with Kinjo. See docs/meetings/naist_2027-01-13_presentation_draft.md for the running order. "
         "Time boxes there: intro 3, history 10, Kinjo 5-10, problems 5, plan 10, Q&A 5.")

# ---------------------------------------------------------------- 4-13 HISTORY (10 slides)
history(1, "1603–1958 · THE WHOLE STORY IN ONE LINE",
        "Three centuries in one strip: how Japan came to plant so much sugi",
        [("1603–1867", "Tokugawa", "Land is feudal or communal. Edo and Osaka grow huge and burn and rebuild; planted timber starts to pay."),
         ("1868–1947", "Meiji to the war", "Forests are split between state and village; the Imperial estate runs forestry as a real business."),
         ("1929–1949", "Cutting outruns planting", "Twenty years of overcutting, then wartime emergency harvest."),
         ("1950–1958", "Replant, replant, replant", "Compulsory planting, three national plans, the biggest boom ever.")],
        ["Four chapters, ten slides.",
         "The punchline arrives in 1958: the trees we see today were planted just as the demand behind them began to fade."],
        "Totman; Iwamoto; Matsushita (2015)",
        "Overview slide for the history segment (~10 min, ~8-10 slides). James to restructure as he prefers.")

history(2, "1603–1867 · TOKUGAWA TENURE AND THE FIRST PLANTING WAVE",
        "Who owns a tree on shared land? The question that made plantations possible",
        [("1603–1867", "Tenure", "Land is held by feudal lords or villages in common; private land ownership is banned in principle. Lord's forests in Kiso are guarded and theft is severely punished."),
         ("1665 · 1724", "Kiso reforms", "1665: cutting halved by seedling protection and patrols, reversed within years for revenue. 1724: cut down by more than 60%, and this time held for 30 years."),
         ("late 1600s", "Wave 1", "Edo and Osaka boom; a 50-year timber investment pays for the first time. Local custom starts to recognise private ownership of planted trees even on communal land (Yoshino, Owase)."),
         ("1801", "Edo", "Population of Edo around 1,000,000, bigger than London or Paris. With imports shut out, all demand falls on domestic forests.")],
        ["Plant a tree on land you do not own, and who gets the timber 50 years later?",
         "The answer worked out in Yoshino and Owase, in the 1600s, is the same question that sits behind Mitsue's private woodlots now."],
        "Iwamoto; Totman, Green Archipelago",
        "Sources: totman_green_archipelago_notes.md, iwamoto_development_japanese_forestry_summary.md. 1779 Kiso first forest inventory can be added.")

history(3, "1750–1849 · CRAFT, GUILDS AND A PLANTING SCHEDULE",
        "Edo-era foresters already had a recipe: plant dense, thin early, thin again",
        [("1750s", "Yamaguni guild adapts", "A rural timber guild creates a new licence class so plantation-growers can join without losing collective control. Rural producers start out-organising city merchants."),
         ("1779", "Kiso inventory", "First forest inventory and planning: early sustained-yield thinking."),
         ("1849", "The Yoshino method, written down", "Okino Takao (Kurobane domain) documents: plant at 3 ft, thin at 2–3 inch butt, rethin at 5 years, final spacing 12 ft. A citable schedule that still looks familiar."),
         ("", "Over 250 years later", "Plantations of this kind are what stand on Mitsue's slopes.")],
        ["The thinning rules are old. What is new is that there is nobody to do the thinning.",
         "Good hook into Kinjo-san's segment on the day-to-day work now."],
        "Totman; Iwamoto",
        "Optional slide: can be merged into slide 2 if time is short. Keep the Yoshino method line, it is the most quotable.")

history(4, "1868–1889 · KAN / MIN",
        "Meiji tries to divide every woodland into 'government' or 'private'",
        [("1868", "Meiji Restoration", "Formal land ownership is introduced. National forests are carved out of communal and former feudal land."),
         ("1871–76", "Six policy reversals in five years", "Villagers need gen'ya, mixed scrub for fodder and fuel. The state wants sanrin, dense conifer. A third category, koyuchi (shared use), appears because the first two do not fit real life."),
         ("1889", "Result", "Government forest reaches 53% of Japan's woodland (31% in 1880). Messy: use-rights linger on both sides."),
         ]
        , ["The same tension in a Japanese village: what the state wants from the forest is not what the village needs.",
           "Worth a joke: six policy reversals in five years is a pace most of us would not call 'planning'."],
        "Totman, 'Green Archipelago'",
        "Source: totman_green_archipelago_notes.md. Villagers' use rights (iriai) could be a nice small side-story.")

history(5, "1889–1947 · GORYŌRIN",
        "For 58 years, forestry was a real business: the Imperial forests",
        [("1889–90", "Founded", "About 1.6 million ha carved out as the Imperial Household's own income-producing forest estate."),
         ("1892", "Turns profitable", "After one or two loss-making years: the start of a real sustained-yield P&L."),
         ("1936–45", "Peak", "Around 40% net margin on gross income, against 23% for the much larger National Forest. 31% of Household income in 1940."),
         ("1942–47", "Override and end", "'Hundred Year Plan' suspended in wartime; harvest up by cutting replanting. Dissolved 1947; asset value had reached ¥2.6bn, 70% of Household wealth.")],
        ["Managed Japanese forestry was, for decades, a real bankable asset and not a subsidised cost.",
         "Our own slogan 'Grow the Forest. Grow the Village.' comes from a hundred-year plan like this."],
        "Totman, Goryōrin and lumber industry notes",
        "Source: totman_goryorin_lumber_industry_notes.md. hundred_year_plan_transcription.md for the plan text. Good place for a simple profit curve if James has the data.")

history(6, "1929–1949 · THE CUTOVER CRISIS",
        "Twenty years in a row, more forest was cut than planted",
        [("1929–49", "The gap", "Annual cut area exceeds planted area nationally every year for two decades; the gap peaks in the mid-1940s."),
         ("1942–44", "Wartime override", "'Special harvesting' authorised: harvest rises from 8.6 to 10.97 million koku, paid for by cutting reforestation and aftercare."),
         ("1948", "Cutover land", "1.49 million ha, around 6% of Japan's forest area, concentrated near villages."),
         ("1948", "The forecast", "GHQ and Forestry Agency studies predict domestic wood will run out within 15–33 years (wrong, in hindsight, but it drove everything that followed).")],
        ["A scarcity scare, followed by a planting rush.",
         "Many of Mitsue's stands are the direct descendants of that rush."],
        "Matsushita (2015); Totman",
        "Source: matsushita_2015_postwar_forestation_policies_summary.md.")

history(7, "1949–1961 · POSTWAR PLANS",
        "Three plans in twelve years, and planting becomes compulsory",
        [("1949–53", "5-Year Plan", "First full postwar plan for 1.5 million ha of cutover land; budget shortfalls keep execution at 60–70%."),
         ("1951", "Forest Act amended", "Planting made compulsory for the first time (Article 14). Same year: log import tariffs cut to near zero."),
         ("1952–61", "10-Year Plan", "Self-sufficiency in industrial roundwood through broadleaf-to-conifer conversion (0.84 million ha planned)."),
         ("1955–60", "6-Year Plan", "From quantity to quality: nursery stock, seed trees, 'right tree, right site'.")],
        ["Broadleaf-to-conifer conversion is exactly what we now want to undo, in places where it makes sense.",
         "A tidy irony for the talk: the plan of the 1950s and the plan of the 2020s point in opposite directions."],
        "Matsushita (2015)",
        "Source: matsushita_2015_postwar_forestation_policies_summary.md. The broadleaf-to-conifer irony is Rob's addition; James to check it holds for the Nara region.")

history(8, "1950–1955 · TWO CURVES CROSS",
        "Just as planting peaks, the reason for planting starts to disappear",
        [("1950", "The demand floor drops out", "Fossil fuels replace firewood and charcoal, chemical fertiliser replaces green fertiliser, machinery replaces draft animals. Village woodland (gen'ya) starts to lose its value."),
         ("1954", "Peak planting year", "Highest annual planted area recorded under the 10-Year Plan."),
         ("1955–1970", "Wave 3, the biggest", "Postwar recovery drives the largest of Japan's three plantation booms. Artificial planting peaks in 1955 and stays high until 1970."),
         ]
        , ["Planting goes up. Demand for what the trees were meant to supply goes down.",
           "(Idea for James: a simple two-line chart here, 'planted area' vs 'firewood and charcoal use'. Schematic is fine if labelled.)"],
        "Totman; Iwamoto; Matsushita",
        "A chart slide would work well. Data: Forestry Agency planted-area series and the energy-use series; to be sourced by James.")

history(9, "1951–1980 · SEEDS PLANTED IN THE FIFTIES",
        "Two quiet decisions that explain the next 70 years",
        [("1951", "Import tariffs cut", "Log import tariffs lowered to near zero. At the time it looked sensible; it set up self-sufficiency to fall for decades."),
         ("1956", "Forest Development Corporation", "A national vehicle, with prefectural corporations from 1959, plants the least attractive land with long-term debt against a 40–50-year harvest. All 47 prefectural corporations end up in debt distress once stumpage prices collapse after 1980."),
         ("1970s–80s", "Cheap imports", "The market crashes before the planted trees grow up. A-grade sugi falls from about ¥12,000 to ¥4,475/m³ by 2025.")],
        ["We planted a retirement fund, then the market crashed before the trees were old enough to cash in.",
         "Only A-grade wood sells today. That is the problem the later part of the talk tries to solve."],
        "Matsushita (2015); price series to be confirmed",
        "The ¥12,000 → ¥4,475/m³ line is in the draft talk outline (docs/meetings/naist_2027-01-13_presentation_draft.md); original price series and years to be sourced by James before it goes on a slide.")

history(10, "1958 · THE HINGE",
         "1958: Rob's birth year, and the year the story turns",
         [("1958", "Deep in the biggest boom", "Planting compulsory since 1951; self-sufficiency still about 95% and about to start its long decline."),
          ("1958", "A new financing model", "The Profit-Sharing Forestation Act follows the same year; debt-financed corporate planting is formalised."),
          ("today", "What is standing now", "The sugi and hinoki in Mitsue's mountains were planted in exactly this window.")],
         ["The trees are older than the demand that justified planting them.",
          "That is the hinge into 'today'. Over to Kinjo-san."],
         "Matsushita (2015); Iwamoto; Rob's own notes",
         "Hinge line from docs/energy-forest/history/naist_timeline_history_to_1958.md. Rob was born 1958-11-30, check with Rob whether he wants that on the slide.")

# ---------------------------------------------------------------- 14 Kinjo segment
s = base("§ 01 · TODAY · KINJO-SAN", "The forest as it is now: Kinjo-san's slides go here", sources="to be written with Kinjo-san")
rect(s, 0.9, 3.5, 18.2, 5.9, CARD)
rect(s, 0.9, 3.5, 0.09, 5.9, GREEN2)
text(s, 1.4, 3.8, 17, 5.2, [
    [("Placeholder. ", {"bold": True, "color": TERRA}), ("Kinjo-san decides what she wants to show: the day-to-day, photos of the forest, what the work looks like.", {})],
    "Ideas to offer her, not requirements:",
    "·  A few photos of the stands: thinned, unthinned, left-in-forest wood",
    "·  What the cooperative does, and what it cannot do at the moment",
    "·  What the village hall plan says about thinning (see next slides)",
    "·  What she would like NAIST students to look at"], size=24, after=14)
notes(s, "5-10 min, hers. Keep this slide as a divider, or replace it with her own deck. Do not put words in her mouth: "
         "share the numbers on the next slides with her before the talk.")

# ---------------------------------------------------------------- 15 village facts
s = base("§ 01 · TODAY · THE SETTING", "A village of about 1,400 people, and a forest of about 7,000 hectares",
         sources="Village forestry plan; Mitsue statistics; draft outline")
for i, (big, small) in enumerate([("≈ 1,400", "residents"), ("≈ 93 %", "forest cover"),
                                  ("≈ 7,050 ha", "forest, over 90% private"), ("50–60 yr", "age of the main sugi and hinoki stands")]):
    x = 0.9 + i * 4.6
    rect(s, x, 3.5, 4.3, 2.5, CARD)
    rect(s, x, 3.5, 4.3, 0.09, TERRA)
    text(s, x + 0.2, 3.8, 3.9, 1.1, big, font=SERIF, size=40, bold=True, color=GREEN)
    text(s, x + 0.2, 4.9, 3.9, 1.0, small, size=20, color=GREY)
text(s, 0.9, 6.5, 18.2, 3.4, [
    "Most of the forest is private, many owners are elderly or live elsewhere, and a lot of it was planted in the 1950s–60s boom you just saw.",
    "At today's prices a cut sugi barely pays for the cutting. Only the straight, clean A-grade logs sell, and even that price has fallen by about two thirds since the 1980s.",
    [("Still checking: ", {"bold": True, "color": TERRA}), ("how many owners, how many parcels, who inherits. The forest register is with the village hall.", {})]],
     size=24, after=14)
stamp(s)
notes(s, "Figures: residents and cover from the existing project deck; 7,051 ha and >90% private from the village plan. "
         "Price drop: ¥12,000 → ¥4,475/m³ A-grade sugi (outline); source to confirm.")

# ---------------------------------------------------------------- 16 problems
s = base("§ 02 · THE PROBLEM", "Three problems with one shape: nobody is paid to fix it")
card(s, 0.9, 3.5, 5.9, 5.4, "1  Not enough hands", [
    "The cooperative is small and has few young people. Harvest at scale needs machines and trained operators; we have neither yet.",
    "Thinning is planned, but most of it is cut and left."], accent=TERRA, head_color=TERRA, body_size=23)
card(s, 7.0, 3.5, 5.9, 5.4, "2  A ticking clock", [
    "A large share of the forest reaches harvest age inside the same ~25-year window.",
    "The same window in which new small-scale power technology matures. Nice timing, if we use it."], accent=GREEN, body_size=23)
card(s, 13.1, 3.5, 6.0, 5.4, "3  No pull to replant", [
    "Cutting sugi for cheap lumber does not pay enough to put anything back.",
    "Short-term profit, repeat forever. Nobody has a reason to break the cycle."], accent=GREEN2, body_size=23)
notes(s, "~5 min. Source structure: docs/meetings/naist_2027-01-13_presentation_draft.md section 4. "
         "Council minutes 2020: Mayor named the worker shortage as the bottleneck.")

# ---------------------------------------------------------------- 17 chart: left in forest
s = base("§ 02 · THE PROBLEM IN NUMBERS", "Most of the thinning wood stays in the forest", sources="Village forestry plan R6–R8 (FY2024–26); Oba, village hall")
cd = CategoryChartData()
cd.categories = ["Planned thinning FY2024–26"]
cd.add_series("Cut and left in the forest", (18140,))
cd.add_series("Taken out", (2574,))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_STACKED, Inches(0.9), Inches(3.5), Inches(11.4), Inches(4.2), cd)
ch = gf.chart
ch.has_legend = True
from pptx.enum.chart import XL_LEGEND_POSITION
ch.legend.position = XL_LEGEND_POSITION.BOTTOM
ch.legend.include_in_layout = False
ch.legend.font.size = Pt(16)
ch.legend.font.name = SANS
ch.value_axis.visible = False
ch.value_axis.has_major_gridlines = False
ch.category_axis.visible = False
ch.plots[0].gap_width = 40
ch.plots[0].overlap = 100
for ser, col in zip(ch.plots[0].series, (TERRA, GREEN)):
    ser.format.fill.solid()
    ser.format.fill.fore_color.rgb = col
    ser.data_labels.show_value = True
    ser.data_labels.number_format = '#,##0" m³"'
    ser.data_labels.number_format_is_linked = False
    ser.data_labels.font.size = Pt(18)
    ser.data_labels.font.bold = True
    ser.data_labels.font.color.rgb = CREAM
    ser.data_labels.position = XL_LABEL_POSITION.CENTER
dark_card(s, 12.7, 3.5, 6.4, 4.2, "≈ 88 % stays put", [
    "113 parcels, about 222 ha, in 4 districts.",
    "About 20,700 m³ planned; about 860 m³ a year actually comes out."], body_size=21)
text(s, 0.9, 8.1, 18.2, 1.9, [
    "That cut-and-left wood is a fuel resource, if it can be collected at a price that makes sense. Steep slopes and missing roads are why it is left.",
    [("Still checking: ", {"bold": True, "color": TERRA}), ("how much of it is reachable with a winch-assisted machine, and what an earlier '120–300 m³/yr' cooperative figure really measured.", {})]],
     size=21, after=10)
stamp(s)
notes(s, "18,140 of 20,714 m³ left; 2,574 m³ out over three years (about 860/yr). Verify the split and parcel counts with the village data sheet (xlsx) before the talk.")

# ---------------------------------------------------------------- 18 idea: pull don't push
s = base("§ 03 · THE IDEA", "Pull, don't push: give the wood a buyer that pays")
steps = [("1  Thin and clear", "Cut-to-length machines on steep sugi", GREEN),
         ("2  Sort A / B / C / D", "A and B to the sawmill; C and D to chips", GREEN),
         ("3  Chip and dry", "Local chipping, drying with CHP heat", GREEN),
         ("4  Small CHP", "Gasification plant: power and heat, 24 h", GREEN)]
for i, (h, b, c) in enumerate(steps):
    x = 0.9 + i * 4.65
    rect(s, x, 3.5, 4.2, 2.7, c if i else TERRA)
    text(s, x + 0.25, 3.7, 3.8, 0.8, h, font=SERIF, size=24, bold=True, color=CREAM)
    text(s, x + 0.25, 4.6, 3.8, 1.5, b, size=20, color=CREAM)
    if i < 3:
        text(s, x + 4.2, 4.3, 0.45, 0.7, "›", font=SERIF, size=34, bold=True, color=TERRA, align=PP_ALIGN.CENTER)
rect(s, 0.9, 6.6, 18.2, 0.06, TERRA)
text(s, 0.9, 6.85, 8.8, 3.0, [
    [("Why 'pull'. ", {"bold": True, "color": GREEN, "font": SERIF, "size": 26})],
    "Waiting for a subsidy pushes wood out of the forest once, then stops. A buyer that wants fuel 24 hours a day pulls wood out every year, and can pay for the replanting."], size=21)
text(s, 10.1, 6.85, 9.0, 3.0, [
    [("Then replant. ", {"bold": True, "color": GREEN, "font": SERIF, "size": 26})],
    "Cleared stands go back to native broadleaf (oak, chestnut, konara) for wildlife and watershed, with a fast-growing kiri (paulownia) fuel crop on part of the land. Species are chosen with the NGO more trees."], size=21)
notes(s, "Core of the talk (~10 min). Keep jokes about 'planting a retirement fund' for the history bridge. "
         "Compute load (AI data center) is the anchor customer later; present as 'a small compute load next to the CHP' not as a done deal.")

# ---------------------------------------------------------------- 19 A/B/C/D
s = base("§ 03 · THE IDEA", "Only A-grade wood sells today. B, C and D are a problem we can use",
         sources="Forestry Agency grade conventions; Japanese-wood market notes")
grades = [("A", "Straight, clean, no knots", "Sawlog. The only grade worth cutting for lumber.", TERRA),
          ("B", "Slightly bent, some knots", "Sawlog or laminated; price depends on buyer.", GREEN),
          ("C", "Crooked, small", "Chips, pulp, board. Cheap.", GREEN2),
          ("D", "Branches, tops, bark", "Today: left on the slope.", GREY)]
for i, (g, h, b, c) in enumerate(grades):
    x = 0.9 + i * 4.65
    rect(s, x, 3.5, 4.3, 4.3, CARD)
    rect(s, x, 3.5, 4.3, 1.5, c)
    text(s, x + 0.25, 3.55, 1.5, 1.4, g, font=SERIF, size=64, bold=True, color=CREAM, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 1.7, 3.6, 2.5, 1.3, h, size=17, color=CREAM, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.25, 5.3, 3.85, 2.4, b, size=21)
text(s, 0.9, 8.2, 18.2, 1.8, [
    "CHP fuel and a data-center customer mean C and D wood suddenly has a buyer too. The sawlogs still fund most of the work.",
    [("Still checking: ", {"bold": True, "color": TERRA}), ("what share of Mitsue's neglected stands is really A-grade. The national average is about 61%; thinning-type stands can be near 22%.", {})]],
     size=21, after=10)
stamp(s)
notes(s, "Grade definitions here are simplified: check against the Japanese log-grading rules before presenting to forestry specialists. "
         "61% A and 22% A come from the integrated system model v1.2 (kiri_sugi_system_summary_2026-11-03.md).")

# ---------------------------------------------------------------- 20 numbers
s = base("§ 04 · THE FIRST NUMBERS", "Our first model says plus, and then shows how fragile that is",
         sources="kiri_sugi_integrated_system_model_2026-11-03.xlsx v1.2. All prices and costs are placeholders, not quotes.")
cases = [("Base case", 45), ("Owners get 0 %", 79), ("Owners get 50 %", 22), ("No residue collected", 32),
         ("Replant kiri every cut", 26), ("Thinning-type grade split", 4),
         ("317 m³/ha, 95 ha/yr", 1), ("Low price, high cost", -10)]
# drawn with shapes (not a native chart) so it renders identically everywhere and stays editable
text(s, 0.9, 3.35, 11.6, 0.4, "Steady-state system net, ¥M per year (placeholder prices)", font=MONO, size=14, color=GREY)
ZERO, SCALE, ROW = 6.9, 0.062, 0.72
for i, (lab, v) in enumerate(cases):
    y = 3.9 + i * ROW
    text(s, 0.9, y, 4.1, 0.55, lab, size=17, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    w = max(abs(v) * SCALE, 0.04)
    x = ZERO if v >= 0 else ZERO - w
    col = TERRA if v < 0 else (GREEN2 if lab == "Base case" else GREEN)
    rect(s, x, y + 0.05, w, 0.45, col)
    lx = ZERO + w + 0.1 if v >= 0 else ZERO - w - 0.9
    text(s, lx, y, 0.8, 0.55, f"{v:+d}".replace("-", "−"), size=17, bold=True,
         align=PP_ALIGN.LEFT if v >= 0 else PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
rect(s, ZERO - 0.01, 3.85, 0.03, 8 * ROW + 0.05, GREY)
dark_card(s, 12.9, 3.4, 6.2, 6.5, "Not a forecast", [
    "50 ha/yr clear-cut at 600 m³/ha, sawlogs sold, C+D chipped, half the land replanted to kiri, landowners paid 30% of sawlog net.",
    "At the village's actual standing volume (277–317 m³/ha) the base case falls to about break-even.",
    "Left out: carbon credits, data-center income, machine purchase, wages."], body_size=19)
stamp(s, "PLACEHOLDER PRICES")
notes(s, "Steady-state system net, ¥M/yr, from model v1.2. Say clearly: feasibility sizing, not a forecast. "
         "Do NOT state +45 as an expected result. Odd one out: '317 m³/ha, 95 ha/yr' = +1 (30,000 m³/yr at the village volume).")

# ---------------------------------------------------------------- 21 four drivers
s = base("§ 04 · WHAT DECIDES IT", "Four unknowns decide the answer, not the technology")
drv = [("1", "Wood per hectare", "Model uses 600 m³/ha. The village plan shows 277–317 m³/ha standing."),
       ("2", "A-grade share", "Sawlog sales fund everything. National average 61%; Mitsue may be much lower."),
       ("3", "Landowner share", "Each 10 points to owners costs about ¥11M a year. We chose 30% as an incentive."),
       ("4", "Residue price", "Placeholder ¥4,000/t. Doubling it adds only about ¥1.6M a year: minor.")]
for i, (n, h, b) in enumerate(drv):
    x = 0.9 + (i % 2) * 9.2
    y = 3.5 + (i // 2) * 3.2
    rect(s, x, y, 8.9, 2.95, CARD)
    rect(s, x, y, 0.09, 2.95, TERRA if i < 2 else GREEN)
    text(s, x + 0.3, y + 0.2, 1.0, 1.0, n, font=SERIF, size=44, bold=True, color=TERRA if i < 2 else GREEN)
    text(s, x + 1.4, y + 0.25, 7.2, 0.7, h, font=SERIF, size=26, bold=True, color=GREEN)
    text(s, x + 1.4, y + 1.0, 7.2, 1.9, b, size=21)
text(s, 0.9, 9.9, 18, 0.5, "Ordered by how much they move the result. Sources and calculations in docs/energy-forest/economics/.", font=MONO, size=13, color=GREY)
stamp(s)
notes(s, "From kiri_sugi_system_summary_2026-11-03.md section 'What drives the result'.")

# ---------------------------------------------------------------- 22 energy
s = base("§ 04 · THE ENERGY SIDE", "Start small to learn, size the real plant to the wood we can actually get",
         sources="Energy, finance and resources overview v1.1 (2026-11-03)")
card(s, 0.9, 3.5, 5.9, 5.9, "Step 1: a 50 kWe prototype", [
    "Small gasification unit in a 20 ft container. Needs about 450–600 t of dry wood a year for 24 h running.",
    "A learning step, not an economic unit: efficiency only about 12–20% at that size.",
    "Site not decided."], accent=TERRA, head_color=TERRA, body_size=21)
card(s, 7.0, 3.5, 5.9, 5.9, "Step 2: about 0.5–0.6 MWe", [
    "Our current view of the first commercial size. Efficiency 23–28% for gasifier plus engine at that scale.",
    "A 1.2 MWe plant needs about 24,000 m³ of fuel a year; we would not size for it until the harvest is proven.",
    "At 1,000 kW and above the tariff is FIP-only, and splitting is not allowed."], accent=GREEN, body_size=21)
card(s, 13.1, 3.5, 6.0, 5.9, "Three more constraints", [
    "Japanese maker only. Gasification plus engine beats steam below about 1 MWe.",
    "Grid: the local substation has about 3 MW locally and none upstream. Prior consultation drafted, not filed.",
    "Fuel may be bought from neighbouring villages too, not only from Mitsue."], accent=GREEN2, body_size=21)
stamp(s)
notes(s, "'Fuel from neighbours' is not yet in the model (needs delivered ¥/t and haul distance). "
         "Do not name a CHP maker in public: the shortlist and quotes are still in flux (one European supplier is insolvent).")

# ---------------------------------------------------------------- 23 precedents
s = base("§ 05 · NOT JUST US DREAMING", "Pieces of this already exist, in Japan and abroad",
         sources="Tenkawa Forest Power Council; Aizu (2011) Safecast blog; Buena Vista, DT/Metzler, IIJ Matsue")
prec = [("Tenkawa, next door", "A biomass council since 2016. A wood boiler heats the Dorogawa hot spring baths. Photos from our visit on 25 Aug 2026.", GREEN),
        ("Aizu, 2011", "A closed school (Akazawa Elementary) turned into a data center. A precedent for what to do with an empty school building.", GREEN2),
        ("Wood power plus compute", "Biomass-powered or biogas-powered compute has been tried: Buena Vista (US), Deutsche Telekom with Bankhaus Metzler (Germany), IIJ Matsue (Japan).", TERRA)]
for i, (h, b, c) in enumerate(prec):
    card(s, 0.9 + i * 6.15, 3.5, 5.9, 4.9, h, b, accent=c, head_color=c, body_size=23)
text(s, 0.9, 8.8, 18.2, 1.0, [[("Still checking: ", {"bold": True, "color": TERRA}), ("what exactly each of these is, and what actually transfers. Treat each as a lead, not as proof.", {})]], size=21)
stamp(s)
notes(s, "Each precedent needs one verified sentence before the talk. Tenkawa photos: from 2026-08-25 meeting (Sugimoto). "
         "Do not claim these are identical to our plan.")

# ---------------------------------------------------------------- 24 homework
s = base("§ 05 · WHAT WE DID", "The homework so far", sources="repository docs/, research/, docs/reference/")
done = [("Read the law", "45 village, prefectural and national acts on forestry, biomass, 協力隊 and siting collected and summarised."),
        ("Read the village", "Council minutes and the village newsletter archive, run through OCR; the thinning plan for 113 parcels."),
        ("Asked the makers", "Two rounds with Komatsu on steep-slope harvesting; gasification CHP makers compared; FFPRI references."),
        ("Built a model", "A spreadsheet linking clear-cut, sawlogs, chips, kiri, CHP and landowner payments. Version 1.2."),
        ("Went to the sites", "Forest visits, the village hall, the Uda City cooperative and the Tenkawa meeting."),
        ("Wrote it down", "Everything is open in a public repository, so anyone, including NAIST students, can check or challenge it.")]
for i, (h, b) in enumerate(done):
    x = 0.9 + (i % 3) * 6.15
    y = 3.5 + (i // 3) * 3.3
    card(s, x, y, 5.9, 3.05, h, b, accent=GREEN if i % 2 == 0 else GREEN2, body_size=19, head_size=23)
text(s, 0.9, 10.1, 18, 0.4, "", size=10)
notes(s, "Numbers: 45 acts (village regulations folder), 113 parcels (thinning plan). Edit this list to match what James and Kinjo-san have also done. "
         "Public repository: https://codeberg.org/YR-Design/mitsue-ai-data-center (mirror on GitHub).")

# ---------------------------------------------------------------- 25 still researching
s = base("§ 05 · WHAT WE DO NOT KNOW YET", "Honest list of open questions, and who is answering them",
         sources="docs/strategy/mitsue_energy_finance_resources_overview_2026-11-03.md section 5")
rows = [("Stand volume, stumpage, who gets the sale income", "Village hall (Oba)", "asked 6 Nov"),
        ("Slope limits with and without winch, road width, yearly output", "Komatsu", "follow-up sent"),
        ("Real CHP efficiency and cost at 0.6–0.8 MWe", "Maker quotes", "to request"),
        ("Kiri growth on Mitsue slopes", "SANSEI planting data", "asked 2 Nov"),
        ("Grid connection at 6.6 kV", "Kansai T&D", "consultation drafted"),
        ("Fuel bought in from neighbouring villages", "Uda City, others", "to approach"),
        ("What students and researchers would measure", "NAIST (you)", "to discuss")]
y = 3.45
rect(s, 0.9, y, 18.2, 0.55, GREEN)
for xx, w, t in [(1.1, 10, "OPEN QUESTION"), (11.6, 4.0, "WHO"), (15.7, 3.3, "STATUS")]:
    text(s, xx, y + 0.05, w, 0.45, t, font=MONO, size=14, bold=True, color=CREAM)
y += 0.6
for i, (q, w, st) in enumerate(rows):
    rect(s, 0.9, y, 18.2, 0.75, CARD if i % 2 == 0 else CREAM)
    text(s, 1.1, y + 0.03, 10.2, 0.8, q, size=19, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 11.6, y + 0.03, 4.0, 0.8, w, size=18, color=GREEN, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 15.7, y + 0.03, 3.3, 0.8, st, font=MONO, size=14, color=TERRA, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.8
stamp(s)
notes(s, "Refresh this table right before the talk: statuses change weekly. The last row is the real ask to NAIST.")

# ---------------------------------------------------------------- 26 status honesty
s = base("§ 05 · WHERE WE STAND", "Early planning. No money raised, no contracts, no machines bought")
tl = [("NOW", "Phase 0", "Trust, sites, fuel talks, homework", TERRA),
      ("DEC 2026", "Phase 0 ends", "Decision on first site and partners", GREEN),
      ("2027", "Prototype", "50 kWe CHP and fuel trial, if site and partners are settled", GREEN),
      ("2028 →", "Machines", "A CTL trial, if a fit is shown and financing is in place", GREEN),
      ("LATER", "Full scale", "About 0.5–1.2 MWe and a larger compute load; no fixed date", GREEN2)]
rect(s, 1.4, 5.0, 17.2, 0.07, GREEN)
for i, (when, h, b, c) in enumerate(tl):
    x = 1.0 + i * 3.7
    o = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.3), Inches(4.7), Inches(0.65), Inches(0.65))
    o.fill.solid(); o.fill.fore_color.rgb = c; o.line.fill.background(); o.shadow.inherit = False
    text(s, x, 3.6, 3.5, 0.5, when, font=MONO, size=16, bold=True, color=c)
    text(s, x, 5.6, 3.4, 0.8, h, font=SERIF, size=24, bold=True, color=GREEN)
    text(s, x, 6.4, 3.4, 2.2, b, size=19)
rect(s, 0.9, 8.9, 18.2, 1.1, CARD)
rect(s, 0.9, 8.9, 0.09, 1.1, TERRA)
text(s, 1.3, 8.95, 17.5, 1.0, "Status: ¥0 committed. Dates are targets, not promises. The grant tracks we know of (METI GX regional, MoE zero-emission data center) are being studied, not applied for.",
     size=20, anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Align the dates with the current phase plan (Phase 0 extended to Dec 2026, later phases shifted 3 months). "
         "Never imply contracts exist: the outreach rule is no overstatement.")

# ---------------------------------------------------------------- 27 slogan
s = base("§ 06 · THE LONG VIEW", "", dark=True)
text(s, 1.5, 3.4, 17, 2.4, "75 years to grow the forest.", font=SERIF, size=64, bold=True, color=CREAM)
text(s, 1.5, 5.6, 17, 2.4, "25 years to grow the village.", font=SERIF, size=64, bold=True, color=TERRA)
text(s, 1.5, 8.2, 16, 1.4, "A hundred-year plan in the old Goryōrin spirit: planting for the people who will be here when the trees are ready.",
     size=24, color=CREAM)
notes(s, "Closing image: the young sprout and the full-grown tree. If Kinjo agrees to the green / grey dress-code idea, call back to it here.")

# ---------------------------------------------------------------- 28 Q&A
s = base("§ 07 · Q&A", "Tell us where we are wrong", dark=True)
text(s, 1.5, 3.4, 17, 2.4, ["Honest critique is more useful to us than polite interest.",
                            "What would you measure? What would you doubt? Who else should we ask?"],
     size=28, color=CREAM, after=18)
rect(s, 1.5, 6.9, 17, 0.06, TERRA)
text(s, 1.5, 7.2, 17, 2.6, ["Rob Oudendijk · Mitsue-it · rob@mitsue.it",
                            "All documents open: https://codeberg.org/YR-Design/mitsue-ai-data-center",
                            "Website: mitsue.it"], font=MONO, size=18, color=CARD, after=10)
notes(s, "Q&A ~5 min. Check the signature block against docs/outreach/email_signature_standard.md. Add Kinjo and James contact lines only if they agree.")

# ---------------------------------------------------------------- page numbers
total = len(prs.slides)
for idx, tb in enumerate(pagers, 1):  # one pager per slide, in slide order
    r = tb.text_frame.paragraphs[0].add_run()
    r.text = f"{idx:02d} / {total:02d}"
    r.font.name, r.font.size = MONO, Pt(13)
    r.font.color.rgb = CARD if idx in (1, total - 1, total) else GREY

prs.core_properties.title = f"Mitsue NAIST Seminar v{VERSION}"
prs.core_properties.author = "Mitsue-it"
prs.save(OUT)
print("saved", os.path.abspath(OUT), total, "slides")
