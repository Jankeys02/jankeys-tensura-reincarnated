# packwiz pack

The mod list, as small text files (one per mod) instead of jars. `side` in each file says where it belongs: `client` or `both`.
Edit with [packwiz](https://packwiz.infra.link) from this folder.

```bash
packwiz curseforge add <curseforge-url>   # add a mod
packwiz update --all                      # update mods
packwiz remove <name>                     # remove a mod
packwiz refresh                           # rebuild index.toml (run before committing)
packwiz curseforge export                 # build the CurseForge zip
```

To mark a mod client-only, change `side = "both"` to `side = "client"` in its `.pw.toml`.
Pushing a `v*` tag builds the CurseForge zip and a Modrinth `.mrpack` and attaches them to the GitHub release.
