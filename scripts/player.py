"""Draw assets/player.svg, the card under the README boss fight, in the fight's own panel style.

Same frame, colours and monospace text as game/render.js, so the two read as one screen.
    python scripts/player.py
Standard library only.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "player.svg"
FONT = "Consolas, 'DejaVu Sans Mono', Menlo, monospace"
W = 880

ABOUT = [
    "I make games in Unity and C#, and spend as much time on AI",
    "tooling and software. Final-year student at Hacettepe University,",
    "Computer Education & Instructional Technology (2023-2027).",
]
QUEST = ("Software intern, Barko Elektronik", "Jul-Aug 2026")
QUEST_NOTE = "local LLMs · Open WebUI + LDAP · Oracle to Power BI · FastAPI + Docker"
MOVES = [
    ("UNITY · C#", "games, editor tools"),
    ("PYTHON", "retrieval evals, APIs"),
    ("C++20 · WASM", "deterministic sims"),
    ("LLM TOOLING", "local models, RAG"),
    ("DOCKER · POWER BI", "services, dashboards"),
]


def T(x, y, s, size=13, fill="#fff", bold=False, anchor="start", shadow=True):
    """Text with the fight's hard 2px black shadow."""
    a = f'font-family="{FONT}" font-size="{size}"{" font-weight=\"700\"" if bold else ""} text-anchor="{anchor}"'
    s = escape(s)
    back = f'<text x="{x + 2}" y="{y + 2}" {a} fill="#000">{s}</text>' if shadow else ""
    return back + f'<text x="{x}" y="{y}" {a} fill="{fill}">{s}</text>'


def win(x, y, w, h):
    """A command window: drop shadow, blue gradient, white border, dark inner line."""
    return (f'<rect x="{x}" y="{y + 4}" width="{w}" height="{h}" rx="6" fill="#000"/>'
            f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{w - 3}" height="{h - 3}" rx="6" fill="url(#win)" stroke="#e9e9f2" stroke-width="3"/>'
            f'<rect x="{x + 4}" y="{y + 4}" width="{w - 8}" height="{h - 8}" rx="4" fill="none" stroke="#0a0f3a" stroke-width="2"/>')


def render():
    BY, BH = 19, 186
    H = BY + BH + 19
    LX, LW = 19, 500
    RX = LX + LW + 10
    RW = W - 19 - RX
    label = ("Rızgar Ozan, player 1. " + " ".join(ABOUT) + f" Last quest: {QUEST[0]}, {QUEST[1]}: {QUEST_NOTE}. "
             "Moves: " + "; ".join(f"{n}: {h}" for n, h in MOVES) + ".")
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(label, {chr(34): "&quot;"})}">',
         '<defs><linearGradient id="win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22379e"/><stop offset="1" stop-color="#0c154f"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="10" fill="#070a12"/>']

    # left: who's playing
    o.append(win(LX, BY, LW, BH))
    o.append(T(LX + 16, BY + 24, "PLAYER 1", size=12, fill="#f3c623", bold=True))
    o.append(T(LX + LW - 16, BY + 24, "ANKARA", size=12, fill="#b9c3ff", anchor="end"))
    # the cursor from the fight, blinking next to the name
    o.append(f'<polygon points="{LX + 16},{BY + 38} {LX + 16},{BY + 54} {LX + 26},{BY + 46}" fill="#f3c623" stroke="#000" stroke-width="2">'
             '<animate attributeName="opacity" values="1;0" calcMode="discrete" dur="1s" repeatCount="indefinite"/></polygon>')
    o.append(T(LX + 34, BY + 53, "RIZGAR OZAN", size=20, bold=True))
    for i, line in enumerate(ABOUT):
        o.append(T(LX + 16, BY + 80 + i * 17, line, size=12, fill="#e3e7ff", shadow=False))
    o.append(f'<line x1="{LX + 14}" y1="{BY + 128}" x2="{LX + LW - 14}" y2="{BY + 128}" stroke="#3b52c9" stroke-width="2"/>')
    o.append(T(LX + 16, BY + 150, "LAST QUEST", size=12, fill="#f3c623", bold=True))
    o.append(T(LX + 110, BY + 150, QUEST[0], size=13, bold=True))
    o.append(T(LX + LW - 16, BY + 150, QUEST[1], size=12, fill="#b9c3ff", anchor="end"))
    o.append(T(LX + 16, BY + 170, QUEST_NOTE, size=12, fill="#8d97d8", shadow=False))

    # right: what he fights with
    o.append(win(RX, BY, RW, BH))
    o.append(T(RX + 16, BY + 24, "MOVES", size=12, fill="#f3c623", bold=True))
    for i, (name, hint) in enumerate(MOVES):
        y = BY + 48 + i * 22
        o.append(T(RX + 16, y, name, size=13, bold=True) + T(RX + RW - 16, y, hint, size=12, fill="#b9c3ff", anchor="end"))
    o.append(T(RX + 16, BY + 168, "▼ projects below", size=12, fill="#8de0ff", bold=True))
    o.append("</svg>")
    return "\n".join(o) + "\n"


def main():
    OUT.write_text(render(), encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()
