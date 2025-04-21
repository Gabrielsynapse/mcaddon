#!/bin/sh

src="$PREFIX/bin/mcaddon"

ms_usage () {
	echo "opcao invalido: $1"
	cat $src/_mcaddon/usage.txt
	cat $src/_mcaddon/help.txt
}
ms_help () {
	echo "version: $( cat $src/_mcaddon/version.txt )"
	cat $src/_mcaddon/help.txt
}
ms_version () {
	echo "version: $( cat $src/_mcaddon/version.txt )"
}
error () {
	echo "[error] $1"
}
info () {
	echo "[info] $1"
}
ms_mkdir (){
	info "criando diretorio \"$1\""
	mkdir -p "$1"
}

init () {
	# se o source nao for diretorio:
	if [ ! -d "$1" ]; then
		error "o source \"$1\" nao e um diretorio ou nao existe em \"$PWD\""
		ms_usage "$1"
		exit
	fi
	cd "$1"
	name=$( python -c "src='$PWD';print(src[src.rindex('/')+1:].replace('/',''))" )
	#montando o behavior_pack
	#diretorios
	ms_mkdir $name"_behavior_pack/entities"
	ms_mkdir $name"_behavior_pack/functions"
	ms_mkdir $name"_behavior_pack/items"
	ms_mkdir $name"_behavior_pack/recipes"
	ms_mkdir $name"_behavior_pack/scripts"
	
	#manifest
	python "$src/_mcaddon/create_manifest.py" $name"_behavior_pack/manifest.json" "$src" "$2"
}
build () {
	name="$2.mcaddon"

	# se o source nao for diretorio:
	if [ ! -d "$1" ]; then
		error "o source \"$1\" nao e um diretorio ou nao existe em \"$PWD\""
		ms_usage "$1"
		exit
	fi
	cd "$1"
	zip -r "$name" *
	info "pack \"$name\" criado com sucesso!"
}
install () {
	#se arquivo nao existe:
	if [ ! -f "$1" ]; then
		exit
	fi
	info "instalando pack $1"
	termux-open --view "$1"
	#am start -a android.intent.action.VIEW -d file://$PWD/$1 -t application/zip

}
# mcaddon -start <source.[mcaddon | mcaddon]>
if [ "$1" = "-start" ] && [ ! -z "$2" ]; then
	install "$2"
elif [ "$1" = "-init" ] && [ ! -z "$2" ]; then
	init "$2" "$3"
elif [ "$1" = "-build" ] && [ ! -z "$2" ] && [ ! -z "$3" ]; then
	build "$2" "$3"
elif [ "$1" = "--help" ]; then
	ms_help
elif [ "$1" = "--version" ]; then
	ms_version
else
	ms_usage "$1"
fi
