import os
import Util
from uuid import uuid4

def load(_json):
	srcMbp = Util.listdict.get(_json["sources"],"identifier","behavior_pack-manifest")
	srcMrp = Util.listdict.get(_json["sources"],"identifier","resource_pack-manifest")
	
	if srcMbp != dict():
		behavior_pack.manifest = Util.readjson(srcMbp["src"])
	if srcMrp != dict():
		resource_pack.manifest = Util.readjson(srcMrp["src"])

class behavior_pack:
	manifest = {
		"format_version":2,
		"header":{
			"name":"",
			"description":"",
			"uuid":"",
			"version":[0,0,1],
			"min_engine_version":[1,19,0]
		},
		"modules":[],
		"dependencies":[]
	}
	def adddependency(_type,_uuid):
		if _type == "rp" or "bp":
			dependency = {
				"uuid":_uuid,
				"version":[0,0,1]
			}
			behavior_pack.manifest["dependencies"].append(dependency)
	def init(_name):
		src = _name+"_behavior_pack"
		behavior_pack.manifest["header"]["name"] = _name
		behavior_pack.manifest["header"]["description"] = ""
		behavior_pack.manifest["header"]["uuid"] = str(uuid4())
		
		Util.mkdir(src)
		Util.writejson(src+"/manifest.json",behavior_pack.manifest)

class resource_pack:
	manifest = {
		"format_version":2,
		"header":{
			"name":"",
			"description":"",
			"uuid":"",
			"version":[0,0,1],
			"min_engine_version":[1,19,0]
		},
		"modules":[],
		"dependencies":[]
	}
	def adddependency(_type,_uuid):
		if _type == "rp" or "bp":
			dependency = {
				"uuid":_uuid,
				"version":[0,0,1]
			}
			resource_pack.manifest["dependencies"].append(dependency)

	def init(_name):
		src = _name+"_resource_pack"
		resource_pack.manifest["header"]["name"] = _name
		resource_pack.manifest["header"]["description"] = ""
		resource_pack.manifest["header"]["uuid"] = str(uuid4())
		
		Util.mkdir(src)
		Util.writejson(src+"/manifest.json",resource_pack.manifest)
