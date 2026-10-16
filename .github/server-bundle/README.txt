Jankeys' Tensura Reincarnated - server pack @VERSION@
Minecraft @MC@, NeoForge @NEOFORGE@. Needs Java 21.

1. Unzip this folder somewhere empty.
2. Open MISSING-MODS.txt. If it lists mods, download each from its link (they can't be bundled because their authors
   block it) and put the files in the "mods" folder.
3. Run start.bat (Windows) or "sh start.sh" (Linux). The first run installs the NeoForge server; it stops because
   the Minecraft EULA is not accepted yet. Open eula.txt, set eula=true, and run the start script again.
4. Give the server 4-8 GB RAM: edit user_jvm_args.txt (for example -Xms4G -Xmx8G). Open TCP port 25565 on your router.

Updating: back up your world, then unzip the new version over the old one (keep your world and eula.txt), check
MISSING-MODS.txt again, and delete mods that are no longer in the new "mods" folder. Players need the matching
client version. World generation mods only change newly generated chunks.
