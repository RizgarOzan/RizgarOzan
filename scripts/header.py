"""Render assets/header-{dark,light}.svg.

Text is converted to outlines so the banner looks the same on every machine
(an SVG shown through <img> cannot load web fonts). Needs fontTools and the
Windows fonts Georgia and Segoe UI:  python scripts/header.py
"""
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

from palette import THEMES

FONTS = Path("C:/Windows/Fonts")
OUT = Path(__file__).resolve().parent.parent / "assets"
W, H = 1200, 300


def ntos(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def outline(font_file, text, size, x, y, tracking=0.0):
    """Return (path data, advance width) for `text` with its baseline at y."""
    font = TTFont(FONTS / font_file)
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    pen = SVGPathPen(glyphs, ntos=ntos)
    cursor = 0.0
    for ch in text:
        glyph = glyphs[cmap[ord(ch)]]
        glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, x + cursor, y)))
        cursor += glyph.width * scale + tracking
    return pen.getCommands(), cursor - tracking


# 6 x 4 board; letters are piece shapes, "*" marks the three pieces that match.
BOARD = [
    "cdsdtc",
    "t***ds",
    "sdtcsd",
    "cstdct",
]
TILE, GAP = 40, 12


def piece(kind, cx, cy):
    r = 11
    if kind == "c":
        return f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'
    if kind == "s":
        return f'<rect x="{cx - r + 1}" y="{cy - r + 1}" width="{2 * r - 2}" height="{2 * r - 2}" rx="3"/>'
    if kind == "d":
        return f'<path d="M{cx} {cy - r - 1}L{cx + r + 1} {cy}L{cx} {cy + r + 1}L{cx - r - 1} {cy}Z"/>'
    return f'<path d="M{cx} {cy - r}L{cx + r} {cy + r - 2}L{cx - r} {cy + r - 2}Z"/>'


def board(t, x0, y0):
    cells, match = [], []
    for row, line in enumerate(BOARD):
        for col, kind in enumerate(line):
            x, y = x0 + col * (TILE + GAP), y0 + row * (TILE + GAP)
            cx, cy = x + TILE // 2, y + TILE // 2
            if kind == "*":
                delay = len(match) * 0.18
                match.append(
                    f'<g class="m" style="animation-delay:{delay:.2f}s">'
                    f'<rect x="{x}" y="{y}" width="{TILE}" height="{TILE}" rx="10" fill="{t["accent"]}" fill-opacity=".14" stroke="{t["accent"]}"/>'
                    f'<g fill="{t["accent"]}">{piece("c", cx, cy)}</g></g>'
                )
            else:
                cells.append(
                    f'<rect x="{x}" y="{y}" width="{TILE}" height="{TILE}" rx="10" fill="none" stroke="{t["hair"]}"/>'
                    f'<g fill="none" stroke="{t["faint"]}" stroke-width="1.6">{piece(kind, cx, cy)}</g>'
                )
    return "".join(cells) + "".join(match)


def render(t):
    x = 64
    eyebrow, _ = outline("seguisb.ttf", "AI SYSTEMS & GAME TOOLS PROGRAMMER  ·  PYTHON / C#  ·  ANKARA", 14, x, 92, tracking=2.2)
    first, w = outline("georgia.ttf", "Rızgar ", 82, x, 176)
    last, _ = outline("georgiai.ttf", "Ozan", 82, x + w, 176)
    tagline, _ = outline("segoeui.ttf", "I build measurement systems: retrieval evals, and game tools.", 22, x, 228)
    bw = 6 * TILE + 5 * GAP
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Rızgar Ozan — AI systems and game tools programmer">
<style>
.m{{animation:pulse 3.6s ease-in-out infinite}}
@keyframes pulse{{0%,62%,100%{{opacity:1}}72%{{opacity:.25}}84%{{opacity:1}}}}
@media (prefers-reduced-motion:reduce){{.m{{animation:none}}}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{t["panel"]}" stroke="{t["hair"]}"/>
<path fill="{t["accent"]}" d="{eyebrow}"/>
<path fill="{t["ink"]}" d="{first}"/>
<path fill="{t["accent"]}" d="{last}"/>
<path fill="{t["soft"]}" d="{tagline}"/>
{board(t, W - 64 - bw, (H - (4 * TILE + 3 * GAP)) // 2)}
</svg>
"""


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, theme in THEMES.items():
        (OUT / f"header-{name}.svg").write_text(render(theme), encoding="utf-8")
        print("wrote", OUT / f"header-{name}.svg")
