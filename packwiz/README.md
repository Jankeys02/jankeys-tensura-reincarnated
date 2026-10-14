# packwiz pack

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
| TensuraMoreSkills (`tensuramoreskills`) | 0.0.4.9.2 | 0.0.4.9.3 | quest skill ids all still exist (44 checked), but 0.0.4.9.3 adds a required dependency, CosmicEntropy (not in the pack), and is an alpha (checked 2026-10-14) |
| Tensura Reincarnated Nightmares (`tensura-reincarnated-nightmares`) | 1.0.5.1 | 1.0.5.2.2.5 | Tensura addon; check first |
| Polymorph (`polymorph`) | 1.1.0 | 1.2.0 | newer build is a beta |
| Simple Voice Chat (`simple-voice-chat`) | 2.6.22 | 2.6.24 | newer build is a beta |
| Music Notification (`music-notification`) | 3.3.1 | 3.4.0-alpha.1 | alpha |
| Tensura: Reincarnated Bosses (`tensura-reincarnated-bosses`) | 3.0.0 | 1.0.0 | would be a downgrade |
| Nightmare's Tensura Utils (`nightmares-tensura-utils`) | 0.1.2 | 0.1.0 | would be a downgrade |

Release channel: packwiz does not record it and `update` can pick betas, so check a file's type on its CurseForge/Modrinth page before updating. JEI builds are all marked beta by its author and are fine.
