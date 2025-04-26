import Project
import Util
from sys import argv
from os import path

source = argv[1]
name   = argv[2]

src = f"{name}_behavior_pack"

cmd = [
	"mcaddon.sh -init . -bp",
	"mcaddon.sh -add -bp -dependency server",
	"mcaddon.sh -add -bp -dependency server-ui",
	"mcaddon.sh -add -bp -dependency common",
	"mcaddon.sh -add -bp -module -javascript main"
]
for c in cmd:
	out = Util.Shell(c.split(" "))
	print(out.result)

Util.mkdir(f"{src}/scripts")

Util.writefile(f"{src}/scripts/main.js","""
import { world,system } from "@minecraft/server";
let player;

//player.storage.get("key")
//player.storage.set("key","value")
//world.storage.get("key")
//world.storage.set("key","value")
//world.runCommand("cmd")

function onJob(eventData){
	player = eventData.player
	world.sendMessage("Hello, World!");
}
world.afterEvents.playerSpawn.subscribe(onJob)
});

""")
