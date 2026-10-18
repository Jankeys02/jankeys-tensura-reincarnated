# Contributing to Jankeys' Tensura Reincarnated

Thanks for taking a look. This is a small project, and issues and Pull Requests are welcome: quest fixes, config tweaks, KubeJS scripts, new mod suggestions, bug reports.

## New here? Never used GitHub?

**You do not need GitHub to help.** The easiest way is to play the pack and tell us what you notice (on Discord, or as a comment on an issue). You can also just send files (configs, scripts, mod lists) on Discord; someone who uses GitHub will add them.

**The words you will see, in plain language**

| Word | What it means |
|---|---|
| **Repository (repo)** | The folder with the whole pack online (mod list, configs, quests, scripts). It remembers every change ever made. |
| **Issue** | A note about one topic: a bug, an idea or a task ("chests render sunk", "add the farming mods"). It is where we discuss and tick things off. Anyone with a GitHub account can comment. |
| **Sub-issue** | A smaller note that belongs to a bigger one. The big issue shows how many of its sub-issues are done. |
| **Branch** | A copy of the pack where you can change things without touching the real pack (`main`). |
| **Commit** | A saved state with a short description ("fixed a quest text"). |
| **Push** | Uploading your saved state to GitHub. |
| **Pull Request (PR)** | A change proposal: "please take my changes into the pack." It is checked, then taken over. |
| **Draft** | A PR that is not finished yet. It cannot be merged by accident. |
| **Merge** | Taking the changes into the real pack (`main`). |
| **Fork** | Your own copy of the whole repo under your account, so you can change things without rights on the original. |
| **Collaborator** | Someone who was invited and may create branches directly in this repo. |
| **`main`** | The main branch, the real pack. Only checked changes end up here. |

**Three ways to help, from easiest to hardest**
1. **Play and report.** No GitHub needed. Say on Discord or in the matching issue what works and what does not (and send the file from `crash-reports` after a crash).
2. **Change one file in your browser** (only a GitHub account is needed):
   1. Open the file in the repo (for example `CHANGELOG.md` or a quest file).
   2. Click the **pencil icon** (Edit) at the top right.
   3. Change the text.
   4. Click **Commit changes...**, write a short note on what you changed, choose **Create a new branch**, then **Propose changes**.
   5. Click **Create pull request**. Done; the owner takes it from there.
3. **Change things in the game and upload them with GitHub Desktop** (see "Sharing in-game changes without commands" below). This is for quests you edit in the game.

**Questions are fine.** If a word or a step is unclear, ask on Discord. We will explain it and improve this page.

## Get set up

You need Git and Prism Launcher (a separate dev instance that installs the mods for you). [DEVELOPMENT.md](DEVELOPMENT.md) has the click-by-click setup, how to stay in sync, and how the repo is laid out. Read it first.

## What do you want to change?

Everything in the pack is a file in this repo, so every kind of change works the same way: change the file, test it in the game, send it back (see "Working together on one change" below for the click-by-click way). What differs is *which* file and *how to test it*.

| I want to change... | The files | How to test | Needs a CHANGELOG line |
|---|---|---|---|
| **Quests** (new chapter, text, rewards, order) | `config/ftbquests/quests/chapters/*.snbt` (one file per chapter), `config/ftbquests/quests/lang/en_us.snbt` (titles and descriptions) | Edit in game with the FTB Quests editor (it writes these files for you), or edit the files and reload the world. Check that every quest can be completed and the order makes sense | yes |
| **Scripts** (recipes, spawns, gates: KubeJS) | `kubejs/server_scripts/*.js` (server side), `kubejs/startup_scripts/*.js` (loaded once at start), `kubejs/data/` and `kubejs/assets/` (data and resource overrides) | Server scripts: run `/reload` in game. Client scripts: F3+T. Startup scripts: restart the game. Look for red errors in chat and in `logs/kubejs/` | yes |
| **Mod configs** (balance, behaviour of one mod) | `config/<mod>*.toml` / `.json` / `.json5`; `defaultconfigs/` for defaults that only apply to **new** worlds | Restart the game (some mods reload with a command). Commit only the config you changed on purpose: mods rewrite many files on launch | `defaultconfigs/`: yes; others: only if players notice |
| **A new mod, or removing/updating one** | `packwiz/mods/<mod>.pw.toml` (one file per mod), `packwiz/index.toml`, plus the mod's `config/` files | Prism dev instance installs it for you; start the game and then a server | yes |
| **Texts and docs** | `README.md`, `CHANGELOG.md`, the other `.md` files | Read it in the GitHub preview | no |

