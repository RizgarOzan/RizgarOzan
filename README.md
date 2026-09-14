<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" width="100%" alt="Rızgar Ozan — game and tools programmer. Systems behind games, and the tools that prove they work.">
</picture>

<p align="center">
  <a href="https://rizgarozan.github.io"><img src="https://img.shields.io/badge/website-rizgarozan.github.io-D6C29A?style=flat-square&labelColor=121114" alt="Website"></a>
  <a href="https://www.linkedin.com/in/rizgarozan/"><img src="https://img.shields.io/badge/linkedin-rizgarozan-D6C29A?style=flat-square&labelColor=121114" alt="LinkedIn"></a>
  <a href="https://rizgarozan.itch.io"><img src="https://img.shields.io/badge/itch.io-rizgarozan-D6C29A?style=flat-square&labelColor=121114" alt="itch.io"></a>
  <a href="mailto:rizgarozan7@gmail.com"><img src="https://img.shields.io/badge/email-rizgarozan7%40gmail.com-D6C29A?style=flat-square&labelColor=121114" alt="Email"></a>
</p>

I build **systems and the tools around them**: rules engines you can test without an engine
running, editors that show a designer what a change will cost, and simulators that measure
instead of guess. Final-year Computer Education & Instructional Technology student at
Hacettepe University, so I also care about the moment a game teaches something and the player
doesn't notice.

## Selected work

Five projects, in the order I'd show them to you. Every number on a card is copied from the
project's own committed results.

<a href="https://github.com/RizgarOzan/match3-lab">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-match3-lab-dark.svg">
  <img src="assets/card-match3-lab-light.svg" width="100%" alt="01 Match3 Lab — C# match-3 rules core, readable level format, Unity editor tools and a bot simulator. Difficulty curve: greedy-bot win rate falls from 100% on level 1 to 50% on level 6; random bot from 70% to 3%. 1000 games per level.">
</picture>
</a>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/RizgarOzan/turkish-rag-eval">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/card-turkish-rag-eval-dark.svg">
  <img src="assets/card-turkish-rag-eval-light.svg" width="100%" alt="02 Turkish RAG Eval — 3 chunkers × 4 retrievers on a hand-labelled Turkish gold set. Best nDCG@10 per retriever: BM25 0.41, BM25 with 5-character prefix 0.51, dense 0.50, hybrid RRF 0.61.">
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

<sub>Match3 Lab ships a WebGL build, 39 core tests and 2 play-mode tests, and a decision record for every rule.
Turkish RAG Eval: 58 hand-labelled queries; differences under 0.05 nDCG are noise, and the README says so. TMP Glyph Audit: 18 xUnit + 4 EditMode tests.</sub>

## Open source

Pull requests to projects I don't own. Refreshed every week by
[a workflow](.github/workflows/profile.yml).

<!-- oss:start -->
**4 merged** across 3 projects · **7 in review**

| | Pull request | Project |
|---|---|---|
| 🟣 merged | [Fix implied second keyword for single-keyword position-area values](https://github.com/mdn/content/pull/45689) | [mdn/content](https://github.com/mdn/content) · ★ 11k |
| 🟣 merged | [Keep the DropZone can-drop class while dragging over its items](https://github.com/radzenhq/radzen-blazor/pull/2722) | [radzenhq/radzen-blazor](https://github.com/radzenhq/radzen-blazor) · ★ 4.3k |
| 🟣 merged | [fix(docx): record Roman and ideographTraditional counts past their domain](https://github.com/HKUDS/LightRAG/pull/3940) | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) · ★ 39.6k |
| 🟣 merged | [Hide the decorative dropdown trigger icon from screen readers](https://github.com/radzenhq/radzen-blazor/pull/2721) | [radzenhq/radzen-blazor](https://github.com/radzenhq/radzen-blazor) · ★ 4.3k |
| 🟢 in review | [fix(auth): strip whitespace around AUTH_ACCOUNTS entries](https://github.com/HKUDS/LightRAG/pull/3944) | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) · ★ 39.6k |
| 🟢 in review | [Fix compiled models with losses that require media counts in the trainer](https://github.com/huggingface/sentence-transformers/pull/4015) | [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) · ★ 19.1k |
| 🟢 in review | [Chrome 144 supports Temporal constructors](https://github.com/mdn/browser-compat-data/pull/30513) | [mdn/browser-compat-data](https://github.com/mdn/browser-compat-data) · ★ 5.7k |
| 🟢 in review | [Fix: C# project discovery ignores configured ignore patterns](https://github.com/oraios/serena/pull/2033) | [oraios/serena](https://github.com/oraios/serena) · ★ 29.3k |
| 🟢 in review | [Node.js 24 supports SuppressedError](https://github.com/mdn/browser-compat-data/pull/30511) | [mdn/browser-compat-data](https://github.com/mdn/browser-compat-data) · ★ 5.7k |
| 🟢 in review | [docs(reference): add unity_docs and unity_reflect examples](https://github.com/CoplayDev/unity-mcp/pull/1401) | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) · ★ 14.2k |
<!-- oss:end -->

## Also

- **Suspicious Delicacies** — restaurant sim × turn-based RPG in Unity, three-person team; the restaurant loop, customer AI, QTE minigames and editor tooling are mine

## Toolbox

![Unity](https://img.shields.io/badge/Unity-121114?style=flat-square&logo=unity&logoColor=D6C29A)
![C# / .NET](https://img.shields.io/badge/C%23_%2F_.NET-121114?style=flat-square&logo=dotnet&logoColor=D6C29A)
![Python](https://img.shields.io/badge/Python-121114?style=flat-square&logo=python&logoColor=D6C29A)
![React](https://img.shields.io/badge/React-121114?style=flat-square&logo=react&logoColor=D6C29A)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-121114?style=flat-square&logo=githubactions&logoColor=D6C29A)
![Git](https://img.shields.io/badge/Git-121114?style=flat-square&logo=git&logoColor=D6C29A)

<sub>Header and cards are SVGs rendered by <code>scripts/</code> in the site's palette; the cards' text is outlined so they look the same on every machine.</sub>
