"""Refresh the open-source table in README.md.

Runs weekly in .github/workflows/profile.yml. Locally:
    GITHUB_TOKEN=$(gh auth token) python scripts/profile.py
Standard library only.
"""
import json
import os
import re
import urllib.request
from pathlib import Path

LOGIN = "RizgarOzan"
ROOT = Path(__file__).resolve().parent.parent
PRS = f"author:{LOGIN} type:pr -user:{LOGIN}"
PR_FIELDS = "... on PullRequest { title url createdAt mergedAt repository { nameWithOwner url stargazerCount } }"
QUERY = f"""
query {{
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
        data=json.dumps({"query": QUERY}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}"},
    )
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    if "errors" in body:
        raise SystemExit(f"GraphQL errors: {body['errors']}")
    return body["data"]


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
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    table = oss_table(data["merged"], data["open"])
    text = re.sub(r"(<!-- oss:start -->).*?(<!-- oss:end -->)",
                  lambda m: f"{m.group(1)}\n{table}\n{m.group(2)}", text, flags=re.S)
    readme.write_text(text, encoding="utf-8")
    print(table.splitlines()[0])


if __name__ == "__main__":
    main()
