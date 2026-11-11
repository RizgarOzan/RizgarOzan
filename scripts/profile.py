"""Refresh the open-source line in README.md (the summary block under the boss fight).

Runs daily in .github/workflows/profile.yml. Locally:
    GITHUB_TOKEN=$(gh auth token) python scripts/profile.py
Standard library only.
"""
import json
import os
import re
import urllib.request
from pathlib import Path

LOGIN = "RizgarOzan"
# The projects worth naming in the summary line; every merge is still counted.
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
PR_FIELDS = "... on PullRequest { repository { nameWithOwner } }"
QUERY = f"""
query($after: String) {{
  merged: search(type: ISSUE, first: 100, after: $after, query: "{PRS} is:merged sort:updated-desc") {{
    issueCount pageInfo {{ hasNextPage endCursor }} nodes {{ {PR_FIELDS} }}
  }}
  open: search(type: ISSUE, first: 1, query: "{PRS} is:open") {{
    issueCount
  }}
}}
"""


def query(after=None):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"after": after}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}"},
    )
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    if "errors" in body:
        raise SystemExit(f"GraphQL errors: {body['errors']}")
    return body["data"]


def fetch():
    """Search returns 100 merges a page; past that the project count fell short."""
    data = query()
    page = data["merged"]["pageInfo"]
    while page["hasNextPage"]:
        more = query(page["endCursor"])["merged"]
        data["merged"]["nodes"] += more["nodes"]
        page = more["pageInfo"]
    return data


def featured(pr):
    return pr["repository"]["nameWithOwner"] in FEATURED


def oss_summary(merged, open_):
    """One line: totals, and the featured projects with the most merges."""
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
        among = f", among them {', '.join(named[:-1])} and {named[-1]}"
    elif named:
        among = f", among them {named[0]}"
    n = merged['issueCount']
    line = (f"**{n} pull request{'s' * (n != 1)} merged** into {projects} "
            f"project{'s' * (projects != 1)} I don't own{among}.")
    if open_["issueCount"]:
        line += f" {open_['issueCount']} more in review."
    return line


def replace_between(text, name, body):
    return re.sub(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)",
                  lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text, flags=re.S)


def main():
    data = fetch()
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    summary = oss_summary(data["merged"], data["open"])
    text = replace_between(text, "summary", summary)
    readme.write_text(text, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
