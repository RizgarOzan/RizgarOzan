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
**106 pull requests merged** into 34 projects I don't own — mteb, kornia, unity-mcp and docling among them — with 27 more in review.
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

Fixes sent back to the retrieval and Unity tooling I use, refreshed daily by [a workflow](.github/workflows/profile.yml).

<!-- oss:start -->
| | Pull request | Project |
|---|---|---|
| 🟣 merged | [fix(augmentation): make auto policies picklable](https://github.com/kornia/kornia/pull/5651) | [kornia/kornia](https://github.com/kornia/kornia) · ★ 11.4k |
| 🟣 merged | [[fix] Warn about every include_positives option that discards the positives](https://github.com/huggingface/sentence-transformers/pull/4053) | [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) · ★ 19.2k |
| 🟣 merged | [[fix] Keep leading dims when binary-quantizing a single embedding](https://github.com/huggingface/sentence-transformers/pull/4061) | [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) · ★ 19.2k |
| 🟣 merged | [fix(pdf): keep failed-page sizes on the conversion, not on the pipeline](https://github.com/docling-project/docling/pull/4486) | [docling-project/docling](https://github.com/docling-project/docling) · ★ 68.7k |
| 🟣 merged | [fix(html): keep description lists with nested divs or inner headings](https://github.com/docling-project/docling/pull/4578) | [docling-project/docling](https://github.com/docling-project/docling) · ★ 68.7k |

<sub>…and 101 more merged pull requests. Merges by project: mteb 18 · kornia 16 · unity-mcp 8 · docling 6 · browser-compat-data 5 · results 4 · LightRAG 4 · module-replacements 3 · telegram-mcp 3 · sentence-transformers 3, and 24 more projects.</sub>
<!-- oss:end -->

## Now · October 2026

- Turkish RAG Eval 0.2.0 is on [PyPI](https://pypi.org/project/turkish-rag-eval/): 300 queries (58 hand-labelled, 242 LLM-drafted and double-labelled) across five models, with the dataset on Hugging Face. The MTEB task is in review ([mteb#5615](https://github.com/embeddings-benchmark/mteb/pull/5615)), and the drafted queries are open for human review as good first issues.
- Graduating in June 2027; open to internships and new-grad roles in applied AI and game engineering.
