"""Checks for the profile builders:  python scripts/test_profile.py"""
from pathlib import Path

import player
import profile as p

ROOT = Path(__file__).resolve().parent.parent


def pr(repo):
    return {"repository": {"nameWithOwner": repo}}


MERGED = [pr("embeddings-benchmark/mteb"), pr("embeddings-benchmark/mteb"), pr("HKUDS/LightRAG"),
          pr("mdn/content"), pr("radzenhq/radzen-blazor")]


def main():
    merged, open_ = {"issueCount": 5, "nodes": MERGED}, {"issueCount": 1}

    # the line reports the true totals and names the featured projects, busiest first
    summary = p.oss_summary(merged, open_)
    assert summary == ("**5 pull requests merged** into 4 projects I don't own, "
                       "among them mteb and LightRAG. 1 more in review."), summary

    # no featured merges and nothing open: no "among them", no review count
    bare = p.oss_summary({"issueCount": 1, "nodes": [pr("mdn/content")]}, {"issueCount": 0})
    assert bare == "**1 pull request merged** into 1 project I don't own.", bare

    # only the summary block is rewritten; the boss fight block next to it is left alone
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    new = p.replace_between(readme, "summary", "X")
    assert "<!-- summary:start -->\nX\n<!-- summary:end -->" in new
    cut = lambda t: t.split("<!-- summary:start -->")[0] + t.split("<!-- summary:end -->")[1]
    assert cut(new) == cut(readme)

    # each marker block in the README is present exactly once, so the Actions can fill them
    for name in ("summary", "boss"):
        assert readme.count(f"<!-- {name}:start -->") == 1 and readme.count(f"<!-- {name}:end -->") == 1, name
    # the header banner opens the README, then one plain line on who I am and what I'm looking for
    first, second = readme.split("\n\n", 2)[:2]
    assert first.startswith('<p align="center"><img src="assets/hero.svg'), readme[:60]
    assert (ROOT / "assets" / "hero.svg").is_file()
    assert "Hacettepe" in second and "June 2027" in second and "Europe and Turkey" in second, second
    # projects and the open-source line come before the game; its heading is the players' landing anchor
    assert readme.count("\n## Duel: Soundwave vs Shockwave\n") == 1
    duel = readme.index("## Duel: Soundwave vs Shockwave")
    assert readme.index("<!-- summary:end -->") < duel and readme.index("**Projects**") < duel
    # hero.svg already carries the name, so no second name heading
    assert not readme.startswith("# ") and "\n# " not in readme

    # the player card is committed as drawn
    svg = (ROOT / "assets" / "player.svg").read_text(encoding="utf-8")
    assert svg == player.render(), "assets/player.svg is stale: run python scripts/player.py"
    assert 'src="assets/player.svg"' in readme
    # what the card says is also under it as plain text, so search can read it
    under = readme.split('src="assets/player.svg"')[1]
    for fact in ("Barko Elektronik", "Jul-Aug 2026", "Open WebUI + LDAP", "Oracle to Power BI",
                 "FastAPI + Docker", "Unity and C#", "Python", "C++20"):
        assert fact in under, fact

    print("ok")


if __name__ == "__main__":
    main()
