// Spawn gate: strong mobs only spawn naturally when the world difficulty is high enough.
// Biome modifiers (the data files) cannot see the difficulty, so this script cancels the spawn instead.
// Only natural and world-generation spawns are blocked. Spawn eggs, commands, spawners and structures are not.
// Difficulty ids: 0 Peaceful, 1 Easy, 2 Normal, 3 Hard. Use 99 to stop a mob from spawning naturally at all.
// Edit MIN_DIFFICULTY, then `/kubejs reload server_scripts` (or restart) to apply.

const MIN_DIFFICULTY = {
  // Tensura: Reincarnated Bosses (the pack tones these spawns down in kubejs/data/trying_to_make_an_addon/)
  'trying_to_make_an_addon:ogre': 2,
  'trying_to_make_an_addon:benimaru': 3,
  'trying_to_make_an_addon:primordialnoir': 3,
  'trying_to_make_an_addon:bosstest': 99, // test mob from the mod author

  // Tensura and addons
  'tensura:arch_daemon': 3,
  'tensura:salamander': 3,
  'tensura:feathered_serpent': 3,
  'tensura:sissie': 3,
  'tensura:greater_daemon': 2,
  'tensura:kyoya_tachibana': 2,
  'tensura_guild:laplace': 2,

  // Ice and Fire
  'iceandfire:dread_lich': 2
}

const GATED_SPAWN_TYPES = ['NATURAL', 'CHUNK_GENERATION']

Object.keys(MIN_DIFFICULTY).forEach(function (id) {
  EntityEvents.checkSpawn(id, function (event) {
    if (GATED_SPAWN_TYPES.indexOf(String(event.type.name())) === -1) return
    if (event.level.getDifficulty().getId() < MIN_DIFFICULTY[id]) event.cancel()
  })
})
