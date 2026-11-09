#!/usr/bin/env python3
"""NAIST 13 Jan 2027 seminar deck, v0.3 (python-pptx).

Look: same as mitsue.it (cream paper, deep green, clay accent; Cormorant Garamond
headlines with italic emphasis, IBM Plex Sans body, IBM Plex Mono labels, Noto Serif JP).
Install those Google Fonts on the machine that opens the deck, or PowerPoint will fall back.
Run:  python3 build_deck_v03.py   ->  ../Mitsue_NAIST_Seminar_v0.3.pptx
"""
import os
from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.oxml.ns import qn

VERSION, DATE = "0.3", "2026-11-09"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", f"Mitsue_NAIST_Seminar_v{VERSION}.pptx")
IMG = lambda n: os.path.join(HERE, "img", n)
ILLUS = os.path.join(HERE, "title_illustration.png")

# website palette (style.css of mitsue-v2; oklch converted)
BG = RGBColor(0xF5, 0xF1, 0xEA)
BG2 = RGBColor(0xEF, 0xEA, 0xE0)
PAPER = RGBColor(0xFB, 0xF8, 0xF1)
INK = RGBColor(0x1C, 0x1C, 0x1A)
SOFT = RGBColor(0x3A, 0x3A, 0x36)
MUTE = RGBColor(0x6C, 0x6A, 0x62)
RULE = RGBColor(0xD8, 0xD2, 0xC5)
ACC = RGBColor(0x39, 0x55, 0x3F)
DEEP = RGBColor(0x1F, 0x34, 0x23)
CLAY = RGBColor(0x9D, 0x6F, 0x48)
SUN = RGBColor(0xC4, 0x66, 0x3A)   # illustration sun only
LEAF = RGBColor(0x6F, 0x8F, 0x6A)  # light green for graphics
SERIF, SANS, MONO, JP = "Cormorant Garamond", "IBM Plex Sans", "IBM Plex Mono", "Noto Serif JP"

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(18288000), Emu(10287000)
BLANK = prs.slide_layouts[6]
pagers = []


# ------------------------------------------------------------ primitives
def _strip_style(sh):
    st = sh._element.find(qn("p:style"))
    if st is not None:
        sh._element.remove(st)


def alpha(sh, a):
    for c in sh._element.spPr.iter(qn("a:srgbClr")):
        e = etree.SubElement(c, qn("a:alpha"))
        e.set("val", str(int(a * 100000)))
        break


def shape(s, kind, x, y, w, h, fill=None, line=None, lw=1.0, a=None):
    r = s.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    _strip_style(r)
    if fill is None:
        r.fill.background()
    else:
        r.fill.solid()
        r.fill.fore_color.rgb = fill
        if a is not None:
            alpha(r, a)
    if line is None:
        r.line.fill.background()
    else:
        r.line.color.rgb = line
        r.line.width = Pt(lw)
    return r


def rect(s, x, y, w, h, fill=None, line=None, lw=1.0, a=None):
    return shape(s, MSO_SHAPE.RECTANGLE, x, y, w, h, fill, line, lw, a)


def oval(s, x, y, w, h, fill=None, line=None, lw=1.0, a=None):
    return shape(s, MSO_SHAPE.OVAL, x, y, w, h, fill, line, lw, a)


def tri(s, x, y, w, h, fill, a=None):
    return shape(s, MSO_SHAPE.ISOSCELES_TRIANGLE, x, y, w, h, fill, None, 1, a)


def line(s, x1, y1, x2, y2, color=RULE, lw=1.0, arrow=False, dash=False):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    _strip_style(c)
    c.line.color.rgb = color
    c.line.width = Pt(lw)
    ln = c.line._get_or_add_ln()
    if dash:
        d = etree.SubElement(ln, qn("a:prstDash"))
        d.set("val", "dash")
    if arrow:
        t = etree.SubElement(ln, qn("a:tailEnd"))
        t.set("type", "triangle")
    return c


def poly(s, pts, fill=None, line_c=None, lw=2.0, close=False, a=None):
    E = lambda v: int(v * 914400)
    fb = s.shapes.build_freeform(E(pts[0][0]), E(pts[0][1]))
    fb.add_line_segments([(E(px), E(py)) for px, py in pts[1:]], close=close)
    sh = fb.convert_to_shape()
    _strip_style(sh)
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
        if a is not None:
            alpha(sh, a)
    if line_c is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line_c
        sh.line.width = Pt(lw)
    return sh


def R(t, **o):
    return (t, o)


def text(s, x, y, w, h, paras, font=SANS, size=20, color=INK, bold=False, italic=False,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, spacing=1.12, after=6):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.04)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    if isinstance(paras, str):
        paras = paras.split("\n")
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment, p.line_spacing, p.space_after = align, spacing, Pt(after)
        for t, o in ([(para, {})] if isinstance(para, str) else para):
            r = p.add_run()
            r.text = t
            f = r.font
            f.name = o.get("font", font)
            f.size = Pt(o.get("size", size))
            f.bold = o.get("bold", bold)
            f.italic = o.get("italic", italic)
            f.color.rgb = o.get("color", color)
    return tb


def headline(s, parts, x=0.9, y=1.55, w=17.5, size=54, color=INK, em=DEEP, h=2.2):
    """parts: list of (text, is_emphasis). Emphasis = italic, deep green (as on the website)."""
    runs = [R(t, italic=bool(e), color=(em if e else color)) for t, e in parts]
    return text(s, x, y, w, h, [runs], font=SERIF, size=size, spacing=0.95)


def eyebrow(s, label, x=0.9, y=1.2, color=ACC):
    line(s, x, y + 0.17, x + 0.6, y + 0.17, color, 1.0)
    text(s, x + 0.75, y, 14, 0.35, label, font=MONO, size=12, color=color)


def tag(s, label, x=15.7, w=3.4, y=1.12):
    b = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, 0.42, None, CLAY, 1.25)
    tf = b.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.05)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = label
    r.font.name, r.font.size, r.font.bold = MONO, Pt(11), True
    r.font.color.rgb = CLAY


def photo(s, path, x, y, w, h, fx=0.5, fy=0.5):
    iw, ih = Image.open(path).size
    pic = s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))
    box, img = w / h, iw / ih
    if img > box:  # crop sides
        keep = box / img
        l = (1 - keep) * fx
        pic.crop_left, pic.crop_right = l, 1 - keep - l
    else:
        keep = img / box
        t = (1 - keep) * fy
        pic.crop_top, pic.crop_bottom = t, 1 - keep - t
    return pic


def notes(s, body):
    s.notes_slide.notes_text_frame.text = body


def slide(section=None, title=None, dark=False, src=None, mark=None, tagline=None, title_size=54, title_h=2.2):
    s = prs.slides.add_slide(BLANK)
    rect(s, 0, 0, 20, 11.25, DEEP if dark else BG)
    fg, mu = (BG, RULE) if dark else (INK, MUTE)
    oval(s, 0.9, 0.42, 0.13, 0.13, BG if dark else ACC)
    text(s, 1.15, 0.33, 9, 0.35, "PHASE 0 · MITSUE VILLAGE · NARA PREFECTURE", font=MONO, size=11, color=mu)
    text(s, 10.0, 0.33, 9.1, 0.35, f"NAIST SEMINAR · 13 JAN 2027 · v{VERSION} DRAFT · WORK IN PROGRESS",
         font=MONO, size=11, color=mu, align=PP_ALIGN.RIGHT)
    line(s, 0.9, 0.85, 19.1, 0.85, RULE if not dark else ACC, 0.75)
    pg = text(s, 16.3, 10.62, 2.8, 0.35, "", font=MONO, size=11, color=mu, align=PP_ALIGN.RIGHT)
    pagers.append((pg, dark))
    text(s, 0.9, 10.62, 8, 0.35, [[R("御 ", font=JP, size=14, color=fg), R("Mitsue Project", font=SERIF, size=15, color=fg)]])
    if section:
        eyebrow(s, section, color=(RULE if dark else ACC))
    if title:
        headline(s, title, size=title_size, h=title_h, color=(BG if dark else INK), em=(RULE if dark else DEEP))
    if tagline:
        tag(s, tagline)
    if src:
        text(s, 0.9, 10.25, 18, 0.35, "Sources: " + src, font=MONO, size=10, color=mu)
    return s


def history(n, era, title, tagtxt="JAMES · TO EXPAND"):
    return slide(f"HISTORY {n:02d} / 10 · {era}", title, tagline=tagtxt, title_size=50, title_h=1.9)


def stat(s, x, y, big, small, w=4.2, color=DEEP, size=58):
    line(s, x, y, x + w, y, RULE, 0.75)
    text(s, x, y + 0.15, w, 1.0, big, font=SERIF, size=size, color=color)
    text(s, x, y + 1.2, w, 1.0, small, size=16, color=MUTE, spacing=1.05)


def tree(s, x, base, h, color=ACC, kind="cone"):
    """Tree standing on y=base, centre x, total height h."""
    tw = max(h * 0.07, 0.04)
    rect(s, x - tw / 2, base - h * 0.2, tw, h * 0.2, CLAY)
    if kind == "cone":
        tri(s, x - h * 0.18, base - h, h * 0.36, h * 0.85, color)
    else:
        oval(s, x - h * 0.3, base - h, h * 0.6, h * 0.62, color)


