<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Rızgar Ozan — AI systems and game tools programmer. I build measurement systems: retrieval evals, and game tools.">
</picture>

<p align="center">
  <a href="https://rizgarozan.github.io">rizgarozan.github.io</a> · <a href="https://www.linkedin.com/in/rizgarozan/">LinkedIn</a> · <a href="https://rizgarozan.itch.io">itch.io</a> · <a href="https://huggingface.co/RizgarOzan">Hugging Face</a> · <a href="mailto:rizgarozan7@gmail.com">rizgarozan7@gmail.com</a>
</p>

I build **measurement systems**: retrieval evaluations that say which part of a RAG pipeline
earns its cost, and game tools that score a level or catch a broken font before anyone ships it.
Final-year Computer Education & Instructional Technology student at Hacettepe University, Ankara.

<!-- summary:start -->
**63 pull requests merged** into 19 projects I don't own — mteb, kornia, LightRAG and unity-mcp among them — with 31 more in review.
<!-- summary:end -->

## Selected work

Five projects, in the order I'd show them to you. Every number on a card is copied from the
project's own committed results.

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

<sub>Turkish RAG Eval: 58 hand-labelled queries, <a href="https://huggingface.co/datasets/RizgarOzan/turkish-rag-eval">published as a dataset on Hugging Face</a>; differences under 0.05 nDCG are noise, and the README says so.
Match3 Lab <a href="https://rizgarozan.github.io/match3-lab/">plays in the browser</a> and ships 50 tests and a decision record for every rule. TMP Glyph Audit: 24 xUnit + 5 EditMode tests, <a href="https://openupm.com/packages/com.rizgarozan.tmp-glyph-audit/">on OpenUPM</a>.</sub>

## Open source

Fixes sent back to the retrieval and Unity tooling I use. The AI and Unity projects get a row each,
the rest are counted; [a workflow](.github/workflows/profile.yml) refreshes this every week.

<!-- oss:start -->
| | Pull request | Project |
|---|---|---|
| 🟣 merged | [docs(reference): add run_tests and get_test_job examples](https://github.com/CoplayDev/unity-mcp/pull/1400) | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) · ★ 14.7k |
| 🟣 merged | [model: add Linkup-Platform/linkup-sparseup-embed-v1](https://github.com/embeddings-benchmark/mteb/pull/5547) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix: read task modalities in result filtering](https://github.com/embeddings-benchmark/mteb/pull/5550) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [docs(reference): add unity_docs and unity_reflect examples](https://github.com/CoplayDev/unity-mcp/pull/1401) | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) · ★ 14.7k |
| 🟣 merged | [fix(augmentation): place RandomGaussianIllumination's peak at center * L - 0.5](https://github.com/kornia/kornia/pull/4990) | [kornia/kornia](https://github.com/kornia/kornia) · ★ 11.4k |
| 🟣 merged | [docs(geometry): list the scaled large-root quartic defect (#4954) and pin it](https://github.com/kornia/kornia/pull/4989) | [kornia/kornia](https://github.com/kornia/kornia) · ★ 11.4k |
| 🟣 merged | [fix(geometry): make solve_quartic's cubic fallback tolerance relative to the row](https://github.com/kornia/kornia/pull/4921) | [kornia/kornia](https://github.com/kornia/kornia) · ★ 11.4k |
| 🟣 merged | [fix: don't place pair classification thresholds between tied scores](https://github.com/embeddings-benchmark/mteb/pull/5465) | [embeddings-benchmark/mteb](https://github.com/embeddings-benchmark/mteb) · ★ 3.4k |
| 🟣 merged | [fix(ebcdic): keep fixed-point notation for scaled numbers](https://github.com/docling-project/docling/pull/4296) | [docling-project/docling](https://github.com/docling-project/docling) · ★ 68.3k |
| 🟣 merged | [fix(afp): follow PTOCA control sequence chaining](https://github.com/docling-project/docling/pull/4297) | [docling-project/docling](https://github.com/docling-project/docling) · ★ 68.3k |

<sub>…and 24 more merged pull requests to Effect-TS, ManimCommunity, SchemaStore, TheAlgorithms, e18e, embeddings-benchmark, mdn, modelscope, pylint-dev, radzenhq, umbraco.</sub>
<!-- oss:end -->

## Now · October 2026

- Growing Turkish RAG Eval from 58 hand-labelled queries to a 300-query, six-model benchmark, with the dataset on Hugging Face.
- A few pull requests a day to the retrieval and Unity tooling in the table above.
- Graduating in June 2027; open to internships and new-grad roles in applied AI and game engineering.

<sub>Header and cards are SVGs rendered by <code>scripts/</code> in the site's palette; the cards' text is outlined so they look the same on every machine.</sub>
