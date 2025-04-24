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
	def getEnableCapabilities():
		return "capabilities" in behavior_pack.manifest
	def setEnableCapabilities(_enabled):
		if behavior_pack.getEnableCapabilities():return None
		if _enabled:
			behavior_pack.manifest["capabilities"] = [
				"script_eval",
				"editorExtension",
				"chemistry",
				"experimental_custom_ui"
			]
		else:
			behavior_pack.manifest.pop("capabilities")
		behavior_pack.save()
	def save():
		src = Util.listdict.get(Util.readjson("build.json")["sources"],"identifier","behavior_pack-manifest")["src"]
		Util.writejson(src,behavior_pack.manifest)
	def remdependencyall():
		behavior_pack.manifest["dependencies"].clear()
		behavior_pack.save()
	def remdependencypop():
		behavior_pack.manifest["dependencies"].pop()
		behavior_pack.save()
	def remdependencybyindex(_index):
		d = behavior_pack.manifest["dependencies"]
		d.remove(d[_index])
		behavior_pack.save()
	def adddependency(_type,_uuid=None):
		dependency = dict()
		if _type in ["rp","bp"]:
			dependency = {
				"uuid":_uuid,
				"version":[0,0,1]
			}
		elif _type in ["server","server-ui","common"]:
			dependency_dict = {
				"server":{
					"version": "1.14.0",
					"module_name":"@minecraft/server"
				},
				"server-ui":{
					"version": "1.3.0",
					"module_name": "@minecraft/server-ui"
				},
				"common":{
					"version": "1.2.0",
					"module_name": "@minecraft/common"
				}
			}
			dependency = dependency_dict[_type]
		behavior_pack.manifest["dependencies"].append(dependency)
		behavior_pack.save()
	def remmoduleall():
		behavior_pack.manifest["modules"].clear()
		behavior_pack.save()
	def remmodulepop():
		behavior_pack.manifest["modules"].pop()
		behavior_pack.save()
	def remmodulebyindex(_index):
		d = behavior_pack.manifest["modules"]
		d.remove(d[_index])
		behavior_pack.save()
	def addmodule(_type,_name):
		module = dict()
		if _type == "javascript":
			module = {
				"type":"script",
				"uuid":str(uuid4()),
				"version":[0,0,1],
				"entry":f"script/{_name}.js",
				"language":"javascript"
			}
		behavior_pack.manifest["modules"].append(module)
		behavior_pack.save()
	def init(_name):
		src = _name+"_behavior_pack"
		behavior_pack.manifest["header"]["name"] = _name
		behavior_pack.manifest["header"]["description"] = ""
		behavior_pack.manifest["header"]["uuid"] = str(uuid4())
		behavior_pack.manifest["modules"].append({
			"description": "",
			"type": "data",
			"uuid": str(uuid4()),
			"version": behavior_pack.manifest["header"]["version"]
		})
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
	def save():
		src = Util.listdict.get(Util.readjson("build.json")["sources"],"identifier","resource_pack-manifest")["src"]
		Util.writejson(src,resource_pack.manifest)
	def remdependencyall():
		resource_pack.manifest["dependencies"].clear()
		resource_pack.save()
	def remdependencypop():
		resource_pack.manifest["dependencies"].pop()
		resource_pack.save()
	def remdependencybyindex(_index):
		d = resource_pack.manifest["dependencies"]
		d.remove(d[_index])
		resource_pack.save()
	def adddependency(_type,_uuid=None):
		dependency = dict()
		if _type in ["rp","bp"]:
			dependency = {
				"uuid":_uuid,
				"version":[0,0,1]
			}
		resource_pack.manifest["dependencies"].append(dependency)
		resource_pack.save()
	def remmoduleall():
		resource_pack.manifest["modules"].clear()
		resource_pack.save()
	def remmodulepop():
		resource_pack.manifest["modules"].pop()
		resource_pack.save()
	def remmodulebyindex(_index):
		d = resource_pack.manifest["modules"]
		d.remove(d[_index])
		resource_pack.save()
	def addmodule(_type,_uuid):
		pass
	def init(_name):
		src = _name+"_resource_pack"
		resource_pack.manifest["header"]["name"] = _name
		resource_pack.manifest["header"]["description"] = ""
		resource_pack.manifest["header"]["uuid"] = str(uuid4())
		resource_pack.manifest["modules"].append({
			"description": "",
			"type": "resources",
			"uuid": str(uuid4()),
			"version": resource_pack.manifest["header"]["version"]
		})
		Util.mkdir(src)
		Util.writejson(src+"/manifest.json",resource_pack.manifest)
