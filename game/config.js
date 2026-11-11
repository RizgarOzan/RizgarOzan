// Where this copy of the fight lives. core.js (README links), turn.js (issues) and the Worker
// (GitHub API, redirect) all read it, so moving the game to another repo means editing only this file.
module.exports = {
  // owner/name of the repo that holds state.json, boss.svg and the README
  repo: 'RizgarOzan/RizgarOzan',
  branch: 'main',
  // the page the README shows on and where players land after a move; a profile README shows on the user page
  page: 'https://github.com/RizgarOzan',
  // GitHub's id for the fight's heading in the README
  anchor: 'boss-fight-autobots-vs-megatron',
  // one-click links go to this Worker; set it to '' and the README falls back to issue links
  worker: 'https://profile-boss.rizgarozan7.workers.dev',
  // files the fight writes, relative to the repo root
  files: { state: 'game/state.json', svg: 'assets/boss.svg', readme: 'README.md' },
};
