import Project
import Util
from sys import argv

typepack = argv[1]
option = argv[2]
args = argv[3:]

build = Util.readjson("build.json")
Project.load(build)

if typepack == "-bp":
	if option == "-dependency":
		if args[0] in ["rp","bp"]:
			Project.behavior_pack.adddependency(*args)
		elif args[0] in ["server","server-ui","common"]:
			Project.behavior_pack.adddependency(*args)
		else:
			Util.error("argumento '{}' invalido".format(args[0]))
	elif option == "-module":
		if args[0] == "-javascript":
			Project.behavior_pack.addmodule("javascript",args[1])
			Project.behavior_pack.setEnableCapabilities(True)
	else:
		Util.error("opcao '{}' invalido".format(option))
elif typepack == "-rp":
	if option == "-dependency":
		if args[0] in ["rp","bp"]:
			Project.resource_pack.adddependency(args[0],args[1])
		else:
			Util.error("argumento '{}' invalido".format(args[0]))
	else:
		Util.error("opcao '{}' invalido".format(option))
else:
	Util.error("opcao '{}' invalido".format(typepack))