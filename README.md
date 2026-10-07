# Jankeys' Tensura Reincarnated

NeoForge 1.21.1 modpack built around *That Time I Got Reincarnated as a Slime* (Tensura) with 14 FTB Quests chapters.

> Download and install through the CurseForge app: [Jankeys' Tensura Reincarnated](https://www.curseforge.com/minecraft/modpacks/jankeys-tensura-reincarnated). This repo holds the pack's configs, KubeJS scripts, quests and changelog; mod jars are not stored here.

**What's inside**
- Tensura core + addons (Ice and Fire, Nightmare, FTB quests, better subordinates, Guild, Enigmatic, Unique Monsters)
- 14 FTB Quests chapters guiding you from Getting Started to Myths and Treasure
- Leveling system: quests grant ranks as you progress. Ultimine starts small (8 blocks) and grows to 64 with the Miner's Path, with hunger cost and cooldown; more rank paths to come
- Better structures (YUNG's suite), Dungeons Arise, Artifacts, Backpacked, Sophisticated Storage
- Performance: Sodium, Iris, ModernFix, FerriteCore, Entity Culling, Distant Horizons
- World: Terralith biomes plus four extra dimensions (The Twilight Forest, Eternal Starlight, Chrono Dawn, The Afterdark)
- Bosses and structures: L_Ender's Cataclysm, Mowzie's Mobs, plus custom Tensura boss structures
- Polished visuals: Fresh Animations, 3D trims, Complementary shaders (optional)

**Requirements**
- Minecraft 1.21.1, NeoForge 21.1.249
- 6-8 GB RAM allocated (8 GB recommended with shaders / Distant Horizons)

**Credits** — see the mod list; all mods belong to their authors.

**Server pack**
A tested dedicated-server pack (NeoForge 21.1.249, client-only mods removed) is attached to each release as an additional file. Accept the Minecraft EULA yourself, give it 4-8 GB RAM, and open UDP 24454 if you want proximity voice chat. It includes Chunky (pregeneration) and FTB Ranks (command permissions); see `SERVER_HOSTING.md` in the pack for setup. Three mods are not bundled because their authors do not allow redistribution (Tensura: Better Subordinates, Tensura: Enigmatic, Tensura: Unique Monsters); download them from their CurseForge pages, see `SERVER_HOSTING.md` in the pack. Back up your world before updating, since worldgen mods only change newly generated chunks.

## Repo layout
- `config/`, `defaultconfigs/` — mod configs and FTB Quests
- `kubejs/` — scripts and resource overrides (incl. `musicnotification/musics.json` fix)
- `SERVER_PACK.md`, `SERVER_HOSTING.md` — server pack build notes and hosting guide
- `CHANGELOG.md` — SemVer; `package.json` `version` is the source of truth

## License
See [LICENSE](LICENSE). Mods belong to their authors.
