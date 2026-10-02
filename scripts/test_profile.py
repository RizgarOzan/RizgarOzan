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

    # the copy says only retrieval-trained dense models beat prefix BM25: the multilingual
    # paraphrase model (MiniLM) must sit below it and the Turkish retrieval model above it.
    # (e5-small/base, also retrieval-trained, beat it too, so "only ... Turkish" was false.)
    rag = dict(cards.RAG)
    assert rag["dense (multilingual)"] < rag["BM25 + 5-char prefix"] < rag["dense (Turkish model)"], rag
    assert "only dense models trained for retrieval beat it" in svg
    assert "trained for Turkish" not in svg


def main():
    check_hero_numbers()

    merged, open_ = {"issueCount": 5, "nodes": MERGED}, {"issueCount": 1, "nodes": OPEN}
    out = p.oss_table(merged, open_)

    # only the featured repos get a row of their own, newest merge first
    assert out.count("| 🟣 merged |") == 2, out
    assert out.index("mteb") < out.index("LightRAG"), out
    for hidden in ("mdn/content", "radzen-blazor", "browser-compat-data"):
        assert f"]({hidden}" not in out and f"/{hidden}/pull" not in out, hidden

    # the rest are counted, with their projects named
    assert "3 more merged pull requests" in out, out
    for owner in ("mdn", "radzenhq"):
        assert owner in out.rsplit("\n", 1)[-1], out

    # one project cannot take the whole table: the 4th kornia merge yields to the older LightRAG one
    busy = [pr("kornia/kornia", n, f"2026-09-{10 + n:02d}T00:00:00Z") for n in range(1, 5)] + MERGED
    spread = p.oss_table({"issueCount": 9, "nodes": busy}, {"issueCount": 0, "nodes": []})
    assert spread.count("kornia/kornia/pull") == p.PER_PROJECT, spread
    assert "LightRAG" in spread and "mteb" in spread, spread

    # the proof line reports the true totals and names the featured projects, busiest first
    summary = p.oss_summary(merged, open_)
    assert summary.startswith("**5 pull requests merged** into 5 projects I don't own"), summary
    assert "mteb and LightRAG among them" in summary and "1 more in review" in summary, summary
    assert "mdn" not in summary, summary

    # no featured merges at all: no table, just the tail line; the proof line has no "among them"
    only_rest = p.oss_table({"issueCount": 1, "nodes": [pr("mdn/content", 3)]},
                            {"issueCount": 0, "nodes": []})
    assert "| Pull request |" not in only_rest, only_rest
    assert "1 more merged pull request" in only_rest, only_rest
    assert "among" not in p.oss_summary({"issueCount": 1, "nodes": [pr("mdn/content", 3)]},
                                        {"issueCount": 0, "nodes": []})

    # both marker blocks in the README are present exactly once, so the Action can fill them
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in ("summary", "oss"):
        assert readme.count(f"<!-- {name}:start -->") == 1 and readme.count(f"<!-- {name}:end -->") == 1, name

    print("ok")


if __name__ == "__main__":
    main()
