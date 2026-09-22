"""Checks for the profile builders:  python scripts/test_profile.py"""
from pathlib import Path

import cards
import profile as p
from palette import THEMES

ROOT = Path(__file__).resolve().parent.parent


def pr(repo, number, merged="2026-09-01T00:00:00Z", stars=1000):
    return {"title": f"fix {number}", "url": f"https://github.com/{repo}/pull/{number}",
            "createdAt": merged, "mergedAt": merged,
            "repository": {"nameWithOwner": repo, "url": f"https://github.com/{repo}",
                           "stargazerCount": stars}}


MERGED = [
    pr("embeddings-benchmark/mteb", 1, "2026-09-05T00:00:00Z"),
    pr("HKUDS/LightRAG", 2, "2026-09-04T00:00:00Z"),
    pr("mdn/content", 3, "2026-09-03T00:00:00Z"),
    pr("radzenhq/radzen-blazor", 4, "2026-09-02T00:00:00Z"),
    pr("mdn/browser-compat-data", 5, "2026-09-01T00:00:00Z"),
]
OPEN = [pr("huggingface/sentence-transformers", 6)]


def check_hero_numbers():
    """The hero card's numbers are drawn once and quoted twice — keep the three in step."""
    svg = cards.hero(THEMES["light"])
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for lab, v in cards.RAG:
        assert f">{v:.2f}<" in svg, lab                 # drawn at the end of its bar
        assert f"{lab} {v:.2f}" in svg, lab             # named in the aria label
        assert f"{lab} {v:.2f}" in readme, lab          # and in the README alt text

    # the card's copy says a Turkish retrieval model is the only dense winner
    assert max(cards.RAG, key=lambda r: r[1])[0].startswith("dense"), cards.RAG


def main():
    check_hero_numbers()

    out = p.oss_table({"issueCount": 5, "nodes": MERGED}, {"issueCount": 1, "nodes": OPEN})

    # only the featured repos get a row of their own, newest merge first
    assert out.count("| 🟣 merged |") == 2, out
    assert out.index("mteb") < out.index("LightRAG"), out
    for hidden in ("mdn/content", "radzen-blazor", "browser-compat-data"):
        assert f"]({hidden}" not in out and f"/{hidden}/pull" not in out, hidden

    # the rest are counted, with their projects named
    assert "3 more merged pull requests" in out, out
    for owner in ("mdn", "radzenhq"):
        assert owner in out.rsplit("\n", 1)[-1], out

    # summary still reports the true totals
    assert "**5 merged**" in out and "**1 in review**" in out, out

    # no featured merges at all: no table, just the tail line
    only_rest = p.oss_table({"issueCount": 1, "nodes": [pr("mdn/content", 3)]},
                            {"issueCount": 0, "nodes": []})
    assert "| Pull request |" not in only_rest, only_rest
    assert "1 more merged pull request" in only_rest, only_rest

    print("ok")


if __name__ == "__main__":
    main()
