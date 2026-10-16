# Contributing to Jankeys' Tensura Reincarnated

Thanks for taking a look. This is a small project, and issues and Pull Requests are welcome: quest fixes, config tweaks, KubeJS scripts, new mod suggestions, bug reports.

## Get set up

You need Git and Prism Launcher (a separate dev instance that installs the mods for you). [DEVELOPMENT.md](DEVELOPMENT.md) has the click-by-click setup, how to stay in sync, and how the repo is laid out. Read it first.

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

## Releasing

See [RELEASE_GUIDE.md](RELEASE_GUIDE.md). Only the maintainer cuts releases.
