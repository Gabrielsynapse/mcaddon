#!/bin/sh

src="$HOME/bin/mcaddon"
python () {
	$src/_mcaddon/_pyenv/bin/python $@
}

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
	#echo "[info] $1"
	echo -e "\033[1;49;32m[\033[34minfo\033[32m] $1\033[m"

}
ms_mkdir (){
	info "criando diretorio \"$1\""
	mkdir -p "$1"
}
apitest () {
	# se nao existir o arquivo:
	if [ ! -d "$1" ]; then
		error "source \"$1\" nao existe ou nao e um diretorio"
	fi
	source="$1"
	port="3030"
	cd "$1"
	python "$src/_mcaddon/apitest.py" "$source" "$src"
	info "abrindo o ambiente sair: ctl + d"
	
	#xdg-open "http://localhost:$port/"
	cd "$src/_mcaddon/api-test-temp"
	node -r ./index.js
}
rem () {
	# se nao existir o arquivo build.json no diretorio atual:
	if [ ! -f "./build.json" ]; then
		error "va ate o projeto ou crie no diretorio atual"
		exit
	fi
	python "$src/_mcaddon/rem.py" $@
}
add () {
	# se nao existir o arquivo build.json no diretorio atual:
	if [ ! -f "./build.json" ]; then
		error "va ate o projeto ou crie no diretorio atual"
		exit
	fi
	
	python "$src/_mcaddon/add.py" $@
}
init () {
	# se o source nao for diretorio:
	if [ ! -d "$1" ]; then
		error "o source \"$1\" nao e um diretorio ou nao existe"
		ms_usage "$1"
		exit
	fi
	cd "$1"
	name=$( python -c "src='$PWD';print(src[src.rindex('/')+1:].replace('/',''))" )

	python "$src/_mcaddon/make-addon.py" "$name" "$src" "$2"
}
template () {
	cd "$2"
	# se o source nao for diretorio:
	if [ ! -d "$2" ]; then
		error "o source \"$2\" nao e um diretorio ou nao existe"
		ms_usage "$2"
		exit
	fi
	src_template="$src/_mcaddon/template/$1.py"
	# se o template nao existir:
	if [ ! -f "$src_template" ]; then
		error "o template em \"$src_template\" nao existe"
		ms_usage
		exit
	fi
	name_template="$1"
	source="$2"
	name_project="$3"
	python "$src_template" "$source" "$name_project"
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
	zip -r "$name" *_behavior_pack *_resource_pack
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
elif [ "$1" = "-api-test" ] && [ ! -z "$2" ]; then
	apitest "$2"
elif [ "$1" = "-template" ] && [ ! -z "$2" ] && [ ! -z "$3" ] && [ ! -z "$4" ]; then
	template "$2" "$3" "$4"
elif [ "$1" = "-init" ] && [ ! -z "$2" ]; then
	init "$2" "$3"
elif [ "$1" = "-build" ] && [ ! -z "$2" ] && [ ! -z "$3" ]; then
	build "$2" "$3"
elif [ "$1" = "-rem" ] && [ ! -z "$2" ] && [ ! -z "$3" ] && [ ! -z "$4" ]; then
	shift
	rem $@
elif [ "$1" = "-add" ] && [ ! -z "$2" ] && [ ! -z "$3" ] && [ ! -z "$4" ]; then
	shift
	add $@
elif [ "$1" = "--help" ]; then
	ms_help
elif [ "$1" = "--version" ]; then
	ms_version
else
	ms_usage "$1"
fi
