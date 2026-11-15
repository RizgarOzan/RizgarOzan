<p align="center"><img src="assets/hero.gif" width="880" alt="Rızgar Ozan, game and tools programmer. Soundwave drawn one letter per pixel."></p>

**Unity/C# game and tools programmer. I also build LLM eval tooling: [Turkish RAG Eval](https://github.com/RizgarOzan/turkish-rag-eval) is now an MTEB task.**<br>
Final year at Hacettepe University, graduating June 2027 · software intern at Barko Elektronik, Jul-Aug 2026 · looking for game/tools programmer and LLM-eval internships and new-grad roles in Europe and Turkey.

<!-- summary:start -->
**160 pull requests merged** into 42 projects I don't own, among them mteb, kornia, unity-mcp and docling. 16 more in review.
<!-- summary:end -->

`C#` `Unity` `C++20` `WebAssembly` `Python` `FastAPI` `Docker` `local LLMs / RAG`

[rizgarozan.github.io](https://rizgarozan.github.io) · [LinkedIn](https://www.linkedin.com/in/rizgarozan/) · [itch.io](https://rizgarozan.itch.io)

<p><img src="assets/chip-1.svg" width="880" alt="Work"></p>

<p align="center">
<a href="https://github.com/RizgarOzan/turkish-rag-eval"><img src="assets/card-rag.svg" width="400" alt="Turkish RAG Eval: nDCG@10 0.78 vs 0.50"></a>
<a href="https://rizgarozan.github.io/lockstep-tactics/"><img src="assets/card-lockstep.svg" width="400" alt="Lockstep Tactics: 1000 of 1000 matches bit-identical"></a>
<a href="https://github.com/RizgarOzan/match3-lab"><img src="assets/card-match3.svg" width="400" alt="Match3 Lab: greedy bot 100% vs random 70%"></a>
</p>

| Project | What it is | Proof |
|---|---|---|
| [Turkish RAG Eval](https://github.com/RizgarOzan/turkish-rag-eval) | Turkish retrieval benchmark, in MTEB | nDCG@10 0.78 vs 0.50 |
| [Lockstep Tactics](https://github.com/RizgarOzan/lockstep-tactics) | C++20 lockstep tactics game | 1000/1000 matches bit-identical · [play](https://rizgarozan.github.io/lockstep-tactics/) |
| [Match3 Lab](https://github.com/RizgarOzan/match3-lab) | match-3 core, Unity tools, bot sim | bot wins 100% vs random 70% |
| [TMP Glyph Audit](https://github.com/RizgarOzan/tmp-glyph-audit) | finds TextMeshPro text your fonts can't draw | 33 core tests |

<p><img src="assets/chip-2.svg" width="880" alt="Last mission"></p>

<p align="center"><img src="assets/intercept-log.svg" width="440" alt="Internship log: Barko Elektronik, complete."></p>

**Barko Elektronik**, software intern, Jul-Aug 2026: local LLMs behind Open WebUI + LDAP, an Oracle to Power BI pipeline, FastAPI + Docker services.

## Duel: Soundwave vs Shockwave

<p align="center"><img src="assets/shockwave-radar.gif" width="880" alt="Shockwave is scanning"></p>

Everyone who visits plays Soundwave in the same duel against Shockwave's planning AI. Turn engine and AI are in [game/](https://github.com/RizgarOzan/RizgarOzan/tree/main/game). Pick a move and a GitHub Action plays it in about a minute. If the picture looks unchanged, give it a few seconds and refresh.

<!-- boss:start -->
**Round 5** · Soundwave 2299/3000 HP, 6 EP · Shockwave 2876/3750. Pick Soundwave's move ↓

<p align="center"><img src="assets/scene-4.svg" width="880" alt="Duel scene. Shockwave diverts all power to his arm cannon. LOGIC CANNON next turn. Guard!"></p>

> ⚠️ **Shockwave has charged the LOGIC CANNON.** It hits for 520–590 this round. GUARD or MIND SCAN cuts it down.

| Move | Cost | Effect |
|---|---|---|
| [**ATTACK**](https://github.com/RizgarOzan/RizgarOzan/issues/new?title=boss%3A%20soundwave%20atk&body=Just%20press%20Submit.%20A%20GitHub%20Action%20plays%20the%20move%20and%20updates%20the%20README%20in%20about%20a%20minute.) | – | SONIC BLASTER: hit for 200–260 |
| ~~LASERBEAK~~ | 14 EP (has 6) | Hit twice for 110–140 each |
| ~~MIND SCAN~~ | 8 EP (has 6) | Hit for 90–120, take half damage this round (even from CRUSHING GRIP), and see Shockwave's plan and reasoning for next round |
| [**GUARD**](https://github.com/RizgarOzan/RizgarOzan/issues/new?title=boss%3A%20soundwave%20guard&body=Just%20press%20Submit.%20A%20GitHub%20Action%20plays%20the%20move%20and%20updates%20the%20README%20in%20about%20a%20minute.) | – | Take a third of the damage this round, +10 EP, +15% limit. CRUSHING GRIP goes through it |
| LIMIT: CASSETTE ASSAULT | 74% | Locked, fills as you attack, guard and take hits |

<sub>Each move opens a prefilled issue: press **Submit** and a GitHub Action plays it, usually within a minute.</sub>

**Last moves**
- Shockwave diverts all power to his arm cannon. LOGIC CANNON next turn. Guard!
- @RizgarOzan · Soundwave probes Shockwave's mind for 119 damage: POWER DIVERT is coming, and his next plan will show. Incoming damage halved this round.
- Shockwave uses CRUSHING GRIP. 195 damage.

<details><summary>earlier</summary>

- @RizgarOzan · Laserbeak makes two passes: 115 and 122.
- Shockwave uses ARM CANNON. 255 damage.
- @SemihAsln · Laserbeak makes two passes: 133 and 137.
- Shockwave uses ARM CANNON. 251 damage.
- @RizgarOzan · Laserbeak makes two passes: 136 and 112.

</details>

**Top damage this duel**: 🥇 @RizgarOzan 604 · 🥈 @SemihAsln 270
<!-- boss:end -->

<details><summary>How Shockwave thinks</summary>

Each round Soundwave moves, then Shockwave answers. Shockwave doesn't pick at random: he plans his next move from what you just did. Guard twice in a row and he crushes the guard, sit on full EP and he jams it, fall low and he goes for the finish, get him low and he repairs. MIND SCAN shows his next move and his reasoning. When he charges the LOGIC CANNON, GUARD or MIND SCAN. If someone moved before you, the page tells you and you pick again from the fresh board.

</details>

<sub>Letter art inspired by [@jin_22ee](https://github.com/JIN2-ASCII). Soundwave and Shockwave are Hasbro's Transformers; this is fan art.</sub>
