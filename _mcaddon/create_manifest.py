from os import getcwd
from sys import argv
from uuid import uuid4

src = argv[1]
bin = argv[2]
opt = argv[3]

class project:
	name = getcwd().split("/")[-1]
	class behavior_pack:
		description = ""
		uuid = ""
		modules = ""
		dependencies = ""
		def addmodule(self,type):
			pass
	class resource_pack:
		description = ""
		uuid = ""
		modules = ""
		dependencies = ""
		

def info(m):
	print(f"[info] {m}")

info(f"criando arquivo em '{src}'")

arq_template_manifest_behaviorpack_base   = open(f"{bin}/_mcaddon/template/behavior_pack/manifest/base.json","r")
arq_template_manifest_behaviorpack_script = open(f"{bin}/_mcaddon/template/behavior_pack/manifest/modules/script.json","r")

template_manifest_behaviorpack_base = arq_template_manifest_behaviorpack_base.read()
template_manifest_behaviorpack_script = arq_template_manifest_behaviorpack_script.read()

#procesando uuid
if opt == "-bp":
	project.behavior_pack.uuid = str(uuid4())
elif opt == "-rp":
	project.resource_pack.uuid = str(uuid4())
else:
	project.behavior_pack.uuid = str(uuid4())
	project.resource_pack.uuid = str(uuid4())

#procesando modules
linhas = template_manifest_behaviorpack_script.split("\n")
for linha in linhas:
	project.behavior_pack.modules += "\t\t" + linha + "\n"
#procesando dependencies

template_manifest_behaviorpack_base = template_manifest_behaviorpack_base.replace("%project.name",project.name)
template_manifest_behaviorpack_base = template_manifest_behaviorpack_base.replace("%project.behavior_pack.uuid",project.behavior_pack.uuid)
template_manifest_behaviorpack_base = template_manifest_behaviorpack_base.replace("%project.behavior_pack.description",project.behavior_pack.description)
template_manifest_behaviorpack_base = template_manifest_behaviorpack_base.replace("%project.behavior_pack.modules",project.behavior_pack.modules)
template_manifest_behaviorpack_base = template_manifest_behaviorpack_base.replace("%project.behavior_pack.dependencies",project.behavior_pack.dependencies)

print(template_manifest_behaviorpack_base)
arq_template_manifest_behaviorpack_base.close()

#arq = open(src,"w")

#arq.close()
