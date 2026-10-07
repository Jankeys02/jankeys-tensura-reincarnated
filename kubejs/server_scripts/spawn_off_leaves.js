// Terralith forests are tall, and vanilla picks the world spawn from a heightmap that counts leaves,
// so players can spawn on top of a tree canopy. If a player (re)spawns near the world spawn standing
// on leaves, move them to the nearest real ground. Never moves anyone who is not on leaves.

const McHeightmap = Java.loadClass('net.minecraft.world.level.levelgen.Heightmap$Types')

const SPAWN_RADIUS = 24 // only act this close to the world spawn
const SEARCH_RADIUS = 12 // how far to look for open ground
function groundY(level, x, z) {
  // MOTION_BLOCKING_NO_LEAVES = first free y above the top non-leaf block
  const y = level.getHeight(McHeightmap.MOTION_BLOCKING_NO_LEAVES, x, z)
  const below = level.getBlock(x, y - 1, z)
  if (below.hasTag('minecraft:leaves') || below.hasTag('minecraft:logs')) return null
  if (!below.blockState.getFluidState().isEmpty()) return null
  if (!level.getBlock(x, y, z).blockState.isAir()) return null
  if (!level.getBlock(x, y + 1, z).blockState.isAir()) return null
  return y
}

// Look outward in square rings around (px, pz) and return [x, y, z] of the nearest column with open ground.
function findGround(level, px, pz) {
  for (var r = 0; r <= SEARCH_RADIUS; r++) {
    for (var dx = -r; dx <= r; dx++) {
      for (var dz = -r; dz <= r; dz++) {
        if (Math.max(Math.abs(dx), Math.abs(dz)) !== r) continue
        var y = groundY(level, px + dx, pz + dz)
        if (y !== null) return [px + dx, y, pz + dz]
      }
    }
  }
  return null
}

function groundPlayer(event) {
  const player = event.player
  const level = player.level
  // level.dimension is a KubeJS property (not a method); its string form contains the dimension id
  if (String(level.dimension).indexOf('minecraft:overworld') === -1) return
  const pos = player.blockPosition()
  const spawn = level.getSharedSpawnPos()
  if (Math.abs(pos.getX() - spawn.getX()) > SPAWN_RADIUS || Math.abs(pos.getZ() - spawn.getZ()) > SPAWN_RADIUS) return
  const under = level.getBlock(pos.getX(), pos.getY() - 1, pos.getZ())
  if (!under.hasTag('minecraft:leaves')) return

  const g = findGround(level, pos.getX(), pos.getZ())
  if (g === null) {
    return // no open ground nearby; leave the player where they are
  }
  const name = player.getGameProfile().getName()
  event.server.runCommandSilent('tp ' + name + ' ' + (g[0] + 0.5) + ' ' + g[1] + ' ' + (g[2] + 0.5))
  console.info('spawn_off_leaves: moved ' + name + ' from the canopy at ' + pos.getX() + ' ' + pos.getY() + ' ' + pos.getZ() + ' to ' + g[0] + ' ' + g[1] + ' ' + g[2])
}

PlayerEvents.loggedIn(groundPlayer)
PlayerEvents.respawned(groundPlayer)
