import Project
import Util
from sys import argv

name = argv[1]
opt  = argv[3]

build = {
	"name":name,
	"version":[0,0,1],
	"sources":[]
}
if opt == "-bp":
	build["sources"].append({"identifier":"behavior_pack-manifest","src":f"{name}_behavior_pack/manifest.json"})
	Project.behavior_pack.init(name)
elif opt == "-rp":
	build["sources"].append({"identifier":"resource_pack-manifest","src":f"{name}_resource_pack/manifest.json"})
	Project.resource_pack.init(name)
else:
	build["sources"].append({"identifier":"behavior_pack-manifest","src":f"{name}_behavior_pack/manifest.json"})
	build["sources"].append({"identifier":"resource_pack-manifest","src":f"{name}_resource_pack/manifest.json"})

	Project.behavior_pack.init(name)
	Project.resource_pack.init(name)

Util.writejson("build.json",build)