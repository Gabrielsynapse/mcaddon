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
		if args[0] == "rp" or "bp":
			Project.behavior_pack.adddependency(args[0],args[1])
			Util.writejson(Util.listdict.get(build["sources"],"identifier","behavior_pack-manifest")["src"],Project.behavior_pack.manifest)
		else:
			Util.error("argumento '{}' invalido".format(args[0]))
	else:
		Util.error("opcao '{}' invalido".format(option))
elif typepack == "-rp":
	if option == "-dependency":
		if args[0] == "rp" or "bp":
			Project.resource_pack.adddependency(args[0],args[1])
			Util.writejson(Util.listdict.get(build["sources"],"identifier","resource_pack-manifest")["src"],Project.resource_pack.manifest)
		else:
			Util.error("argumento '{}' invalido".format(args[0]))
	else:
		Util.error("opcao '{}' invalido".format(option))
else:
	error("opcao '{}' invalido".format(typepack))