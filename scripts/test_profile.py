"""Checks for the open-source section builder:  python scripts/test_profile.py"""
import profile as p


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


def main():
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