def pull(s, x, y, w, txt, color=CLAY, size=24):
    """Pull-quote with clay bar, website style."""
    rect(s, x, y, 0.06, 1.1, color)
    text(s, x + 0.25, y - 0.02, w - 0.3, 1.5, txt, font=SERIF, size=size, italic=True, color=SOFT, spacing=1.05)


# ============================================================ 1 TITLE
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, 20, 11.25, BG)
photo(s, IMG("sugi_rice_field.jpg"), 10.6, 0, 9.4, 11.25, fx=0.25)
rect(s, 0.9, 0.55, 0.62, 0.62, None, INK, 1.0)
text(s, 0.9, 0.55, 0.62, 0.62, "御", font=JP, size=24, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
text(s, 1.7, 0.55, 5, 0.4, "Mitsue Project", font=SERIF, size=22)
text(s, 1.7, 0.92, 5, 0.3, "御杖プロジェクト", font=JP, size=11, color=MUTE)
eyebrow(s, "NAIST SEMINAR · 13 JANUARY 2027", y=2.4)
headline(s, [("Planted for a market that ", 0), ("no longer exists.", 1)], y=3.0, w=9.4, size=76, h=4.2)
text(s, 0.9, 7.35, 9, 0.7, "いまは無い市場のために植えられた森", font=JP, size=20, color=MUTE)
text(s, 0.9, 8.1, 9, 1.4, "A forest, a village, and a sideways idea: history, today, and what we are still working out.",
     size=19, color=SOFT, spacing=1.2)
line(s, 0.9, 9.7, 10.0, 9.7, RULE, 0.75)
text(s, 0.9, 9.85, 9.5, 0.4, "JAMES HILL  ·  ROB OUDENDIJK", font=MONO, size=12, color=ACC)
text(s, 0.9, 10.22, 9.5, 0.4, f"v{VERSION} DRAFT · {DATE} · WORK IN PROGRESS", font=MONO, size=11, color=MUTE)
pagers.append((text(s, 8.0, 10.22, 2.2, 0.4, "", font=MONO, size=11, color=MUTE, align=PP_ALIGN.RIGHT), False))
notes(s, "Working title. Hook: the sugi standing in Mitsue today were planted for a timber and firewood economy that "
         "fossil fuels had begun dismantling by 1950. Photo: sugi above rice paddies (from the project funding deck).")

# ============================================================ 2 TWO PEOPLE
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, 20, 11.25, BG)
rect(s, 0, 0, 7.4, 11.25, DEEP)
text(s, 0.9, 0.4, 6, 0.35, "NAIST SEMINAR · 13 JAN 2027", font=MONO, size=11, color=RULE)
eyebrow(s, "WHO IS TALKING", y=1.2, color=RULE)
headline(s, [("Two people, ", 0), ("one forest.", 1)], y=1.7, w=6.2, size=60, color=BG, em=RULE, h=3.4)
s.shapes.add_picture(ILLUS, Inches(0.5), Inches(6.2), Inches(6.4), Inches(5.69 * 0.95))
for i, (nm, role, body) in enumerate([
    ("James Hill", "FOREST HISTORY · OPENS THE TALK",
     "Takes us from the Tokugawa to 1958: how Japan came to plant this much sugi, and why it made sense at the time."),
    ("Rob Oudendijk", "MITSUE-IT · THE REST OF THE TALK",
     "Dutch engineer. Built his own house in the Mitsue forest, so the trees are 3 m from the front door. "
     "If the talk goes badly, blame the neighbours.")]):
    y = 1.7 + i * 4.3
    line(s, 8.3, y, 19.1, y, RULE, 0.75)
    text(s, 8.3, y + 0.2, 10.8, 1.2, nm, font=SERIF, size=60, italic=True, color=DEEP)
    text(s, 8.3, y + 1.45, 10.8, 0.4, role, font=MONO, size=12, color=CLAY)
    text(s, 8.3, y + 1.95, 10.2, 1.8, body, size=20, color=SOFT, spacing=1.2)
pagers.append((text(s, 16.3, 10.62, 2.8, 0.35, "", font=MONO, size=11, color=MUTE, align=PP_ALIGN.RIGHT), False))
notes(s, "Kinjo Rie (Mitsue Kanko) is NOT presenting (decided 2026-11-09). If she attends, thank her from the floor; "
         "do not put words in her mouth. Check James's own bio line with him.")

# ============================================================ 3 AGENDA PATH
s = slide("THE PLAN FOR 40 MINUTES", [("Forty minutes, ", 0), ("five stops.", 1)])
stops = [("1", "History", "How Japan came to plant\nso much sugi", "JAMES · ~10 MIN"),
         ("2", "Today", "The village and forest\nas they are now", "ROB · ~5 MIN"),
         ("3", "The problem", "Three problems with\none shape", "ROB · ~5 MIN"),
         ("4", "The idea", "Pull, don't push:\nwood, power, replanting", "ROB · ~10 MIN"),
         ("5", "Homework", "What we checked and\nwhat we do not know", "ROB · ~5 MIN + Q&A")]
