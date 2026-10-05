<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Rızgar Ozan, AI systems and game tools programmer. I build games, tools and AI systems.">
</picture>

<p align="center">
  <a href="https://rizgarozan.github.io">rizgarozan.github.io</a> · <a href="https://www.linkedin.com/in/rizgarozan/">LinkedIn</a> · <a href="https://rizgarozan.itch.io">itch.io</a> · <a href="https://huggingface.co/RizgarOzan">Hugging Face</a> · <a href="mailto:rizgarozan7@gmail.com">rizgarozan7@gmail.com</a>
</p>

I build games, tools and AI systems: retrieval evaluations that say which part of a RAG pipeline
earns its cost, and game tools that score a level or catch a broken font before anyone ships it.
Final-year Computer Education & Instructional Technology student at Hacettepe University, Ankara.

<!-- summary:start -->
**80 pull requests merged** into 24 projects I don't own — mteb, kornia, unity-mcp and docling among them — with 30 more in review.
<!-- summary:end -->

<a href="https://rizgarozan.github.io"><img src="assets/site.jpg" width="100%" alt="rizgarozan.github.io: a moonlit field where each sword standing in the ground is one of my projects; scroll down into the smithy for what I'm working on now."></a>

## Selected work

<a href="https://github.com/RizgarOzan/turkish-rag-eval">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-turkish-rag-eval-dark.svg">
  <img src="assets/card-turkish-rag-eval-light.svg" width="100%" alt="01 Turkish RAG Eval — 3 chunkers by 4 retrievers on a hand-labelled Turkish gold set. Best nDCG@10 per retriever: BM25 0.41, BM25 + 5-char prefix 0.51, hybrid RRF 0.61, dense (multilingual) 0.50, dense (Turkish model) 0.78.">
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

## Open source

Fixes sent back to the retrieval and Unity tooling I use, refreshed weekly by [a workflow](.github/workflows/profile.yml).

<!-- oss:start -->
| | Pull request | Project |
|---|---|---|
| 🟣 merged | [model: add KURE-Reranker-base and KURE-Reranker-nano](https://github.com/embeddings-benchmark/mteb/pull/5574) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: read model files as UTF-8 in extract_model_names.py](https://github.com/embeddings-benchmark/mteb/pull/5575) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: skip top_ranked ids missing from queries in cross-encoder search](https://github.com/embeddings-benchmark/mteb/pull/5573) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: find native m_ fields when setting built-in component properties](https://github.com/CoplayDev/unity-mcp/pull/1419) | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) · ★ 14.7k |
| 🟣 merged | [fix: parse numeric tool parameters with the invariant culture](https://github.com/CoplayDev/unity-mcp/pull/1416) | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) · ★ 14.7k |

<sub>…and 32 more merged pull requests to Effect-TS, ManimCommunity, SchemaStore, TheAlgorithms, atlassian-api, chigwell, e18e, embeddings-benchmark, mdn, modelscope, obsidian-full-calendar-remastered, pcottle, pylint-dev, radzenhq, umbraco, yairm210.</sub>
<!-- oss:end -->

## Now · October 2026

- Turkish RAG Eval is at 300 queries (58 hand-labelled, 242 LLM-drafted and double-labelled) across five models, with the dataset on Hugging Face; next is human review of the drafts and an MTEB task.
- Graduating in June 2027; open to internships and new-grad roles in applied AI and game engineering.
