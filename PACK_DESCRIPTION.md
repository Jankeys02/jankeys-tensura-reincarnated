# Jankeys' Tensura Reincarnated

Reincarnate as a slime (or anything else) in a NeoForge 1.21.1 world built around *That Time I Got Reincarnated as a Slime*. A quest book narrated by the "Voice of the World" teaches you the pack as you play, from your first day to the endgame bosses.

**What's inside**
- **Tensura core + addons:** Ice and Fire, Nightmare, FTB Quests, Better Subordinates, Guild, Enigmatic, Unique Monsters, Ascension, TensuraMoreSkills, Elite Tensura Addon and Origins.
- **A 31-chapter quest book (830 quests)**, with a short tutorial ("Field note") in every quest. Chapters are grouped: a Field Guide to the controls, Tensura, the four extra dimensions, boss hunts, homestead life, ranked Paths, and a chapter for each Tensura addon.
- **Ranked Paths:** quests grant ranks as you progress. The Miner's Path grows Ultimine from 8 to 64 blocks (with hunger cost and cooldown). The Explorer's, Homesteader's and Hunter's Paths add claimed chunks, homes and bonus health, and each rank grants a Tensura skill.
- **Dimension gate:** in survival, three dimensions (Eternal Starlight, Chrono Dawn, The Afterdark) are locked until you have visited the Nether or summoned a Wither. Creative, spectator and operators are exempt.
- **Difficulty-scaled spawns:** the strongest mobs only spawn naturally on higher difficulties. Ogres appear from Normal; Benimaru, Primordial Noir, Arch Daemon, Salamander, Feathered Serpent and Sissie only on Hard; Greater Daemon, Kyoya Tachibana, Laplace and the Dread Lich from Normal. Spawn eggs and commands still work, and the table is easy to edit (`kubejs/server_scripts/spawn_by_difficulty.js`).
- **Safe spawn:** if the world spawn puts you on top of a tall tree canopy or a structure (for example the Thornborn Towers), you are moved to open ground on your first login and on respawns near spawn. A base you build inside a structure is left alone at later logins.
- **Spread-out landmarks:** the Tensura boss structures, the adventurer guild, the Paths Gate and the Mysticism portals share one placement rule, so they lie at least about 800 blocks apart. They also generate in Terralith biomes.
- **Sensible defaults:** new installs start with tuned video, sound and key-binding defaults and mod client configs (through Default Options); your own settings are not overwritten.
- **Quality of life:** AttributeFix (lifts vanilla attribute caps for Tensura's high stats), No Chat Reports, FastSuite, Connectivity, Faster Ladder Climbing, Overflowing Bars, Obscura's Simple Storage and Mod Name Tooltip.
- **World:** Terralith biomes plus four extra dimensions (The Twilight Forest, Eternal Starlight, Chrono Dawn, The Afterdark).
- **Structures and loot:** the YUNG's suite, Dungeons Arise, Artifacts, Backpacked, Sophisticated Storage, and Apotheosis (gear affixes, gems and new enchanting).
- **Bosses:** L_Ender's Cataclysm, Mowzie's Mobs, plus custom Tensura boss structures (some boss structures are rare and may be far from spawn).
- **Homestead:** Farmer's Delight, Comforts, Supplementaries, Waystones.
- **Performance:** Sodium, Iris, ModernFix, FerriteCore, Entity Culling, Distant Horizons.
- **Visuals (optional):** Fresh Animations, 3D trims, Complementary shaders.

**Requirements**
- Minecraft 1.21.1, NeoForge 21.1.249
- 6-8 GB RAM allocated (8 GB recommended with shaders / Distant Horizons)
- Recommended Java arguments: `-XX:+UseZGC -XX:+ZGenerational` (Java 21). Distant Horizons warns about stuttering with the default garbage collector (G1); ZGC avoids it, at the cost of some extra RAM. Put them in the launcher's Java arguments for the instance. The Prism dev instance (see DEVELOPMENT.md) has them set already.

**Server pack**
A dedicated-server pack is attached to each release as an additional file, and on the [GitHub releases page](https://github.com/Jankeys02/jankeys-tensura-reincarnated/releases). It installs the server's mods with an installer, skips client-only mods, and includes Chunky (pregeneration) and FTB Ranks (command permissions). Six mods can't be downloaded automatically because their authors block it (Custom Chest Menus, Easy NPC, FiltPick, Tensura: Better Subordinates, Tensura: Enigmatic, Tensura: Unique Monsters); the installer prints a link for each. Accept the Minecraft EULA yourself, give it 4-8 GB RAM, and open UDP 24454 for proximity voice chat. Setup steps are in `SERVER_HOSTING.md` in the GitHub repo. Back up your world before updating, since world generation mods only change newly generated chunks.

**Contributing and source**
Configs, quests, scripts and the mod list live on [GitHub](https://github.com/Jankeys02/jankeys-tensura-reincarnated). Pull requests are welcome.

**Credits** — the full mod list is in [`packwiz/mods`](https://github.com/Jankeys02/jankeys-tensura-reincarnated/tree/main/packwiz/mods); all mods belong to their authors.