**A few rules that hold for all of them**
- **Test before you send.** Start the game with your change. For mods, also start the server (the Prism dev instance and the server both use the same `packwiz/` list).
- **One change per Pull Request** (one quest chapter, one script, one mod group), so it can be reviewed and undone on its own.
- **Say what you did** in the PR description and in the linked issue: what changed, why, and how you tested it.
- **Write the CHANGELOG line for players**, under `[Unreleased]` in `CHANGELOG.md` ("Added / Changed / Fixed", one short sentence, no technical ids). The "Changelog check" fails without it for `packwiz/`, `kubejs/`, `defaultconfigs/` and `config/ftbquests/`.
- **Don't send junk:** worlds, logs, crash reports, screenshots and anything with your username or account tokens stay on your machine.
- **Quests and scripts that use a mod's items or advancements** need that mod installed, and the ids must be spelled exactly as the mod registers them. Check them in game (for example with the F3+H item tooltip, or `/give` and `/advancement` auto-complete) before you commit.

**New mods without the `packwiz` command.** Adding a mod needs the `packwiz` program (see below), which is more setup than the other changes. If you don't want to install it, open or comment on the issue with the CurseForge link, the version for NeoForge 1.21.1, and what the mod is for; whoever has `packwiz` adds it to the same branch.

## Making a change

1. Pull the latest `main`, then make a branch for your change.
2. Test it in the game. Launch the pack and check it works; for a mod change, also start the server.
3. Keep the change focused: one Pull Request, one purpose.
4. Open the Pull Request against `main` and fill in the template. `main` is protected: changes need a Pull Request and one approval from the maintainer.

## Adding, removing or updating a mod

Mods are tracked in [`packwiz/`](packwiz/) (one small file per mod), not as jars. Add a mod with `packwiz curseforge add <CurseForge link>`, set whether it's client-only, run `packwiz refresh`, and commit `packwiz/` together with the mod's `config/` files and a line in `CHANGELOG.md`. The commands and rules are in [DEVELOPMENT.md](DEVELOPMENT.md) and [packwiz/README.md](packwiz/README.md). Developers sync mods automatically through a Prism instance (see DEVELOPMENT.md, "Which setup to use"). A PR that changes a mod isn't done until the reviewer has installed it.

## Changelog check

A Pull Request that changes `packwiz/`, `kubejs/`, `defaultconfigs/` or `config/ftbquests/` must also change `CHANGELOG.md` (a line under `[Unreleased]`, written for players), or the "Changelog check" fails and the PR can't be merged. For changes players won't notice, such as a typo, put `[skip changelog]` in the PR description or add the `skip-changelog` label.

## What not to commit

Worlds (`saves/`), logs, crash reports, screenshots, and anything with your username or account tokens. If `git status` lists them, leave them out of `git add`. Mods often rewrite their own config on launch, so only commit config files you changed on purpose.

## Reporting bugs and requesting features

Use the [issue templates](.github/ISSUE_TEMPLATE); they ask for what's needed to reproduce the problem. For crashes, include the crash report or `latest.log`.

