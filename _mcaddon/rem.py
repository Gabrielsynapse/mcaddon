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
		if args[0].isdigit():
			index = int(args[0])
			Project.behavior_pack.remdependencybyindex(index)
		elif args[0] == "pop":
			Project.behavior_pack.remdependencypop()
		elif args[0] == "all":
			Project.behavior_pack.remdependencyall()
elif typepack == "-rp":
	if option == "-dependency":
		if args[0].isdigit():
			index = int(args[0])
			Project.resource_pack.remdependencybyindex(index)
		elif args[0] == "pop":
			Project.resource_pack.remdependencypop()
		elif args[0] == "all":
			Project.resource_pack.remdependencyall()
else:
	Util.error("opcao '{}' invalido".format(typepack))