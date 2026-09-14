"""Render assets/card-<slug>-{dark,light}.svg — one project card per selected project.

Same rules as header.py: titles are Georgia outlines so they render identically
everywhere, body copy is a system sans stack, colours come from palette.py.
The numbers drawn on the cards are copied from the projects' committed results
(match3-lab docs/curve-1000.csv, turkish-rag-eval results/summary.json).
    python scripts/cards.py
"""
from pathlib import Path

from header import outline
from palette import THEMES

OUT = Path(__file__).resolve().parent.parent / "assets"
SANS = "'Segoe UI',system-ui,-apple-system,Ubuntu,'Helvetica Neue',sans-serif"
MONO = "Consolas,'SF Mono',Menlo,monospace"

# match3-lab docs/curve-1000.csv — win rate per level, 1000 games per bot
GREEDY = [1.000, 0.980, 0.908, 0.800, 0.597, 0.497]
RANDOM = [0.701, 0.167, 0.273, 0.297, 0.091, 0.031]
# turkish-rag-eval results/summary.json — best nDCG@10 per retriever across chunkers
RAG = [("BM25", 0.410), ("BM25 + 5-char prefix", 0.510), ("dense", 0.501), ("hybrid RRF", 0.607)]


def text(t, x, y, s, size=14, fill="soft", weight=400, anchor="start", spacing=0, family=SANS):
    return (f'<text x="{x}" y="{y}" fill="{t[fill]}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" letter-spacing="{spacing}">{s}</text>')


def title(t, x, y, first, last, size):
    """`first` in ink, `last` italic in accent — the site's project-title treatment."""
    a, w = outline("georgia.ttf", first, size, x, y)
    b, _ = outline("georgiai.ttf", last, size, x + w, y)
    return f'<path fill="{t["ink"]}" d="{a}"/><path fill="{t["accent"]}" d="{b}"/>'


def numeral(t, x, y, n, size):
    d, _ = outline("georgiai.ttf", n, size, x, y)
    return f'<path fill="none" stroke="{t["accent"]}" stroke-opacity=".45" stroke-width="1.4" d="{d}"/>'


def frame(t, w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">\n'
            f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="18" fill="{t["panel"]}" stroke="{t["hair"]}"/>\n'
            f'{body}\n</svg>\n')


def card_body(t, n, first, last, lines, tags, w):
    """Left column shared by every card: numeral, title, copy, tags."""
    x = 40
    parts = [numeral(t, x - 4, 146, n, 128), title(t, x, 172, first, last, 32)]
    for i, line in enumerate(lines):
        parts.append(text(t, x, 202 + i * 20, line, 13))
    parts.append(text(t, x, 268, tags, 11, "muted", 600, spacing=1.6))
    parts.append(f'<line x1="{w - 230}" y1="40" x2="{w - 230}" y2="260" stroke="{t["hair"]}"/>')
    return "".join(parts)


# ---------------------------------------------------------------- pictograms

