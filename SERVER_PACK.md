# Server pack plan

NeoForge 21.1.249 / Minecraft 1.21.1. Built from the client pack, minus client-only mods.
Mod ids below are `modId`s from each jar's `neoforge.mods.toml` (151 mods in `mods/` as of the second pass).

## Exclude from the server (client-only)
Rendering / performance (client): `sodium`, `sodium_extra`, `reeses_sodium_options`, `sodiumextrainformation`, `iris`, `immediatelyfast`, `entityculling`, `moreculling`, `entity_model_features`, `entity_texture_features`, `vanillin`, `badoptimizations`, `dynamic_fps`, `smoothchunk`, `chloride`
Animation / visuals: `firstperson`, `notenoughanimations`, `skinlayers3d`, `modefite`, `manas_cosmetics`, `advancementplaques`, `ragdollified`*
UI / HUD / QoL: `betteradvancements`, `controlling`, `mousetweaks`, `extremesoundmuffler`, `trashslot`, `obscure_tooltips`, `betteradvancedtooltips`, `enchdesc`, `jei`, `jeresources`, `ftbjeiextras`, `searchables`, `defaultoptions`, `ftbqopt`
Map: `xaerominimap`, `xaeroworldmap`, `ftbxaerocompat`, `pingtomapxaeros`, `w2w2` (Waystones2Waypoints2)
Audio: `musicnotification`, `timm`, `extrasounds`, `battlemusic`*, `sound_physics_remastered`

## Keep (server needs them)
`waystones`, `spawnstones`, `mysticism`, `tensura_boss_structure`, `patchouli`, `pingwheel` (both sides), `spark` (server profiler), `tensura`, `tensura_*`, `manas*`, `trnightmare`, `nightmareutils`, `greatsage`, `trying_to_make_an_addon`, `iceandfire`, `kubejs`, `rhino`, `ftb*` (chunks/essentials/quests/teams/ultimine/library/xmodcompat), `curios`, `artifacts`, `lootr`, `corpse`, `voicechat`, `dungeons_arise`, `yungs*` / `better*` structures, `terrablender`, `sophistic*`, `backpacked`, libraries (`geckolib`, `architectury`, `balm`, `cloth_config`, `iceberg`, `bookshelf`, ...), `ferritecore`, `modernfix`, `krypton_fnp`, `fastleafdecay`, `alltheleaks`, `easy_npc*`, `watut`, `polymorph`, `carryon`, `incontrol`, `torchmaster`

## Uncertain: test on a real dedicated server
Marked `*` above plus `distanthorizons` (optional server side; leave out unless wanted), `punchy`, `fragmentum`, `showcaseitem`, `eliteholograms`, `cosmeticarmorreworked`, `corpse_waypoints`. NeoForge fails loudly at boot on a client-only mod, so start the server, remove what it names, repeat.

## Steps
1. Export the client pack from the CurseForge app (0.1.0).
2. Build the server zip with ServerPackCreator (downloads mods from CurseForge itself and writes start scripts) using the exclude list above.
3. Boot it, remove any mod that crashes on server.
4. Set `server.properties`, review `ftbessentials`/`ftbchunks`/`ftbteams` defaults for multiplayer.
5. Upload the zip as the "server pack" additional file on the CurseForge release.
