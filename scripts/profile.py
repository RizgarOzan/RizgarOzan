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
# The projects whose merges are worth a row of their own; everything else is counted.
FEATURED = {
    "embeddings-benchmark/mteb",
    "huggingface/sentence-transformers",
    "huggingface/datasets",
    "HKUDS/LightRAG",
    "kornia/kornia",
    "docling-project/docling",
    "CoplayDev/unity-mcp",
    "openupm/openupm",
}
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


def featured(pr):
    return pr["repository"]["nameWithOwner"] in FEATURED


def rest_line(prs):
    """One line for the merges that do not get a row, naming the projects they went to."""
    if not prs:
        return ""
    owners = sorted({p["repository"]["nameWithOwner"].split("/")[0] for p in prs})
    return (f"<sub>…and {len(prs)} more merged pull request{'s' * (len(prs) != 1)} to "
            + ", ".join(owners) + ".</sub>")


def oss_summary(merged, open_):
    """The one-line proof under the intro: totals, and the featured projects with the most merges."""
    merged_prs = merged["nodes"]
    projects = len({p["repository"]["nameWithOwner"] for p in merged_prs})
    counts = {}
    for p in merged_prs:
        if featured(p):
            name = p["repository"]["nameWithOwner"].split("/")[1]
            counts[name] = counts.get(name, 0) + 1
    named = [name for name, _ in sorted(counts.items(), key=lambda kv: -kv[1])[:4]]
    among = ""
    if len(named) > 1:
        among = f" — {', '.join(named[:-1])} and {named[-1]} among them —"
    elif named:
        among = f" — {named[0]} among them —"
    return (f"**{merged['issueCount']} pull requests merged** into {projects} "
            f"project{'s' * (projects != 1)} I don't own{among} with {open_['issueCount']} more in review.")


PER_PROJECT = 3  # rows one project may take, so a busy week in one repo doesn't hide the others


def spread(prs):
    seen, out = {}, []
    for p in prs:
        name = p["repository"]["nameWithOwner"]
        if featured(p) and seen.get(name, 0) < PER_PROJECT:
            seen[name] = seen.get(name, 0) + 1
            out.append(p)
    return out


def oss_table(merged, open_):
    merged_prs = sorted(merged["nodes"], key=lambda p: p["mergedAt"], reverse=True)
    rows = ([row("🟣 merged", p) for p in spread(merged_prs)]
            + [row("🟢 in review", p) for p in spread(open_["nodes"])])
    tail = rest_line([p for p in merged_prs if not featured(p)])
    if not rows:
        return tail
    table = "\n".join(["| | Pull request | Project |", "|---|---|---|", *rows[:5]])
    return "\n\n".join(part for part in [table, tail] if part)


def replace_between(text, name, body):
    return re.sub(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)",
                  lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text, flags=re.S)


def main():
    data = fetch()
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    summary = oss_summary(data["merged"], data["open"])
    text = replace_between(text, "summary", summary)
    text = replace_between(text, "oss", oss_table(data["merged"], data["open"]))
    readme.write_text(text, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