def curve(t, x0, y0, w, h):
    """Greedy vs random win rate over six levels."""
    out = [text(t, x0, y0 - 18, "DIFFICULTY CURVE · 1000 BOT GAMES PER LEVEL", 11, "muted", 600, spacing=1.6)]
    for frac, lab in [(0, "100%"), (0.5, "50%"), (1, "0%")]:
        y = y0 + frac * h
        out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + w}" y2="{y:.1f}" stroke="{t["hair"]}"/>')
        out.append(text(t, x0 + w + 10, y + 4, lab, 11, "muted"))
    step = w / 5
    for series, color, dash, width in [(RANDOM, t["muted"], ' stroke-dasharray="4 5"', 1.4), (GREEDY, t["accent"], "", 2.2)]:
        pts = [(x0 + i * step, y0 + (1 - v) * h) for i, v in enumerate(series)]
        d = " ".join(f"{'M' if i == 0 else 'L'}{px:.1f} {py:.1f}" for i, (px, py) in enumerate(pts))
        out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{dash} stroke-linejoin="round"/>')
        if not dash:
            out += [f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{t["panel"]}" stroke="{color}" stroke-width="2"/>' for px, py in pts]
    for i in range(6):
        out.append(text(t, x0 + i * step, y0 + h + 20, f"0{i + 1}", 11, "muted", anchor="middle", family=MONO))
    lx = x0
    out.append(f'<line x1="{lx}" y1="{y0 + h + 44}" x2="{lx + 22}" y2="{y0 + h + 44}" stroke="{t["accent"]}" stroke-width="2.2"/>')
    out.append(text(t, lx + 30, y0 + h + 48, "greedy bot", 12, "soft"))
    out.append(f'<line x1="{lx + 120}" y1="{y0 + h + 44}" x2="{lx + 142}" y2="{y0 + h + 44}" stroke="{t["muted"]}" stroke-width="1.4" stroke-dasharray="4 5"/>')
    out.append(text(t, lx + 150, y0 + h + 48, "random bot", 12, "soft"))
    return "".join(out)


def glyph_tiles(t, x0, y0):
    """A line of text as glyph tiles; the ones the font cannot draw are tofu."""
    out = [text(t, x0, y0 - 14, "MISSING GLYPHS", 11, "muted", 600, spacing=1.6)]
    row = [("S", True), ("a", True), ("ğ", False), ("l", True), ("ı", False), ("k", True)]
    for i, (ch, ok) in enumerate(row):
        x = x0 + i * 26
        if ok:
            d, w = outline("georgia.ttf", ch, 22, 0, 0)
            out.append(f'<rect x="{x}" y="{y0}" width="22" height="30" rx="5" fill="none" stroke="{t["hair"]}"/>')
            out.append(f'<path transform="translate({x + 11 - w / 2:.1f} {y0 + 22})" fill="{t["soft"]}" d="{d}"/>')
        else:
            out.append(f'<rect x="{x}" y="{y0}" width="22" height="30" rx="5" fill="{t["accent"]}" fill-opacity=".14" stroke="{t["accent"]}"/>')
            out.append(f'<rect x="{x + 6}" y="{y0 + 8}" width="10" height="14" fill="none" stroke="{t["accent"]}" stroke-width="1.2"/>')
    y = y0 + 58
    for i, (lab, val) in enumerate([("tr.txt", "clean"), ("ja.txt", "15 missing")]):
        out.append(text(t, x0, y + i * 22, lab, 12, "muted", family=MONO))
        out.append(text(t, x0 + 156, y + i * 22, val, 12, "soft", anchor="end", family=MONO))
    out.append(f'<rect x="{x0}" y="{y + 40}" width="82" height="22" rx="11" fill="{t["accent"]}" fill-opacity=".14" stroke="{t["accent"]}"/>')
    out.append(text(t, x0 + 41, y + 55, "EXIT 1", 11, "accent", 600, anchor="middle", spacing=1.6))
    return "".join(out)


def bars(t, x0, y0):
    out = [text(t, x0, y0 - 14, "nDCG@10 BY RETRIEVER", 11, "muted", 600, spacing=1.6)]
    best = max(v for _, v in RAG)
    for i, (lab, v) in enumerate(RAG):
        y = y0 + i * 44
        strong = v == best
        out.append(text(t, x0, y + 12, lab, 12, "ink" if strong else "soft"))
        out.append(f'<rect x="{x0}" y="{y + 20}" width="156" height="6" rx="3" fill="{t["hair"]}"/>')
        out.append(f'<rect x="{x0}" y="{y + 20}" width="{156 * v / best:.1f}" height="6" rx="3" fill="{t["accent"]}" fill-opacity="{1 if strong else 0.45}"/>')
        out.append(text(t, x0 + 156, y + 12, f"{v:.2f}", 12, "accent" if strong else "muted", anchor="end", family=MONO))
    return "".join(out)


def magnifier(t, x0, y0):
    cx, cy, r = x0 + 60, y0 + 64, 44
    q, w = outline("georgiai.ttf", "?", 64, 0, 0)
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{t["accent"]}" fill-opacity=".08" stroke="{t["accent"]}" stroke-width="2.5"/>'
        f'<line x1="{cx + r * 0.72:.1f}" y1="{cy + r * 0.72:.1f}" x2="{cx + r + 40}" y2="{cy + r + 40}" stroke="{t["accent"]}" stroke-width="7" stroke-linecap="round"/>'
        f'<path transform="translate({cx - w / 2:.1f} {cy + 22})" fill="{t["ink"]}" d="{q}"/>'
    )


