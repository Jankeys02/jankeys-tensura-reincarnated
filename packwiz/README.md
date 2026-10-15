# packwiz pack

[packwiz](https://packwiz.infra.link) keeps the mod list as plain text: `pack.toml` (Minecraft and NeoForge version), `index.toml` (every file with a hash) and one `mods/<name>.pw.toml` per mod (name, exact file, CurseForge project and file ID, side). No jars are stored. Git therefore shows every added, removed or updated mod in a commit, and several people can change the list through Pull Requests.

Three things read this folder:

- **Developers** on Prism sync their mods from it at each launch (packwiz installer, `-s client`).
- **Servers** do the same with `-s server`.
- **Releases:** pushing a `v*` tag builds the CurseForge zip from it.

Setup steps for each are in [DEVELOPMENT.md](../DEVELOPMENT.md). Keep `index.toml` in step with the mod files: run `packwiz refresh` before every commit, or the installer reports a hash mismatch.

The mod list, as small text files (one per mod) instead of jars. `side` in each file says where it belongs: `client` or `both`.
Edit with [packwiz](https://packwiz.infra.link) from this folder.

```bash
packwiz curseforge add <curseforge-url>   # add a mod
packwiz update --all                      # update mods
packwiz remove <name>                     # remove a mod
packwiz refresh                           # rebuild index.toml (run before committing)

```

To mark a mod client-only, change `side = "both"` to `side = "client"` in its `.pw.toml`.
Pushing a `v*` tag builds the CurseForge zip and attaches them to the GitHub release.

## Held-back versions

`packwiz update --all` is not safe to run blindly: it has proposed downgrades, pre-releases and a file named for the wrong Minecraft version. Update mods one at a time (`packwiz update <name>`). Mods deliberately kept on their current version (last checked 2026-10-14):

| Mod (`mods/` file) | Pinned version | Newer seen | Why it is held |
|---|---|---|---|
| Ice and Fire (`iceandfire-ce`) | 2.0-beta.15 | 2.1.4 | `tensura_iaf` needs classes removed in 2.1.x |
| Uranus (`uranus`) | 2.4.1-bugfix | 3.0-beta.1 | pre-release; a tester reported crashes after updating |
| Corpse x Curios Compat (`corpse-x-curios-api-compat`) | 3.1.3 | 4.2.0 | major version |
| The Afterdark (`the-afterdark`) | 1.0.3.1 | 1.1.0 | 1.1.0 moves the altar structure file to `data/.../structures/` (1.21.1 reads `structure/`), so the altar may stop generating and the way into the dimension is lost; the dimension type also changed (checked 2026-10-14, not booted) |
| Polymorph (`polymorph`) | 1.1.0 | 1.2.0 | newer build is a beta |
| Simple Voice Chat (`simple-voice-chat`) | 2.6.22 | 2.6.24 | newer build is a beta |
| Music Notification (`music-notification`) | 3.3.1 | 3.4.0-alpha.1 | alpha |
| Tensura: Reincarnated Bosses (`tensura-reincarnated-bosses`) | file from 2026-09-27 (named 3.0.0; the author later restarted numbering at 1.0.0) | file from 2026-10-13 (named 1.0.0) | the newer build adds natural boss spawns via biome modifiers (Rimuru True Demon Lord in any biome, weight 2; Adalman, Geld, Zegion, Chloe Aubert, Velzard Frost Dragon and more); quests and overrides are unaffected. The pinned file already spawns Benimaru, Ogre, Primordial Noir and a test boss in every biome; Benimaru and Ogre are toned down by overrides in `kubejs/data/trying_to_make_an_addon/` (checked 2026-10-15). To update, first neutralise the new spawns the same way (checked 2026-10-14, not booted) |
| Nightmare's Tensura Utils (`nightmares-tensura-utils`) | 0.1.2 | 0.1.0 | would be a downgrade |

Release channel: packwiz does not record it and `update` can pick betas, so check a file's type on its CurseForge/Modrinth page before updating. JEI builds are all marked beta by its author and are fine.
