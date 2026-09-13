"""Refresh assets/stats-{dark,light}.svg and the open-source table in README.md.

Runs daily in .github/workflows/profile.yml. Locally:
    GITHUB_TOKEN=$(gh auth token) python scripts/profile.py
Standard library only.
"""
import datetime as dt
import json
import os
import re
import urllib.request
from pathlib import Path

from palette import THEMES

LOGIN = "RizgarOzan"
ROOT = Path(__file__).resolve().parent.parent
PRS = f"author:{LOGIN} type:pr -user:{LOGIN}"
PR_FIELDS = "... on PullRequest { title url createdAt mergedAt repository { nameWithOwner url stargazerCount } }"
QUERY = f"""
query($login: String!) {{
  user(login: $login) {{
    contributionsCollection {{
      contributionCalendar {{
        totalContributions
        weeks {{ contributionDays {{ date contributionCount contributionLevel }} }}
      }}
    }}
  }}
  merged: search(type: ISSUE, first: 100, query: "{PRS} is:merged sort:updated-desc") {{
    issueCount nodes {{ {PR_FIELDS} }}
  }}
  open: search(type: ISSUE, first: 20, query: "{PRS} is:open sort:created-desc") {{
    issueCount nodes {{ {PR_FIELDS} }}
  }}
}}
"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}"},
    )
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    if "errors" in body:
        raise SystemExit(f"GraphQL errors: {body['errors']}")
    return body["data"]


def streak(days):
    """Consecutive days with contributions, ending today (or yesterday if today is still empty)."""
    counts = [d["contributionCount"] for d in days]
    if counts and counts[-1] == 0:
        counts.pop()
    n = 0
    for c in reversed(counts):
        if c == 0:
            break
        n += 1
    return n


# ---------------------------------------------------------------- stats card

W, H = 1200, 290
SANS = "'Segoe UI',system-ui,-apple-system,Ubuntu,'Helvetica Neue',sans-serif"
LEVEL = {"NONE": 0, "FIRST_QUARTILE": 0.3, "SECOND_QUARTILE": 0.5, "THIRD_QUARTILE": 0.75, "FOURTH_QUARTILE": 1}
CELL, STEP, WEEKS = 14, 18, 26


def label(t, x, y, text, anchor="start"):
    return (f'<text x="{x}" y="{y}" fill="{t["muted"]}" font-family="{SANS}" font-size="12" '
            f'letter-spacing="1.6" text-anchor="{anchor}">{text}</text>')


def heatmap(t, weeks, x0, y0):
    out, last_month, last_label = [], None, -9
    for col, week in enumerate(weeks):
        month = week["contributionDays"][0]["date"][:7]
        if month != last_month and col - last_label >= 3:
            name = dt.date.fromisoformat(month + "-01").strftime("%b").upper()
            out.append(label(t, x0 + col * STEP, y0 - 12, name))
            last_label = col
        last_month = month
        for day in week["contributionDays"]:
            row = dt.date.fromisoformat(day["date"]).isoweekday() % 7  # Sunday first, like GitHub
            level = LEVEL[day["contributionLevel"]]
            fill = (f'fill="{t["accent"]}" fill-opacity="{level}"' if level
                    else f'fill="none" stroke="{t["hair"]}"')
            out.append(f'<rect x="{x0 + col * STEP}" y="{y0 + row * STEP}" width="{CELL}" height="{CELL}" rx="3" {fill}/>')
    return "".join(out)


def card(t, metrics, weeks):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="GitHub activity: {", ".join(f"{v} {k.lower()}" for k, v in metrics)}">',
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{t["panel"]}" stroke="{t["hair"]}"/>',
        f'<text x="64" y="64" fill="{t["accent"]}" font-family="{SANS}" font-size="13" font-weight="600" '
        f'letter-spacing="2.2">ACTIVITY</text>',
    ]
    for i, (name, value) in enumerate(metrics):
        x, y = 64 + (i % 2) * 260, 142 + (i // 2) * 92
        parts.append(f'<text x="{x}" y="{y}" fill="{t["ink"]}" font-family="{SANS}" font-size="50" font-weight="300">{value:,}</text>')
        parts.append(label(t, x, y + 26, name))
    hx = W - 64 - (WEEKS * STEP - (STEP - CELL))
    parts.append(heatmap(t, weeks, hx, 96))
    legend_x = W - 64 - 52 - 5 * STEP + (STEP - CELL)
    parts.append(label(t, legend_x - 10, 254, "LESS", anchor="end"))
    parts.append(label(t, W - 64, 254, "MORE", anchor="end"))
    for i, level in enumerate([0, 0.3, 0.5, 0.75, 1]):
        fill = f'fill="{t["accent"]}" fill-opacity="{level}"' if level else f'fill="none" stroke="{t["hair"]}"'
        parts.append(f'<rect x="{legend_x + i * STEP}" y="243" width="{CELL}" height="{CELL}" rx="3" {fill}/>')
    parts.append("</svg>\n")
    return "\n".join(parts)


# ---------------------------------------------------------------- README table

def stars(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def row(status, pr):
    repo = pr["repository"]
    title = pr["title"].replace("|", "\\|")
    return f"| {status} | [{title}]({pr['url']}) | [{repo['nameWithOwner']}]({repo['url']}) · ★ {stars(repo['stargazerCount'])} |"


def oss_table(merged, open_):
    merged_prs = sorted(merged["nodes"], key=lambda p: p["mergedAt"], reverse=True)
    projects = len({p["repository"]["nameWithOwner"] for p in merged_prs})
    summary = f"**{open_['issueCount']} in review**"
    if merged["issueCount"]:
        summary = (f"**{merged['issueCount']} merged** across {projects} project{'s' * (projects != 1)} · "
                   + summary)
    rows = [row("🟣 merged", p) for p in merged_prs] + [row("🟢 in review", p) for p in open_["nodes"]]
    if not rows:
        return summary
    return "\n".join([summary, "", "| | Pull request | Project |", "|---|---|---|", *rows[:10]])


def main():
    data = fetch()
    calendar = data["user"]["contributionsCollection"]["contributionCalendar"]
    days = [d for w in calendar["weeks"] for d in w["contributionDays"]]
    metrics = [
        ("CONTRIBUTIONS · 12 MONTHS", calendar["totalContributions"]),
        ("DAY STREAK", streak(days)),
        ("MERGED OPEN-SOURCE PRS", data["merged"]["issueCount"]),
        ("PRS IN REVIEW", data["open"]["issueCount"]),
    ]
    for name, theme in THEMES.items():
        (ROOT / "assets" / f"stats-{name}.svg").write_text(
            card(theme, metrics, calendar["weeks"][-WEEKS:]), encoding="utf-8")

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    table = oss_table(data["merged"], data["open"])
    text = re.sub(r"(<!-- oss:start -->).*?(<!-- oss:end -->)",
                  lambda m: f"{m.group(1)}\n{table}\n{m.group(2)}", text, flags=re.S)
    readme.write_text(text, encoding="utf-8")
    print(dict(metrics))


if __name__ == "__main__":
    main()