**Big topics get an umbrella issue with sub-issues.** A large change (for example "add the tier 2 mods") is one umbrella issue that holds the decisions. Each step (for example one mod group) gets its own normal issue with a checklist of mods, tests and quest chapter, linked to the umbrella as a GitHub *sub-issue* (open the umbrella, **Create sub-issue** or **Add existing issue**). The umbrella then shows how many sub-issues are done. Close a sub-issue when its checklist is finished. Use labels for the kind of issue (`bug`, `enhancement`, `question`).

## Working together on one change

One issue, one branch, one Pull Request. Example: issue #7 (farming mods) and its draft PR on the branch `farming-mods`.

1. **Open the PR early as a draft**, and put `Refs #<issue>` in its description. That puts the PR in the issue's timeline. Use `Refs`, not `Closes`, so merging does not close the issue before its checklist is done.
2. **Say what you are working on** in a comment on the issue, or assign yourself to it. Two people changing the same file at once causes merge conflicts.
3. **Everyone works on the same branch.** People the maintainer has invited as collaborators (below) can push to it; everyone else forks the repo and sends a PR to that branch.
4. **Tick the issue's checklist** as parts are finished. A sub-issue is closed by hand once the whole checklist is done.
5. **Take the PR out of draft** when it is ready. `main` is protected by a ruleset (**Settings > Rules > Rulesets > Protect main**): changes need a PR, one approval and a passing "Changelog check", and force-pushes and deletion are blocked. Only the owner role can bypass it.

**Editing without Git.** On GitHub, switch to the branch (top left), open a file, click the pencil icon, change it and click **Commit changes**. This is enough for texts, `CHANGELOG.md`, quests and scripts. Adding a mod needs the `packwiz` command (see above).

**Sharing in-game changes without commands (GitHub Desktop).** Quests edited in the game are saved as files in your Prism instance folder. To send them to the branch without typing Git commands:

1. Install [GitHub Desktop](https://desktop.github.com) and sign in (**File > Options > Accounts**) with the GitHub account that was invited.
2. **File > Add local repository**, choose the instance's game folder (in Prism: right-click the instance, **Folder**, open `minecraft`).
3. Top bar **Current branch**: choose the branch of the change (for example `farming-mods`; if it is not listed, click **Fetch origin** first).
4. In the **Changes** list, tick only the files you changed on purpose (for quests: `config/ftbquests/...`). Untick everything else; mods rewrite many config files on launch.
5. Bottom left: write a short summary (for example "Farming chapter: fix quest order") and click **Commit to <branch>**.
6. Click **Push origin** (top bar). The change shows up in the Pull Request.

Without an invitation, click **Fork** on GitHub instead and push to your own fork; GitHub Desktop offers this when you try to push.

**Inviting a collaborator (owner).** Repo **Settings > Collaborators > Add people**, enter the GitHub name, role **Write**. They accept by e-mail. Write access lets them push branches, edit and assign issues and open PRs; it does not let them change `main` directly.

## Trying a change before it is merged

Players who only play can check a change in three ways, from simplest to most work:

1. **Add the mods by hand** (best for one new mod group): open the pack in the CurseForge app, **Add More Content**, install the mods listed in the issue (NeoForge 1.21.1), play, and report in the issue or on Discord. Use a copy of the instance so the real world is safe.
2. **Pre-release:** the maintainer tags `vX.Y.Z-rc.N`, which builds a pre-release zip, and publishes it to CurseForge as a beta ([RELEASE_GUIDE.md](RELEASE_GUIDE.md)). Players update the pack in the app.
3. **Prism dev instance on the branch:** push the branch, then change `main` to the branch name in the installer URL inside `pre-launch.bat` (do not commit that change) and launch. See DEVELOPMENT.md, "Your own mod changes".

Report what you found in the issue: what you did, what worked, what broke, and the crash report or `latest.log` if the game crashed.

## Releasing

See [RELEASE_GUIDE.md](RELEASE_GUIDE.md). Only the maintainer cuts releases.