def dashboard(t, x0, y0):
    out = [text(t, x0, y0 - 14, "PEER DASHBOARD", 11, "muted", 600, spacing=1.6)]
    pts = [0.35, 0.42, 0.38, 0.55, 0.62, 0.58, 0.74, 0.8]
    w, h = 156, 96
    d = " ".join(f"{'M' if i == 0 else 'L'}{x0 + i * w / 7:.1f} {y0 + h - v * h:.1f}" for i, v in enumerate(pts))
    out.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="6" fill="none" stroke="{t["hair"]}"/>')
    out.append(f'<path d="{d}" fill="none" stroke="{t["accent"]}" stroke-width="2"/>')
    py = y0 + h - 0.6 * h
    out.append(f'<line x1="{x0}" y1="{py:.1f}" x2="{x0 + w}" y2="{py:.1f}" stroke="{t["muted"]}" stroke-dasharray="3 4"/>')
    out.append(text(t, x0 + w - 6, py - 6, "peers", 10, "muted", anchor="end"))
    out.append(f'<circle cx="{x0 + w:.1f}" cy="{y0 + h - pts[-1] * h:.1f}" r="4" fill="{t["panel"]}" stroke="{t["accent"]}" stroke-width="2"/>')
    out.append(text(t, x0, y0 + h + 22, "you", 11, "soft"))
    out.append(f'<line x1="{x0 + 30}" y1="{y0 + h + 18}" x2="{x0 + 52}" y2="{y0 + h + 18}" stroke="{t["accent"]}" stroke-width="2"/>')
    out.append(text(t, x0 + 64, y0 + h + 22, "peer median", 11, "soft"))
    out.append(f'<line x1="{x0 + 132}" y1="{y0 + h + 18}" x2="{x0 + 154}" y2="{y0 + h + 18}" stroke="{t["muted"]}" stroke-dasharray="3 4"/>')
    return "".join(out)


# ---------------------------------------------------------------- cards

def hero(t):
    w, h = 1200, 320
    x = 40
    body = [
        numeral(t, x - 4, 152, "01", 140),
        title(t, x, 184, "Match3 ", "Lab", 44),
        text(t, x, 222, "A match-3 workbench, not a match-3 game: an engine-independent C# rules core, a level", 15),
        text(t, x, 244, "format you can read in a diff, Unity editor windows, and a bot simulator that tells a designer", 15),
        text(t, x, 266, "how hard a level is before anyone plays it. 12,000 games in about five seconds.", 15),
        text(t, x, 296, "C#  ·  UNITY 6  ·  .NET  ·  xUNIT  ·  WEBGL", 11, "muted", 600, spacing=1.6),
        f'<line x1="740" y1="40" x2="740" y2="280" stroke="{t["hair"]}"/>',
        curve(t, 790, 66, 300, 140),
    ]
    return frame(t, w, h, "".join(body), "Match3 Lab: C# match-3 rules core, level format, editor tools and a bot simulator; difficulty curve measured with 1000 bot games per level")


def card(t, n, first, last, lines, tags, picto, label):
    w, h = 590, 300
    return frame(t, w, h, card_body(t, n, first, last, lines, tags, w) + picto(t, w - 230 + 32, 66), label)


CARDS = {
    "match3-lab": hero,
    "tmp-glyph-audit": lambda t: card(
        t, "03", "TMP Glyph ", "Audit",
        ["Finds every TextMeshPro text your fonts cannot draw:", "scenes, prefabs and runtime text files, through TMP's", "real fallback chain. Editor window + CI exit codes."],
        "UNITY PACKAGE  ·  C#  ·  CI", glyph_tiles,
        "TMP Glyph Audit: Unity package that finds every TextMeshPro text the fonts cannot draw"),
    "turkish-rag-eval": lambda t: card(
        t, "02", "Turkish ", "RAG Eval",
        ["Which parts of a RAG pipeline earn their cost in", "Turkish? 3 chunkers × 4 retrievers on a hand-labelled", "gold set. A 5-char prefix stemmer lifts nDCG 23–29%."],
        "PYTHON  ·  RAG  ·  IR EVALUATION", bars,
        "Turkish RAG Eval: 12 retrieval configurations measured on a hand-labelled Turkish gold set"),
    "bilim-dedektifi": lambda t: card(
        t, "04", "Bilim ", "Dedektifi",
        ["A short educational mystery told through a detective", "investigating a suspicious death. Team course", "project at Hacettepe; free on itch.io."],
        "UNITY  ·  TEAM PROJECT  ·  ITCH.IO", magnifier,
        "Bilim Dedektifi: educational detective game, free on itch.io"),
    "code-enigma": lambda t: card(
        t, "05", "Code-", "Enigma",
        ["Maths-first academic progress platform, built with", "İlkhan Arda Akmaca. I built the dashboard, the peer", "comparison markers, the filter and settings controls."],
        "REACT 19  ·  VITE  ·  TAILWIND 4  ·  GSAP", dashboard,
        "Code-Enigma: React 19 academic progress platform"),
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for slug, render in CARDS.items():
        for name, theme in THEMES.items():
            path = OUT / f"card-{slug}-{name}.svg"
            path.write_text(render(theme), encoding="utf-8")
            print("wrote", path.name, path.stat().st_size)
