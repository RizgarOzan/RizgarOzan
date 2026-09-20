<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Rızgar Ozan — AI systems and game tools programmer. I build measurement systems: retrieval evals, and game tools.">
</picture>

<p align="center">
  <a href="https://rizgarozan.github.io"><img src="https://img.shields.io/badge/website-rizgarozan.github.io-D6C29A?style=flat-square&labelColor=121114" alt="Website"></a>
  <a href="https://www.linkedin.com/in/rizgarozan/"><img src="https://img.shields.io/badge/linkedin-rizgarozan-D6C29A?style=flat-square&labelColor=121114" alt="LinkedIn"></a>
  <a href="https://rizgarozan.itch.io"><img src="https://img.shields.io/badge/itch.io-rizgarozan-D6C29A?style=flat-square&labelColor=121114" alt="itch.io"></a>
  <a href="mailto:rizgarozan7@gmail.com"><img src="https://img.shields.io/badge/email-rizgarozan7%40gmail.com-D6C29A?style=flat-square&labelColor=121114" alt="Email"></a>
</p>

I build **measurement systems**: retrieval evaluations that say which part of a RAG pipeline
earns its cost, and game tools that score a level or catch a broken font before anyone ships it.
Final-year Computer Education & Instructional Technology student at Hacettepe University.

## Selected work

Five projects, in the order I'd show them to you. Every number on a card is copied from the
project's own committed results.

<a href="https://github.com/RizgarOzan/turkish-rag-eval">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-turkish-rag-eval-dark.svg">
  <img src="assets/card-turkish-rag-eval-light.svg" width="100%" alt="01 Turkish RAG Eval — 3 chunkers by 4 retrievers on a hand-labelled Turkish gold set. Best nDCG@10 per retriever: BM25 0.41, BM25 with 5-character prefix 0.51, dense 0.50, hybrid RRF 0.61.">
</picture>
</a>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/RizgarOzan/match3-lab">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-match3-lab-dark.svg">
  <img src="assets/card-match3-lab-light.svg" width="100%" alt="02 Match3 Lab — C# match-3 rules core, readable level format, Unity editor tools and a bot simulator. The greedy bot's win rate falls from 100% on level 1 to 50% on level 6; the random bot from 70% to 3%. 1000 games per level.">
</picture>
</a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/RizgarOzan/tmp-glyph-audit">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-tmp-glyph-audit-dark.svg">
  <img src="assets/card-tmp-glyph-audit-light.svg" width="100%" alt="03 TMP Glyph Audit — Unity package that finds every TextMeshPro text the fonts cannot draw, through TMP's real fallback chain. Editor window plus CI exit codes.">
</picture>
</a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://rizgarozan.itch.io/bilim-dedektifi">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-bilim-dedektifi-dark.svg">
  <img src="assets/card-bilim-dedektifi-light.svg" width="100%" alt="04 Bilim Dedektifi — short educational mystery game, team course project at Hacettepe, free on itch.io.">
</picture>
</a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/ilkhanarda/Code-Enigma">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-code-enigma-dark.svg">
  <img src="assets/card-code-enigma-light.svg" width="100%" alt="05 Code-Enigma — React 19 academic progress platform built with İlkhan Arda Akmaca; I built the dashboard, peer comparison markers and the filter and settings controls.">
</picture>
</a>
</td>
</tr>
</table>

<sub>Turkish RAG Eval: 58 hand-labelled queries; differences under 0.05 nDCG are noise, and the README says so.
Match3 Lab <a href="https://rizgarozan.github.io/match3-lab/">plays in the browser</a> and ships 50 tests and a decision record for every rule. TMP Glyph Audit: 24 xUnit + 5 EditMode tests, <a href="https://openupm.com/packages/com.rizgarozan.tmp-glyph-audit/">on OpenUPM</a>.</sub>

## Open source

Pull requests to projects I don't own — the AI and Unity ones listed below, the rest counted.
Refreshed every week by [a workflow](.github/workflows/profile.yml).

<!-- oss:start -->
**28 merged** across 9 projects · **21 in review**

| | Pull request | Project |
|---|---|---|
| 🟣 merged | [fix: warm the benchmark-schema cache key the route actually uses](https://github.com/embeddings-benchmark/mteb/pull/5494) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [docs(skill): say where to look when a tool is not in the tool list](https://github.com/CoplayDev/unity-mcp/pull/1406) | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) · ★ 14.4k |
| 🟣 merged | [fix: pass num_proc to every dataloader created during evaluation](https://github.com/embeddings-benchmark/mteb/pull/5489) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: apply scripts filter in TaskResult.get_score](https://github.com/embeddings-benchmark/mteb/pull/5490) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: accept ISO 639-3 codes in get_model_metas(languages=...)](https://github.com/embeddings-benchmark/mteb/pull/5484) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: accept language-script and programming-language codes in filter_tasks](https://github.com/embeddings-benchmark/mteb/pull/5483) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: allow validate_and_filter in load_results without tasks](https://github.com/embeddings-benchmark/mteb/pull/5480) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: do not mutate eval_splits in calculate_descriptive_statistics](https://github.com/embeddings-benchmark/mteb/pull/5481) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix(markdown): treat an escaped pipe as cell text, not a column separator](https://github.com/HKUDS/LightRAG/pull/3976) | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) · ★ 39.8k |
| 🟣 merged | [fix(parser): emit LaTeX-valid delimiters for Word equations](https://github.com/HKUDS/LightRAG/pull/3977) | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) · ★ 39.8k |

<sub>…and 11 more merged pull requests to TheAlgorithms, mdn, radzenhq.</sub>
<!-- oss:end -->

## Toolbox

![Unity](https://img.shields.io/badge/Unity-121114?style=flat-square&logo=unity&logoColor=D6C29A)
![C# / .NET](https://img.shields.io/badge/C%23_%2F_.NET-121114?style=flat-square&logo=dotnet&logoColor=D6C29A)
![Python](https://img.shields.io/badge/Python-121114?style=flat-square&logo=python&logoColor=D6C29A)
![React](https://img.shields.io/badge/React-121114?style=flat-square&logo=react&logoColor=D6C29A)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-121114?style=flat-square&logo=githubactions&logoColor=D6C29A)
![Git](https://img.shields.io/badge/Git-121114?style=flat-square&logo=git&logoColor=D6C29A)

<sub>Header and cards are SVGs rendered by <code>scripts/</code> in the site's palette; the cards' text is outlined so they look the same on every machine.</sub>
