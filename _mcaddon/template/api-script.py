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
	"mcaddon.sh -add -bp -module -javascript "+name
]
for c in cmd:
	out = Util.Shell(c.split(" "))
	print(out.result)

Util.mkdir(f"{src}/script")

Util.writefile(f"{src}/script/main.js","""
import { world, system } from "@minecraft/server";

function onStart() {

}

system.run(onStart);
""")