line(s, 1.5, 6.6, 18.5, 6.6, ACC, 2.0)
for i, (n, h, b, who) in enumerate(stops):
    cx = 2.5 + i * 3.75
    up = (i % 2 == 0)
    oval(s, cx - 0.42, 6.18, 0.84, 0.84, DEEP if i != 3 else CLAY)
    text(s, cx - 0.42, 6.18, 0.84, 0.84, n, font=SERIF, size=28, color=BG, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    ty = 3.7 if up else 7.3
    line(s, cx, ty + 2.3 if up else 7.02, cx, 6.18 if up else ty, RULE, 1.0)
    text(s, cx - 1.75, ty - (0.0 if up else 0.0) + (0 if up else 0.4), 3.5, 0.7, h, font=SERIF, size=34, italic=True, color=DEEP, align=PP_ALIGN.CENTER)
    text(s, cx - 1.75, ty + 0.75 + (0 if up else 0.4), 3.5, 1.0, b, size=15, color=SOFT, align=PP_ALIGN.CENTER, spacing=1.1)
    text(s, cx - 1.75, ty + 1.65 + (0 if up else 0.4), 3.5, 0.4, who, font=MONO, size=11, color=CLAY, align=PP_ALIGN.CENTER)
text(s, 0.9, 9.8, 18, 0.5, "Tone: light, not academic. Big scary problems sometimes have weirdly simple solutions, if you look at them sideways.",
     font=SERIF, size=22, italic=True, color=MUTE)
notes(s, "Two presenters only (James and Rob). Time boxes: history 10, today 5, problem 5, idea 10, homework 5, Q&A 5. "
         "See docs/meetings/naist_2027-01-13_presentation_draft.md.")

# ============================================================ HISTORY 1: strip
s = history(1, "1603–1958 · THE WHOLE STORY IN ONE STRIP", [("Three centuries, ", 0), ("one strip.", 1)])
X0, X1, Y0 = 1.2, 18.8, 7.05
sc = (X1 - X0) / (1960 - 1600)
xy = lambda yr: X0 + (yr - 1600) * sc
bands = [(1603, 1867, "TOKUGAWA", BG2, MUTE), (1868, 1947, "MEIJI → WAR", RGBColor(0xE3, 0xE8, 0xDC), ACC),
         (1948, 1960, "POSTWAR", RGBColor(0xD6, 0xE0, 0xD0), DEEP)]
for a_, b_, lab, col, tc in bands:
    rect(s, xy(a_), Y0 - 0.32, xy(b_) - xy(a_), 0.64, col)
    if xy(b_) - xy(a_) > 2.0:
        text(s, xy(a_) + 0.1, Y0 - 0.18, xy(b_) - xy(a_) - 0.2, 0.4, lab, font=MONO, size=11, color=tc)
rect(s, xy(1929), Y0 + 0.32, xy(1949) - xy(1929), 0.18, CLAY)
text(s, xy(1929) - 1.1, Y0 + 0.55, 3.2, 0.35, "CUTOVER CRISIS 1929–49", font=MONO, size=10, color=CLAY)
for yr in range(1600, 1961, 50):
    line(s, xy(yr), Y0 - 0.32, xy(yr), Y0 - 0.45, MUTE, 0.75)
    text(s, xy(yr) - 0.4, Y0 + 0.9 if yr not in (1950, 1600) else Y0 + 0.9, 0.8, 0.3, str(yr), font=MONO, size=10, color=MUTE, align=PP_ALIGN.CENTER)
ev = [(1665, "1665 Kiso cuts halved", 1, "l"), (1724, "1724 Kiso: cut down >60%", 2, "l"), (1849, "1849 Yoshino method", 1, "l"),
      (1868, "1868 Meiji: land ownership", 2, "l"), (1889, "1889 Goryōrin founded", 1, "l")]
levels = {1: 5.95, 2: 4.95, 3: 3.75}
for yr, lab, lv, _ in ev:
    yy = levels[lv]
    line(s, xy(yr), yy + 0.55, xy(yr), Y0 - 0.32, RULE, 0.75)
    oval(s, xy(yr) - 0.07, Y0 - 0.07, 0.14, 0.14, DEEP)
    text(s, xy(yr) - 0.05, yy, 2.3, 0.6, lab, font=SANS, size=13, color=INK, spacing=1.0)
for yr in (1951, 1955, 1958):
    line(s, xy(yr), 4.7, xy(yr), Y0 - 0.32, RULE, 0.75)
    oval(s, xy(yr) - 0.07, Y0 - 0.07, 0.14, 0.14, CLAY if yr == 1958 else DEEP)
text(s, 15.4, 3.7, 3.7, 1.2, ["1951 planting compulsory", "1955 the biggest boom", "1958  ★ the hinge"], size=13, color=INK, align=PP_ALIGN.RIGHT, spacing=1.0, after=2)
text(s, 0.9, 9.4, 18, 0.7, [[R("The punchline arrives in 1958: ", font=SERIF, size=26, italic=True, color=DEEP),
                            R("the trees we see today were planted just as the demand behind them began to fade.", font=SERIF, size=26, color=SOFT)]])
notes(s, "Overview strip. James: restructure freely. Dates from docs/energy-forest/history/naist_timeline_history_to_1958.md.")

# ============================================================ HISTORY 2: tenure
s = history(2, "1603–1867 · TOKUGAWA TENURE", [("Who owns a tree on shared land? ", 0), ("The question that made plantations possible.", 1)])
text(s, 0.9, 4.2, 7.6, 4.8, [
    [R("Land is feudal or communal. ", bold=True), R("Private ownership is banned in principle; lords' forests in Kiso are guarded and theft is severely punished.")],
    [R("1665 and 1724. ", bold=True), R("Kiso cuts halved, then cut down by more than 60% and held for 30 years.")],
    [R("Late 1600s: wave 1. ", bold=True), R("Edo and Osaka boom; a 50-year timber investment pays for the first time.")],
    [R("1801. ", bold=True), R("Edo has about 1,000,000 people, bigger than London or Paris. With imports shut out, all demand falls on domestic forests.")]],
     size=17, color=SOFT, after=11, spacing=1.12)
# hillside illustration
tri(s, 9.0, 3.9, 10.0, 5.6, ACC)
tri(s, 12.4, 4.7, 7.2, 4.8, DEEP)
rect(s, 9.0, 9.4, 10.0, 0.1, CLAY)
for tx, th, kind in [(10.3, 1.2, "cone"), (11.2, 1.0, "cone"), (15.0, 1.4, "cone"), (16.0, 1.2, "cone"), (17.3, 1.0, "cone")]:
    tree(s, tx, 9.4, th, LEAF if tx < 13 else BG2, kind)
text(s, 13.0, 3.45, 3.6, 0.5, "LORD'S FOREST · guarded", font=MONO, size=10, color=MUTE)
text(s, 9.0, 9.6, 4.6, 0.4, "VILLAGE COMMONS · fuel, fodder", font=MONO, size=10, color=MUTE)
rect(s, 14.2, 5.7, 4.3, 1.35, PAPER, CLAY, 1.0)
text(s, 14.3, 5.78, 4.1, 1.2, "Plant a tree on land you do not own: who gets the timber in 50 years?", font=SERIF, size=19, italic=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Sources: Iwamoto; Totman, Green Archipelago. The answer worked out in Yoshino and Owase (private ownership of planted trees on communal "
         "land) is the same question behind Mitsue's private woodlots today.")

# ============================================================ HISTORY 3: Yoshino method
s = history(3, "1849 · THE YOSHINO METHOD", [("Plant dense, thin early, ", 0), ("thin again.", 1)])
panels = [("PLANT", "at 3 ft spacing", 14, 0.55, 1.5), ("THIN", "when butt reaches 2–3 in.", 8, 0.9, 2.2),
          ("RE-THIN", "5 years later", 5, 1.3, 3.0), ("FINAL", "12 ft spacing, grow on", 3, 1.8, 3.9)]
for i, (h, sub, n, th, _) in enumerate(panels):
    x = 0.9 + i * 4.62
    rect(s, x, 4.0, 4.4, 4.6, PAPER, RULE, 0.75)
    rect(s, x, 7.7, 4.4, 0.9, BG2)
    for k in range(n):
        tx = x + 0.4 + (3.6 / max(n - 1, 1)) * k if n > 1 else x + 2.2
        tree(s, tx, 7.7, th * 1.55, ACC if i < 3 else DEEP)
    text(s, x + 0.25, 8.0, 4.0, 0.5, h, font=MONO, size=14, color=CLAY, bold=True)
    text(s, x + 0.25, 8.33, 4.0, 0.4, sub, size=14, color=SOFT)
    if i < 3:
        text(s, x + 4.3, 5.6, 0.4, 0.6, "›", font=SERIF, size=34, color=CLAY)
text(s, 0.9, 9.0, 12, 0.9, [[R("Okino Takao, Kurobane domain, 1849 ", font=MONO, size=12, color=MUTE),
                            R("a citable Edo-era schedule that still looks familiar.", font=SERIF, size=22, italic=True, color=SOFT)]])
text(s, 13.2, 9.0, 5.9, 1.0, "Also: 1750s Yamaguni guild licence class for plantation growers; 1779 first Kiso forest inventory.", size=13, color=MUTE)
notes(s, "Source: Totman. The thinning rules are old. What is new is that nobody is there to do the thinning. Good hook for 'Today'. "
         "Tree drawings are schematic, not to scale.")

# ============================================================ HISTORY 4: Kan/Min
s = history(4, "1868–1889 · KAN / MIN", [("Government or private? ", 0), ("Six policy reversals in five years.", 1)])
for i, (yr, pct, col) in enumerate([("1880", 31, MUTE), ("1889", 53, DEEP)]):
    y = 4.3 + i * 1.9
    text(s, 0.9, y, 1.6, 0.8, yr, font=SERIF, size=40, color=col)
    rect(s, 2.6, y + 0.1, 10.0, 0.9, BG2, RULE, 0.75)
    rect(s, 2.6, y + 0.1, 10.0 * pct / 100, 0.9, col)
    text(s, 2.7 + 10.0 * pct / 100, y + 0.02, 2.2, 1.0, f"{pct}%", font=SERIF, size=46, color=col, anchor=MSO_ANCHOR.MIDDLE)
text(s, 2.6, 8.1, 10, 0.7, "share of Japan's woodland held by the government", font=MONO, size=12, color=MUTE)
text(s, 2.6, 8.55, 10.2, 1.4, "1868 formal ownership introduced; national forests carved from communal and former feudal land. "
                              "1871–76 the state tries to sort all woodland into kan or min.", size=15, color=SOFT)
for i, (jp, en, col, sub) in enumerate([("官有地 kan'yuchi", "government", DEEP, "the state wants sanrin: dense conifer"),
                                         ("民有地 min'yuchi", "private", ACC, "villagers need gen'ya: scrub for fuel and fodder"),
                                         ("共有地 koyuchi", "shared use", CLAY, "a third category, because the first two did not fit real life")]):
    y = 4.2 + i * 1.75
    rect(s, 13.6, y, 5.5, 1.55, PAPER, RULE, 0.75)
    rect(s, 13.6, y, 0.12, 1.55, col)
    text(s, 13.95, y + 0.1, 5.0, 0.5, jp, font=JP, size=17, color=col, bold=True)
    text(s, 13.95, y + 0.55, 5.0, 0.9, [[R(en + ". ", bold=True), R(sub)]], size=14, color=SOFT, spacing=1.05)
notes(s, "Source: Totman. Worth a joke: six policy reversals in five years is a pace nobody would call planning. "
         "Same tension in a Japanese village today: what the state wants from the forest is not what the village needs.")

# ============================================================ HISTORY 5: Goryorin
s = history(5, "1889–1947 · GORYŌRIN", [("For 58 years, forestry was a ", 0), ("real business.", 1)])
stat(s, 0.9, 4.2, "1.6 M ha", "carved out in 1889–90 as the Imperial Household's own income-producing forest estate", w=4.0)
stat(s, 5.3, 4.2, "40 %", "net margin on gross income at the 1936–45 peak, against 23% for the much larger National Forest", w=4.0)
# margin bars
rect(s, 5.3, 7.0, 4.0 * 0.40 * 2.2, 0.38, DEEP)
rect(s, 5.3, 7.5, 4.0 * 0.23 * 2.2, 0.38, MUTE)
text(s, 5.3 + 4.0 * 0.4 * 2.2 + 0.1, 6.95, 1.6, 0.4, "Goryōrin", size=13, color=DEEP)
text(s, 5.3 + 4.0 * 0.23 * 2.2 + 0.1, 7.45, 2.5, 0.4, "National Forest", size=13, color=MUTE)
stat(s, 9.7, 4.2, "31 %", "of Imperial Household income in 1940 (19% in 1916)", w=4.0)
stat(s, 14.1, 4.2, "70 %", "of Household wealth by 1946: ¥2.6 bn of cumulative asset value", w=5.0)
# life line
line(s, 1.2, 9.3, 18.8, 9.3, ACC, 2.0)
for yr, lab, x_, col in [(1889, "founded", 1.2, DEEP), (1892, "turns profitable", 3.0, DEEP), (1942, "Hundred Year Plan suspended,\n'special harvesting'", 12.4, CLAY), (1947, "dissolved", 18.3, MUTE)]:
    oval(s, x_ - 0.09, 9.21, 0.18, 0.18, col)
    last_ = (yr == 1947)
    text(s, (x_ - 3.5) if last_ else (x_ - 0.1), 9.45, 3.6, 0.7, [[R(str(yr) + "  ", font=MONO, size=11, color=col, bold=True), R(lab, size=12, color=SOFT)]],
         spacing=1.0, align=PP_ALIGN.RIGHT if last_ else PP_ALIGN.LEFT)
notes(s, "Source: Totman, Goryōrin and lumber industry notes. Managed Japanese forestry was, for decades, a real bankable asset and "
         "not a subsidised cost. Our slogan 'Grow the Forest. Grow the Village.' comes from a hundred-year plan like this.")

# ============================================================ HISTORY 6: cutover
s = history(6, "1929–1949 · THE CUTOVER CRISIS", [("Twenty years in a row, more was cut ", 0), ("than planted.", 1)])
GX0, GX1, GY0, GY1 = 1.3, 12.4, 9.3, 4.2
rect(s, GX0 - 0.2, GY1 - 0.2, GX1 - GX0 + 0.5, GY0 - GY1 + 0.6, PAPER, RULE, 0.75)
cut = [(1.5, 8.2), (3.5, 7.8), (5.5, 7.0), (7.0, 6.0), (8.4, 5.1), (9.5, 4.7), (10.6, 5.0), (11.6, 7.3)]
plant = [(1.5, 8.6), (3.5, 8.5), (5.5, 8.4), (7.0, 8.4), (8.4, 8.3), (9.5, 8.3), (10.6, 8.3), (11.6, 8.4)]
poly(s, cut + plant[::-1], fill=CLAY, close=True, a=0.28)
poly(s, cut, line_c=CLAY, lw=3.0)
poly(s, plant, line_c=DEEP, lw=3.0)
text(s, 2.3, 4.55, 4.5, 0.7, "area cut", font=SERIF, size=26, italic=True, color=CLAY)
text(s, 2.3, 8.7, 4.5, 0.7, "area planted", font=SERIF, size=26, italic=True, color=DEEP)
text(s, 8.0, 6.4, 3.2, 0.8, "gap peaks in the\nmid-1940s", font=MONO, size=11, color=CLAY)
text(s, 1.4, 9.4, 11, 0.5, "1929 ········································ 1949   SCHEMATIC, NOT DATA (James to replace)", font=MONO, size=10, color=MUTE)
stat(s, 13.4, 4.2, "1.49 M ha", "cutover land in 1948, about 6% of Japan's forest area, concentrated near villages", w=5.7, size=52)
stat(s, 13.4, 6.65, "8.6 → 10.97", "million koku harvested, 1942 to 1944: paid for by cutting reforestation and aftercare", w=5.7, size=46)
text(s, 13.4, 9.1, 5.7, 1.0, "1948 forecast: wood exhausted in 15–33 years. Wrong, but it drove everything after.", font=SERIF, size=19, italic=True, color=SOFT, spacing=1.0)
notes(s, "Source: Matsushita (2015). The curves are a SCHEMATIC of the stated facts (cut area exceeds planted area every year 1929–49, gap peaks mid-1940s); "
         "replace with the real Forestry Agency series.")

# ============================================================ HISTORY 7: postwar plans
s = history(7, "1949–1961 · POSTWAR PLANS", [("Three plans in twelve years, ", 0), ("and planting becomes the law.", 1)])
PX0, PX1 = 3.2, 18.6
py_ = lambda yr: PX0 + (yr - 1949) * (PX1 - PX0) / 12
for yr in range(1949, 1962):
    line(s, py_(yr), 4.2, py_(yr), 8.7, RULE, 0.5)
    text(s, py_(yr) - 0.4, 8.75, 0.8, 0.3, str(yr), font=MONO, size=10, color=MUTE, align=PP_ALIGN.CENTER)
for i, (nm, a_, b_, col, d) in enumerate([("5-Year Plan", 1949, 1953, DEEP, "1.5 M ha cutover; 60–70% executed"),
                                           ("10-Year Plan", 1952, 1961, ACC, "self-sufficiency via broadleaf → conifer"),
                                           ("6-Year Plan", 1955, 1960, CLAY, "quality: nursery stock, seed trees")]):
    y = 4.45 + i * 1.2
    text(s, 0.9, y + 0.05, 2.2, 0.8, nm, font=SERIF, size=24, italic=True, color=col)
    rect(s, py_(a_), y, py_(b_) - py_(a_), 0.8, col)
    text(s, py_(a_) + 0.15, y + 0.12, py_(b_) - py_(a_) - 0.3, 0.6, d, size=13, color=BG, anchor=MSO_ANCHOR.MIDDLE)
oval(s, py_(1951) - 0.14, 8.2, 0.28, 0.28, SUN)
line(s, py_(1951), 8.2, py_(1951), 4.2, SUN, 1.5, dash=True)
text(s, py_(1951) + 0.2, 7.95, 7.5, 0.6, [[R("1951  ", font=MONO, size=12, color=SUN, bold=True), R("planting compulsory (Art. 14); log import tariffs cut to near zero", size=14, color=INK)]])
text(s, 0.9, 9.3, 18, 0.8, [[R("A tidy irony: ", font=SERIF, size=24, italic=True, color=DEEP),
                            R("broadleaf-to-conifer conversion is what we now want to undo, where it makes sense.", font=SERIF, size=24, color=SOFT)]])
notes(s, "Source: Matsushita (2015). The irony line is Rob's addition; James to check it holds for the Nara region.")

# ============================================================ HISTORY 8: two curves
s = history(8, "1950–1955 · TWO CURVES CROSS", [("Planting peaks. ", 0), ("The reason for planting fades.", 1)])
rect(s, 0.9, 4.1, 12.6, 5.4, PAPER, RULE, 0.75)
planted = [(1.5, 8.7), (3.2, 8.0), (5.0, 6.6), (6.5, 5.1), (7.4, 4.55), (9.5, 4.5), (11.5, 4.7), (13.0, 5.0)]
demand = [(1.5, 4.6), (3.2, 4.7), (5.0, 5.2), (6.5, 6.2), (7.4, 6.7), (9.5, 7.8), (11.5, 8.6), (13.0, 9.0)]
poly(s, planted, line_c=DEEP, lw=3.5)
poly(s, demand, line_c=CLAY, lw=3.5)
text(s, 1.4, 5.5, 4.2, 1.0, "firewood and charcoal\ndemand", font=SERIF, size=22, italic=True, color=CLAY)
text(s, 8.2, 3.95 + 0.0 + 0.9, 5.0, 0.9, "area planted", font=SERIF, size=22, italic=True, color=DEEP)
oval(s, 5.9, 5.65, 0.26, 0.26, SUN)
text(s, 6.4, 6.0, 2.8, 0.6, "curves cross\n≈ 1950s", font=MONO, size=10, color=SUN)
text(s, 1.0, 9.2, 12.5, 0.3, "1945  ·····································  1970    SCHEMATIC, NOT DATA (James to replace)", font=MONO, size=10, color=MUTE)
for i, (yr, h, b) in enumerate([("1950", "The demand floor drops out", "Fossil fuels replace firewood and charcoal; chemical fertiliser replaces green fertiliser; machines replace draft animals."),
                                 ("1954–55", "Peak planting", "Highest annual area under the 10-Year Plan in 1954. Wave 3, the biggest boom, runs 1955–1970.")]):
    y = 4.1 + i * 2.8
    line(s, 14.0, y, 19.1, y, RULE, 0.75)
    text(s, 14.0, y + 0.1, 5.1, 0.4, yr, font=MONO, size=12, color=CLAY, bold=True)
    text(s, 14.0, y + 0.5, 5.1, 0.7, h, font=SERIF, size=26, italic=True, color=DEEP)
    text(s, 14.0, y + 1.2, 5.1, 1.5, b, size=14, color=SOFT, spacing=1.08)
notes(s, "Sources: Totman; Iwamoto; Matsushita. The two curves are SCHEMATIC. James: a real chart of Forestry Agency planted-area series vs "
         "firewood/charcoal use would be the strongest slide of the history part.")

# ============================================================ HISTORY 9: price collapse
s = history(9, "1951–2025 · SEEDS AND THE CRASH", [("Planted as a retirement fund, ", 0), ("then the market crashed.", 1)])
for i, (lab, val, col, h_) in enumerate([("then", "¥12,000", DEEP, 4.4), ("2025", "¥4,475", CLAY, 4.4 * 4475 / 12000)]):
    x = 1.5 + i * 3.2
    rect(s, x, 8.8 - h_, 2.3, h_, col)
    text(s, x - 0.2, 8.8 - h_ - 0.85, 2.7, 0.8, val, font=SERIF, size=40, color=col, align=PP_ALIGN.CENTER)
    text(s, x - 0.2, 8.85, 2.7, 0.4, lab, font=MONO, size=12, color=MUTE, align=PP_ALIGN.CENTER)
text(s, 0.9, 9.3, 7.2, 0.7, "A-grade sugi per m³ (years and series to be sourced)", font=MONO, size=10, color=MUTE)
for i, (yr, h, b) in enumerate([("1951", "Import tariffs to near zero", "Sensible at the time; it set up self-sufficiency to fall for decades."),
                                 ("1956", "Forest Development Corporation", "Long-term debt plants the least attractive land against a harvest 40–50 years out. After 1980 all 47 prefectural corporations fall into debt distress."),
                                 ("1970s–80s", "Cheap imports", "The market crashes before the planted trees are old enough to cash in. Only A-grade sells today.")]):
    y = 4.1 + i * 1.95
    line(s, 9.0, y, 19.1, y, RULE, 0.75)
    text(s, 9.0, y + 0.1, 2.2, 0.4, yr, font=MONO, size=12, color=CLAY, bold=True)
    text(s, 11.2, y + 0.05, 7.9, 0.5, h, font=SERIF, size=26, italic=True, color=DEEP)
    text(s, 11.2, y + 0.65, 7.9, 1.2, b, size=14, color=SOFT, spacing=1.08)
notes(s, "The ¥12,000 → ¥4,475/m³ line is in the draft outline (docs/meetings/naist_2027-01-13_presentation_draft.md); James to source the series and years "
         "before it goes on a slide. 1956 corporation: Matsushita (2015).")

# ============================================================ HISTORY 10: hinge (full-bleed photo)
s = prs.slides.add_slide(BLANK)
photo(s, IMG("sugi_rice_field.jpg"), 0, 0, 20, 11.25, fx=0.5, fy=0.4)
rect(s, 0, 0, 20, 11.25, DEEP, a=0.62)
rect(s, 0, 0, 20, 11.25, DEEP, a=0.0)
text(s, 0.9, 0.33, 9, 0.35, "HISTORY 10 / 10 · 1958 · THE HINGE", font=MONO, size=11, color=RULE)
tag(s, "JAMES · TO EXPAND")
pagers.append((text(s, 16.3, 10.62, 2.8, 0.35, "", font=MONO, size=11, color=RULE, align=PP_ALIGN.RIGHT), True))
text(s, 0.9, 2.2, 5, 1.2, "1958", font=SERIF, size=96, color=RULE)
text(s, 0.9, 3.9, 14.5, 4.2, [[R("The trees are older than ", color=BG), R("the demand that justified planting them.", italic=True, color=BG)]],
     font=SERIF, size=64, spacing=0.98)
text(s, 0.9, 8.4, 11.5, 1.6, "Deep inside the biggest boom (1955–70), planting compulsory since 1951, self-sufficiency still about 95%. "
                             "The sugi and hinoki in Mitsue's mountains were planted in exactly this window. Over to Rob: today.",
     size=17, color=RULE, spacing=1.2)
rect(s, 13.35, 5.95, 5.8, 3.05, PAPER)
photo(s, IMG("rob_born_1958.jpg"), 13.5, 6.1, 5.5, 2.75, fx=0.5)
text(s, 13.35, 9.1, 5.8, 0.4, "ROB, NOVEMBER 1958", font=MONO, size=11, color=RULE, align=PP_ALIGN.RIGHT)
notes(s, "Hinge line from docs/energy-forest/history/naist_timeline_history_to_1958.md. Rob was born 1958-11-30; inset is his newborn photo (decks/Naist/266980202968.jpg), OK'd by Rob for the public repo. "
         "The Profit-Sharing Forestation Act follows in the same year.")

# ============================================================ 14 TODAY
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, 20, 11.25, BG)
photo(s, IMG("village_landscape.jpg"), 0, 0, 11.2, 11.25, fx=0.55)
text(s, 11.9, 0.33, 7.2, 0.35, f"NAIST SEMINAR · 13 JAN 2027 · v{VERSION} DRAFT", font=MONO, size=11, color=MUTE, align=PP_ALIGN.RIGHT)
eyebrow(s, "TODAY · THE SETTING", x=11.9, y=1.2)
headline(s, [("A village of 1,400 people, ", 0), ("a forest of 7,000 hectares.", 1)], x=11.9, y=1.7, w=7.3, size=46, h=2.6)
for i, (big, small) in enumerate([("≈ 1,400", "residents"), ("≈ 93 %", "forest cover"), ("≈ 7,050 ha", "forest, over 90% private"), ("50–60 yr", "age of the main sugi and hinoki stands")]):
    stat(s, 11.9 + (i % 2) * 3.8, 4.5 + (i // 2) * 2.2, big, small, w=3.5, size=40)
text(s, 11.9, 9.0, 7.2, 1.2, "Many owners are elderly or live elsewhere. At today's prices a cut sugi barely pays for the cutting. Still checking: how many owners, how many parcels, who inherits.",
     size=14, color=SOFT, spacing=1.12)
pagers.append((text(s, 16.3, 10.62, 2.8, 0.35, "", font=MONO, size=11, color=MUTE, align=PP_ALIGN.RIGHT), False))
tag(s, "STILL RESEARCHING", x=15.7, y=1.12) if False else None
notes(s, "Figures: residents and cover from the project deck; 7,051 ha and >90% private from the village plan. Photo: Mitsue landscape from the project funding deck. "
         "The forest register is with the village hall (asked 6 Nov).")

# ============================================================ 15 PROBLEMS
s = slide("THE PROBLEM", [("Three problems with one shape: ", 0), ("nobody is paid to fix it.", 1)])
cols = [("Not enough hands", "The cooperative is small and has few young people. Harvest at scale needs machines and trained operators. Thinning is planned, but most of it is cut and left."),
        ("A ticking clock", "A large share of the forest reaches harvest age inside the same ~25-year window in which new small-scale power technology matures. Nice timing, if we use it."),
        ("No pull to replant", "Cutting sugi for cheap lumber does not pay enough to put anything back. Short-term profit, repeat forever. Nobody has a reason to break the cycle.")]
for i, (h, b) in enumerate(cols):
    x = 0.9 + i * 6.2
    if i:
        line(s, x - 0.3, 3.9, x - 0.3, 9.7, RULE, 0.75)
    cx = x + 0.9
    if i == 0:  # people: one solid, two faded
        for k, (px, aa) in enumerate([(0, None), (0.85, 0.35), (1.7, 0.2)]):
            oval(s, x + px + 0.05, 4.1, 0.5, 0.5, DEEP, a=aa)
            shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, x + px - 0.05, 4.7, 0.7, 0.9, DEEP, a=aa)
    elif i == 1:  # clock
        oval(s, x + 0.05, 4.0, 1.7, 1.7, None, DEEP, 3.0)
        line(s, x + 0.9, 4.85, x + 0.9, 4.2, DEEP, 3.0)
        line(s, x + 0.9, 4.85, x + 1.4, 5.15, CLAY, 3.0)
    else:  # stump with rings
        oval(s, x + 0.05, 4.1, 1.7, 1.2, CLAY)
        oval(s, x + 0.35, 4.3, 1.1, 0.8, None, BG, 1.5)
        oval(s, x + 0.6, 4.5, 0.6, 0.4, None, BG, 1.5)
        rect(s, x + 0.2, 4.7, 1.4, 0.8, CLAY, a=0.0) if False else None
    text(s, x, 6.0, 5.6, 0.9, h, font=SERIF, size=38, italic=True, color=DEEP)
    text(s, x, 7.0, 5.5, 2.8, b, size=17, color=SOFT, spacing=1.2)
notes(s, "Structure from docs/meetings/naist_2027-01-13_presentation_draft.md section 4. Council minutes 2020: the Mayor named the worker shortage as the bottleneck.")

# ============================================================ 16 THINNING LEFT
s = slide("THE PROBLEM IN NUMBERS", [("Most of the thinning wood ", 0), ("stays in the forest.", 1)], tagline="STILL RESEARCHING",
          src="Village forestry plan R6–R8 (FY2024–26); village hall (Oba)")
BX, BW = 0.9, 18.2
rect(s, BX, 4.2, BW, 1.5, DEEP)
rect(s, BX + BW * 0.876, 4.2, BW * 0.124, 1.5, CLAY)
text(s, BX + 0.3, 4.2, 8, 1.5, "18,140 m³", font=SERIF, size=60, color=BG, anchor=MSO_ANCHOR.MIDDLE)
text(s, BX + 5.2, 4.2, 8, 1.5, "cut and left in the forest", size=19, color=RULE, anchor=MSO_ANCHOR.MIDDLE)
text(s, BX + BW * 0.876 - 0.3, 5.8, 3.2, 0.9, "2,574 m³\ntaken out", font=SERIF, size=24, italic=True, color=CLAY, align=PP_ALIGN.LEFT, spacing=0.95)
text(s, 0.9, 6.0, 8, 0.5, "PLANNED THINNING FY2024–26 · 113 PARCELS · ≈ 222 ha · 4 DISTRICTS", font=MONO, size=11, color=MUTE)
photo(s, IMG("team_in_forest.jpg"), 0.9, 6.9, 6.0, 3.2, fx=0.5, fy=0.5)
stat(s, 7.5, 6.9, "≈ 88 %", "stays in the forest: about 860 m³ a year actually comes out", w=3.7, size=52)
text(s, 11.9, 6.9, 7.2, 3.3, [
    "That cut-and-left wood is a fuel resource, if it can be collected at a price that makes sense. Steep slopes and missing roads are why it is left.",
    [R("Still checking: ", bold=True, color=CLAY), R("how much is reachable with a winch-assisted machine, and what an earlier '120–300 m³/yr' cooperative figure really measured.")]],
     size=16, color=SOFT, spacing=1.18, after=12)
notes(s, "18,140 of 20,714 m³ left; 2,574 out over three years (about 860/yr). Verify with the village data sheet (xlsx) before the talk. "
         "Photo: forestry team in the forest, from the project funding deck: confirm we may show it and who is in it.")

# ============================================================ 17 IDEA FLOW
s = slide("THE IDEA", [("Pull, don't push: ", 0), ("give the wood a buyer that pays.", 1)])
steps = [("1", "Thin and clear", "Cut-to-length machines on steep sugi"), ("2", "Sort A / B / C / D", "A and B to the sawmill, C and D to chips"),
         ("3", "Chip and dry", "Local chipping, drying with CHP heat"), ("4", "Small CHP", "Gasification plant: power and heat, 24 h")]
for i, (n, h, b) in enumerate(steps):
    x = 0.9 + i * 4.6
    c = shape(s, MSO_SHAPE.PENTAGON, x, 4.1, 4.5, 1.7, CLAY if i == 0 else DEEP)
    text(s, x + 0.3, 4.2, 3.6, 0.7, [[R(n + "  ", font=MONO, size=13, color=RULE), R(h, font=SERIF, size=28, italic=True, color=BG)]])
    text(s, x + 0.3, 4.9, 3.5, 0.9, b, size=14, color=BG, spacing=1.05)
for i, (cx_, kind) in enumerate([(2.4, "tree"), (7.0, "logs"), (11.6, "chips"), (16.2, "plant")]):
    if kind == "tree":
        tree(s, cx_, 7.5, 1.4, ACC)
        tree(s, cx_ + 0.6, 7.5, 1.1, LEAF)
    elif kind == "logs":
        for k in range(3):
            oval(s, cx_ - 0.7 + k * 0.5, 6.75 + (k % 2) * 0.3, 0.55, 0.55, CLAY)
            oval(s, cx_ - 0.57 + k * 0.5, 6.88 + (k % 2) * 0.3, 0.3, 0.3, None, BG, 1.0)
    elif kind == "chips":
        for k in range(14):
            rect(s, cx_ - 0.7 + (k % 7) * 0.2, 7.05 + (k // 7) * 0.22, 0.14, 0.09, CLAY)
    else:
        rect(s, cx_ - 0.6, 6.9, 1.2, 0.7, DEEP)
        rect(s, cx_ - 0.35, 6.4, 0.18, 0.5, DEEP)
        for k in range(3):
            rect(s, cx_ - 0.45 + k * 0.4, 7.15, 0.22, 0.22, BG)
line(s, 0.9, 8.15, 19.1, 8.15, RULE, 0.75)
text(s, 0.9, 8.35, 8.8, 1.8, [[R("Why 'pull'. ", font=SERIF, size=26, italic=True, color=DEEP),
                               R("Waiting for a subsidy pushes wood out once, then stops. A buyer that wants fuel 24 hours a day pulls wood out every year, and can pay for the replanting.")]],
     size=15, color=SOFT, spacing=1.15)
text(s, 10.2, 8.35, 8.9, 1.8, [[R("Then replant. ", font=SERIF, size=26, italic=True, color=DEEP),
                                R("Cleared stands go back to native broadleaf (oak, chestnut, konara) for wildlife and watershed, with fast-growing kiri on part of the land. Species chosen with the NGO more trees.")]],
     size=15, color=SOFT, spacing=1.15)
notes(s, "Core of the talk (~10 min). Compute (AI data center) is the later anchor customer: present as 'a small compute load next to the CHP', not a done deal.")

# ============================================================ 18 PUSH vs PULL (dark)
s = slide("THE IDEA · TWO WAYS TO MOVE WOOD", [("Push stops. ", 0), ("Pull keeps going.", 1)], dark=True)
text(s, 0.9, 3.9, 8, 0.4, "PUSH · A ONE-OFF SUBSIDY", font=MONO, size=12, color=RULE)
oval(s, 1.2, 5.6, 1.6, 1.6, None, RULE, 1.5)
text(s, 1.2, 5.6, 1.6, 1.6, "forest", font=SERIF, size=24, italic=True, color=BG, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
line(s, 2.9, 6.4, 6.4, 6.4, CLAY, 2.5, arrow=True)
text(s, 3.0, 5.7, 3.5, 0.5, "subsidy", font=MONO, size=11, color=CLAY)
text(s, 6.5, 6.0, 2.5, 0.8, "…then nothing", font=SERIF, size=24, italic=True, color=RULE)
line(s, 9.5, 3.9, 9.5, 9.6, ACC, 1.0)
text(s, 10.2, 3.9, 8, 0.4, "PULL · A BUYER FOR FUEL, 24 HOURS A DAY", font=MONO, size=12, color=RULE)
nodes = [("forest", 14.6, 5.0), ("chips", 17.4, 6.9), ("CHP + compute", 14.6, 8.7), ("landowners\n+ replanting", 11.8, 6.9)]
cx, cy = 14.6, 6.9
for nm, nx, ny in nodes:
    oval(s, nx - 1.0, ny - 0.75, 2.0, 1.5, DEEP if nm != "CHP + compute" else CLAY, RULE, 1.25)
    text(s, nx - 1.0, ny - 0.75, 2.0, 1.5, nm, font=SERIF, size=21, italic=True, color=BG, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=0.95)
for (ax, ay, bx, by) in [(15.5, 5.55, 16.7, 6.25), (17.2, 7.65, 15.6, 8.3), (13.6, 8.3, 12.2, 7.6), (12.3, 6.2, 13.7, 5.5)]:
    line(s, ax, ay, bx, by, RULE, 2.0, arrow=True)
text(s, 10.2, 9.75, 8.8, 0.8, "Money from the plant flows back to owners and pays for replanting: the loop closes.", font=SERIF, size=20, italic=True, color=RULE)
notes(s, "'Pull, don't push': an AI data center + biomass CHP creates a buyer for wood that actually pays, pulling sustainable forestry forward "
         "instead of waiting for a subsidy.")

# ============================================================ 19 LOGS
s = slide("THE IDEA · WHAT A TREE IS WORTH", [("Only A-grade wood sells. ", 0), ("B, C and D are a problem we can use.", 1)],
          tagline="STILL RESEARCHING", src="Grade descriptions simplified; model v1.2 (61% A national average, 22% A thinning-type stands)")
logs = [("A", "Straight, clean, few knots", "Sawlog. The only grade worth cutting for lumber.", 2.1, DEEP),
        ("B", "Slightly bent, some knots", "Sawlog or laminated. Price depends on the buyer.", 1.8, ACC),
        ("C", "Crooked or small", "Chips, pulp, board. Cheap.", 1.4, CLAY),
        ("D", "Branches, tops, bark", "Today: left on the slope.", 1.0, MUTE)]
for i, (g, h, b, d, col) in enumerate(logs):
    x = 0.9 + i * 4.62
    cx_ = x + 2.2
    oval(s, cx_ - d, 5.8 - d, d * 2, d * 2, col)
    for k, f in enumerate([0.75, 0.5, 0.25]):
        oval(s, cx_ - d * f, 5.8 - d * f, d * f * 2, d * f * 2, None, BG, 1.0)
    text(s, x, 3.4, 1, 1, g, font=SERIF, size=64, italic=True, color=col)
    text(s, x, 8.0, 4.3, 0.7, h, font=SERIF, size=24, italic=True, color=DEEP)
    text(s, x, 8.7, 4.2, 1.2, b, size=14, color=SOFT, spacing=1.1)
notes(s, "Grade definitions are simplified: check against the Japanese log-grading rules before presenting to forestry specialists. "
         "Idea: CHP fuel plus a data-center customer means C and D wood suddenly has a buyer too; the sawlogs still fund most of the work.")

# ============================================================ 20 REPLANT before/after
s = slide("THE IDEA · THEN REPLANT", [("From one crop of cedar ", 0), ("to a forest that feeds the bears.", 1)])
rect(s, 0.9, 3.8, 8.7, 4.7, PAPER, RULE, 0.75)
rect(s, 10.4, 3.8, 8.7, 4.7, PAPER, RULE, 0.75)
rect(s, 0.9, 7.3, 8.7, 1.2, BG2)
rect(s, 10.4, 7.3, 8.7, 1.2, BG2)
for k in range(11):
    tree(s, 1.4 + k * 0.76, 7.3, 2.9, DEEP)
import random
random.seed(4)
for k in range(9):
    tree(s, 10.9 + k * 0.92, 7.3, random.choice([2.0, 2.4, 2.8, 1.7]), random.choice([ACC, LEAF, CLAY, LEAF]), "round")
tree(s, 14.8, 7.3, 3.4, CLAY, "cone")
text(s, 1.1, 3.9, 6, 0.4, "BEFORE · MONOCULTURE", font=MONO, size=11, color=MUTE)
text(s, 10.6, 3.9, 7, 0.4, "AFTER · NATIVE BROADLEAF + KIRI", font=MONO, size=11, color=ACC)
text(s, 1.1, 7.6, 8, 0.8, "pollen, landslide risk, nothing to eat", font=SERIF, size=22, italic=True, color=MUTE)
text(s, 10.6, 7.6, 8, 0.8, "oak, chestnut, konara: acorns for wildlife", font=SERIF, size=22, italic=True, color=DEEP)
text(s, 0.9, 8.9, 8.8, 1.3, "Species are chosen with the NGO more trees. The village's default is native broadleaf, not another monoculture.", size=15, color=SOFT)
text(s, 10.4, 8.9, 8.7, 1.3, "Kiri (paulownia) is a fast fuel crop on part of the land: Tokushima growth data 8.6 t dry/ha/yr; Mitsue growth data requested from SANSEI. Still checking.",
     size=15, color=SOFT)
notes(s, "Reforestation principle: native broadleaf for wildlife forage; NGO picks species. Kiri figures from model v1.2; do not cite IGES/Miyawaki figures "
         "(Morales 2025 review: evidence weak). Drawings are schematic.")

# ============================================================ 21 NUMBERS
s = slide("THE FIRST NUMBERS", [("Our first model says plus, ", 0), ("then shows how fragile that is.", 1)], tagline="PLACEHOLDER PRICES",
          src="kiri_sugi_integrated_system_model_2026-11-03.xlsx v1.2. All prices and costs are placeholders, not quotes.")
cases = [("Base case", 45), ("Owners get 0 %", 79), ("Owners get 50 %", 22), ("No residue collected", 32), ("Replant kiri every cut", 26),
         ("Thinning-type grade split", 4), ("317 m³/ha, 95 ha/yr", 1), ("Low price, high cost", -10)]
text(s, 0.9, 3.8, 11, 0.4, "STEADY-STATE SYSTEM NET, ¥M PER YEAR", font=MONO, size=11, color=MUTE)
ZERO, SC, ROW = 6.9, 0.062, 0.68
for i, (lab, v) in enumerate(cases):
    y = 4.25 + i * ROW
    text(s, 0.9, y, 4.1, 0.55, lab, size=15, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    w = max(abs(v) * SC, 0.04)
    rect(s, ZERO if v >= 0 else ZERO - w, y + 0.06, w, 0.42, CLAY if v < 0 else (ACC if lab == "Base case" else DEEP))
    text(s, ZERO + w + 0.1 if v >= 0 else ZERO - w - 0.9, y, 0.8, 0.55, f"{v:+d}".replace("-", "−"), size=15, bold=True,
         align=PP_ALIGN.LEFT if v >= 0 else PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
rect(s, ZERO - 0.01, 4.2, 0.03, 8 * ROW + 0.05, MUTE)
rect(s, 12.9, 3.9, 6.2, 5.7, DEEP)
text(s, 13.3, 4.1, 5.4, 0.9, "Not a forecast.", font=SERIF, size=38, italic=True, color=BG)
text(s, 13.3, 5.1, 5.4, 4.4, ["50 ha/yr clear-cut at 600 m³/ha, sawlogs sold, C+D chipped, half the land replanted to kiri, landowners paid 30% of sawlog net.",
                              "At the village's actual standing volume (277–317 m³/ha) the base case falls to about break-even.",
                              "Left out: carbon credits, data-center income, machine purchase, wages."], size=14, color=RULE, spacing=1.15, after=9)
notes(s, "Steady-state system net, ¥M/yr, from model v1.2. Say clearly: feasibility sizing, not a forecast. Do NOT state +45 as an expected result.")

# ============================================================ 22 FOUR UNKNOWNS (range graphic)
s = slide("WHAT DECIDES IT", [("Four unknowns decide the answer, ", 0), ("not the technology.", 1)], tagline="STILL RESEARCHING",
          src="kiri_sugi_system_summary_2026-11-03.md, 'What drives the result'")
rng = [("Wood per hectare", "m³/ha", 0, 700, [(277, 317, "village plan", CLAY)], [(600, "model", DEEP)], "Model assumes 600; village plan shows 277–317."),
       ("A-grade share", "% of volume", 0, 100, [(22, 22, "thinning-type", CLAY)], [(61, "national avg", DEEP)], "Sawlog sales fund everything."),
       ("Landowner share", "% of sawlog net", 0, 60, [(0, 0, "", CLAY)], [(30, "our choice", DEEP)], "Each 10 points costs about ¥11M a year."),
       ("Residue price", "¥ per tonne", 0, 10000, [(4000, 4000, "placeholder", CLAY)], [(8000, "if doubled", DEEP)], "Doubling adds only about ¥1.6M a year: minor.")]
for i, (nm, unit, lo, hi, a_, b_, note) in enumerate(rng):
    y = 4.0 + i * 1.5
    text(s, 0.9, y, 4.6, 0.5, nm, font=SERIF, size=30, italic=True, color=DEEP)
    text(s, 0.9, y + 0.6, 4.6, 0.4, unit.upper(), font=MONO, size=10, color=MUTE)
    tx0, tx1 = 5.8, 14.2
    pos = lambda v: tx0 + (v - lo) / (hi - lo) * (tx1 - tx0)
    rect(s, tx0, y + 0.42, tx1 - tx0, 0.08, RULE)
    for (v1, v2, lab, col) in a_:
        rect(s, pos(v1) - (0.0), y + 0.3, max(pos(v2) - pos(v1), 0.0) + 0.08, 0.32, col)
        oval(s, pos(v2) - 0.13, y + 0.31, 0.3, 0.3, col)
        text(s, pos(v1) - 1.1, y - 0.15, 2.8, 0.4, lab, font=MONO, size=10, color=col, align=PP_ALIGN.CENTER if v1 else PP_ALIGN.LEFT)
    for (v, lab, col) in b_:
        oval(s, pos(v) - 0.15, y + 0.29, 0.34, 0.34, col)
        text(s, pos(v) - 1.1, y + 0.7, 2.6, 0.4, lab, font=MONO, size=10, color=col, align=PP_ALIGN.CENTER)
    text(s, 14.8, y + 0.1, 4.3, 1.0, note, size=13, color=SOFT, spacing=1.08)
    line(s, 0.9, y + 1.32, 19.1, y + 1.32, RULE, 0.5)
notes(s, "Clay = what the village data suggests; green = what the first model assumed. The gap between them is why we say 'fragile'. "
         "Landowner share: base 30%; residue: ¥4,000/t placeholder.")

# ============================================================ 23 ENERGY SCALE
s = slide("THE ENERGY SIDE", [("Start small to learn. ", 0), ("Size the real plant to the wood we can get.", 1)], tagline="STILL RESEARCHING",
          src="Energy, finance and resources overview v1.1 (2026-11-03)", title_size=50)
base_y = 8.6
rect(s, 0.9, base_y, 18.2, 0.1, CLAY)
rect(s, 1.3, base_y - 0.9, 1.7, 0.9, DEEP)
text(s, 3.15, base_y - 0.95, 3.2, 0.9, [[R("50 kWe", font=SERIF, size=34, italic=True, color=DEEP)]])
text(s, 1.3, base_y + 0.25, 4.5, 0.9, "Prototype in a 20 ft container. ≈ 450–600 t dry wood a year. A learning step: efficiency only ~12–20% at this size.", size=12, color=SOFT, spacing=1.05)
rect(s, 6.8, base_y - 2.3, 4.2, 2.3, ACC)
rect(s, 8.7, base_y - 3.2, 0.3, 0.9, ACC)
for k in range(4):
    rect(s, 7.1 + k * 0.95, base_y - 1.5, 0.5, 0.6, BG)
text(s, 6.8, base_y - 4.3, 4.5, 0.9, [[R("≈ 0.5–0.6 MWe", font=SERIF, size=34, italic=True, color=ACC)]])
text(s, 6.8, base_y + 0.25, 4.6, 0.9, "First commercial size. 23–28% efficiency for gasifier plus engine at this scale. Fuel mostly C+D wood and residue.", size=12, color=SOFT, spacing=1.05)
rect(s, 12.2, base_y - 4.4, 5.6, 4.4, None, MUTE, 1.5)
rect(s, 12.2, base_y - 4.4, 5.6, 4.4, MUTE, a=0.12)
text(s, 12.2, base_y - 4.35 - 0.0, 5.6, 0.9, [[R("1.2 MWe", font=SERIF, size=34, italic=True, color=MUTE)]], align=PP_ALIGN.CENTER)
text(s, 12.4, base_y - 3.3, 5.2, 2.2, "needs ≈ 24,000 m³ of fuel a year. Not until the harvest is proven. At ≥ 1,000 kW the tariff is FIP-only, and splitting is not allowed.", size=13, color=MUTE, spacing=1.1)
text(s, 12.2, base_y + 0.25, 5.6, 0.9, "NOT TO SCALE", font=MONO, size=10, color=MUTE)
text(s, 0.9, 9.7, 18.2, 0.5, "Also: Japanese maker only; gasification + engine beats steam below ~1 MWe; grid at 6.6 kV has about 3 MW locally, none upstream; fuel may be bought from neighbouring villages.",
     size=12, color=SOFT)
notes(s, "'Fuel from neighbours' is not yet in the model (needs delivered ¥/t and haul distance). Do not name a CHP maker in public: shortlist and quotes are in flux.")

# ============================================================ 24 PRECEDENTS
s = slide(None, None, src="Tenkawa Forest Power Council; Aizu (2011) Safecast blog; Buena Vista, DT/Metzler, IIJ Matsue", tagline="STILL RESEARCHING")
photo(s, IMG("old_school.jpg"), 0.9, 1.2, 8.4, 8.8, fx=0.5)
text(s, 9.9, 1.2, 9, 0.4, "NOT JUST US DREAMING", font=MONO, size=12, color=ACC)
headline(s, [("Pieces of this already exist, ", 0), ("in Japan and abroad.", 1)], x=9.9, y=1.75, w=9.2, size=46, h=2.2)
for i, (h, b, col) in enumerate([("Tenkawa, next door", "A biomass council since 2016; a wood boiler heats the Dorogawa hot spring baths. We visited on 25 Aug 2026.", DEEP),
                                  ("Aizu, 2011", "A closed school (Akazawa Elementary) turned into a data center. A precedent for an empty school building like ours.", ACC),
                                  ("Wood power plus compute", "Tried before: Buena Vista (US), Deutsche Telekom with Bankhaus Metzler (Germany), IIJ Matsue (Japan).", CLAY)]):
    y = 4.5 + i * 1.6
    line(s, 9.9, y, 19.1, y, RULE, 0.75)
    text(s, 9.9, y + 0.1, 9.2, 0.6, h, font=SERIF, size=28, italic=True, color=col)
    text(s, 9.9, y + 0.7, 9.2, 0.9, b, size=14, color=SOFT, spacing=1.08)
text(s, 9.9, 9.35, 9.2, 0.7, [[R("Still checking ", bold=True, color=CLAY), R("what each one really is and what transfers. Leads, not proof.")]], size=14, color=SOFT)
text(s, 0.9, 10.05, 8.4, 0.3, "The closed Mitsue school building.", font=MONO, size=10, color=MUTE)
notes(s, "Each precedent needs one verified sentence. Photo: the closed Mitsue elementary school (from the project funding deck). "
         "Do not claim these are identical to our plan. Tenkawa photos from the 2026-08-25 meeting can be added.")

# ============================================================ 25 HOMEWORK
s = slide("WHAT WE DID", [("The homework so far: ", 0), ("we read, we asked, we counted.", 1)], src="repository docs/, research/, docs/reference/")
nums = [("45", "village, prefectural and national acts on forestry, biomass, 協力隊 and siting, collected and summarised"),
        ("113", "parcels in the village thinning plan, read parcel by parcel"),
        ("2", "rounds of questions to Komatsu on steep-slope harvesting; gasification CHP makers compared"),
        ("1.2", "version of the spreadsheet model linking clear-cut, sawlogs, chips, kiri, CHP and landowner payments"),
        ("5+", "site and office visits: forest, village hall, Uda City cooperative, Tenkawa"),
        ("100%", "of it open, in a public repository, so anyone including NAIST students can check or challenge it")]
for i, (big, small) in enumerate(nums):
    stat(s, 0.9 + (i % 3) * 4.2, 3.9 + (i // 3) * 2.9, big, small, w=3.9, size=64)
photo(s, IMG("team_in_forest.jpg"), 13.6, 3.9, 5.5, 5.6, fx=0.5)
text(s, 13.6, 9.55, 5.5, 0.4, "Forest work in Mitsue (confirm who and where).", font=MONO, size=10, color=MUTE)
notes(s, "Numbers: 45 acts (village regulations folder), 113 parcels (thinning plan). Edit to match what James has also done. "
         "Public repository: https://codeberg.org/YR-Design/mitsue-ai-data-center (mirror on GitHub). Photo needs a caption/consent check.")

# ============================================================ 26 OPEN QUESTIONS
s = slide("WHAT WE DO NOT KNOW YET", [("An honest list of open questions, ", 0), ("and who is answering them.", 1)], tagline="STILL RESEARCHING",
          src="docs/strategy/mitsue_energy_finance_resources_overview_2026-11-03.md section 5")
rows = [("Stand volume, stumpage, who gets the sale income", "Village hall (Oba)", "asked 6 Nov"),
        ("Slope limits with and without winch, road width, yearly output", "Komatsu", "follow-up sent"),
        ("Real CHP efficiency and cost at 0.6–0.8 MWe", "Maker quotes", "to request"),
        ("Kiri growth on Mitsue slopes", "SANSEI planting data", "asked 2 Nov"),
        ("Grid connection at 6.6 kV", "Kansai T&D", "consultation drafted"),
        ("Fuel bought in from neighbouring villages", "Uda City, others", "to approach"),
        ("What students and researchers would measure", "NAIST (you)", "to discuss")]
y = 3.8
for xx, w, t in [(0.9, 10, "OPEN QUESTION"), (11.7, 4, "WHO"), (15.9, 3.2, "STATUS")]:
    text(s, xx, y, w, 0.35, t, font=MONO, size=11, color=MUTE)
y += 0.45
for i, (q, w, st) in enumerate(rows):
    line(s, 0.9, y, 19.1, y, RULE, 0.75)
    last = (i == len(rows) - 1)
    if last:
        rect(s, 0.9, y + 0.02, 18.2, 0.8, DEEP)
    text(s, 1.0, y + 0.05, 10.5, 0.75, q, font=SERIF, size=24, italic=last, color=BG if last else INK, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 11.7, y + 0.05, 4, 0.75, w, size=15, bold=True, color=RULE if last else DEEP, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 15.9, y + 0.05, 3.2, 0.75, st, font=MONO, size=11, color=RULE if last else CLAY, anchor=MSO_ANCHOR.MIDDLE)
    y += 0.84
line(s, 0.9, y, 19.1, y, RULE, 0.75)
notes(s, "Refresh right before the talk: statuses change weekly. The last row is the real ask to NAIST.")

# ============================================================ 27 STATUS TIMELINE
s = slide("WHERE WE STAND", [("Early planning. ", 0), ("No money raised, no contracts, no machines bought.", 1)], title_size=50)
tl = [("NOW", "Phase 0", "Trust, sites, fuel talks, homework", CLAY), ("DEC 2026", "Phase 0 ends", "Decision on first site and partners", DEEP),
      ("2027", "Prototype", "50 kWe CHP and fuel trial, if site and partners settle", DEEP), ("2028 →", "Machines", "A CTL trial if a fit is shown and financing is in place", DEEP),
      ("LATER", "Full scale", "≈ 0.5–1.2 MWe and a larger compute load; no fixed date", MUTE)]
poly(s, [(1.5, 6.3), (3.5, 6.3), (6.0, 6.3), (8.5, 6.3), (11.0, 6.3), (13.5, 6.3), (16.0, 6.3), (18.6, 6.3)], line_c=ACC, lw=2.5)
for i, (when, h, b, c) in enumerate(tl):
    x = 1.0 + i * 3.7
    oval(s, x + 0.4, 6.0, 0.6, 0.6, c)
    text(s, x, 4.5, 3.4, 0.4, when, font=MONO, size=12, color=c, bold=True)
    text(s, x, 4.95, 3.4, 0.9, h, font=SERIF, size=34, italic=True, color=DEEP)
    text(s, x, 6.95, 3.4, 2.0, b, size=14, color=SOFT, spacing=1.1)
rect(s, 0.9, 8.85, 18.2, 1.2, PAPER, RULE, 0.75)
rect(s, 0.9, 8.85, 0.08, 1.2, CLAY)
text(s, 1.3, 8.9, 17.5, 1.1, "¥0 committed. Dates are targets, not promises. The grant tracks we know of (METI GX regional, MoE zero-emission data center) are being studied, not applied for.",
     font=SERIF, size=22, italic=True, color=SOFT, anchor=MSO_ANCHOR.MIDDLE)
notes(s, "Align the dates with the current phase plan (Phase 0 extended to Dec 2026, later phases shifted three months). Never imply contracts exist.")

# ============================================================ 28 SLOGAN (photo)
s = prs.slides.add_slide(BLANK)
photo(s, IMG("village_landscape.jpg"), 0, 0, 20, 11.25, fx=0.5)
rect(s, 0, 0, 20, 11.25, DEEP, a=0.72)
text(s, 0.9, 0.33, 9, 0.35, "THE LONG VIEW", font=MONO, size=11, color=RULE)
pagers.append((text(s, 16.3, 10.62, 2.8, 0.35, "", font=MONO, size=11, color=RULE, align=PP_ALIGN.RIGHT), True))
text(s, 1.5, 3.4, 17.5, 2.2, "75 years to grow the forest.", font=SERIF, size=80, color=BG)
text(s, 1.5, 5.4, 17.5, 2.2, "25 years to grow the village.", font=SERIF, size=80, italic=True, color=RULE)
text(s, 1.5, 8.5, 14, 1.4, "A hundred-year plan in the old Goryōrin spirit: planting for the people who will be here when the trees are ready.",
     font=SERIF, size=26, color=BG, spacing=1.1)
notes(s, "Closing image. Link back to the Goryōrin slide (history 5): the last time anyone planned forestry on this horizon.")

# ============================================================ 29 Q&A
s = slide("Q&A", [("Tell us ", 0), ("where we are wrong.", 1)], dark=True, title_size=70)
text(s, 0.9, 4.4, 14, 2.4, ["Honest critique is more useful to us than polite interest.", "What would you measure? What would you doubt? Who else should we ask?"],
     font=SERIF, size=34, color=BG, after=18, spacing=1.1)
line(s, 0.9, 7.6, 19.1, 7.6, ACC, 1.0)
text(s, 0.9, 7.9, 18, 2.2, ["Rob Oudendijk · Mitsue-it · rob@mitsue.it", "All documents open: https://codeberg.org/YR-Design/mitsue-ai-data-center", "Website: mitsue.it"],
     font=MONO, size=16, color=RULE, after=10)
s.shapes.add_picture(ILLUS, Inches(12.6), Inches(3.4), Inches(6.5), Inches(5.78))
notes(s, "Q&A ~5 min. Check the signature block against docs/outreach/email_signature_standard.md. Add James's contact line only if he agrees.")

# ------------------------------------------------------------ page numbers
total = len(prs.slides)
for i, (tb, dark) in enumerate(pagers, 1):
    r = tb.text_frame.paragraphs[0].add_run()
    r.text = f"{i:02d} / {total:02d}"
    r.font.name, r.font.size = MONO, Pt(11)
    r.font.color.rgb = RULE if dark else MUTE
assert len(pagers) == total, (len(pagers), total)
prs.core_properties.title = f"Mitsue NAIST Seminar v{VERSION}"
prs.core_properties.author = "Mitsue-it"
prs.save(OUT)
print("saved", os.path.abspath(OUT), total, "slides")
