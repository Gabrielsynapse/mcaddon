# Comando `mcaddon`

## Usage: `mcaddon [options] [args...]`

Esse comando auxilia no desenvolvimento de addons para minecraft
cria estruturas e empacota addon para o teste

### Considerações importantes
* Esse comando foi criado para ser instalado no termux

### Dependências

Para que esse comando funcione corretamente, algumas instalações são nescessarias
* nodejs v23.11.0

### opções

#### `-init`
Cria um projeto de addons com a estrutura básica como for especificado.

**Uso:** `mcaddon -init <source> <option>`

**Parâmetros:**

* `<source>`: Caminho absoluto ou relativo do diretorio do addon
* `<option>`: Opções quais estruturas deve criar.

**Exemplos:**

Para um pack completo execute:

```
mcaddon -init .
```

Para um pack somente de comportamento execute:
```
mcaddon -init . -bp
```

Para um pack somente de recursos execute:
```
mcaddon -init . -rp
```

#### `-build`
Compacta os recursos em um mcaddon

**Uso:** `mcaddon -build <source> <nomedopack>`

**Parâmetros:**

* `<source>`: caminho relativo ou absoluto do projeto
* `<nomedopack>`: nome do pack.

**Exemplos:**

Para compactar recursos no diretorio atual execute:
```
cd myaddon/
mcaddon -build . myaddon
```

#### `-start`
Essa opção deve instalar o pack ja empacotado

**Uso:** `mcaddon -start <source>`

**Parâmetros:**
* `<source>`: caminho relativo ou absoluto do pack empacotado

**Exemplos:**
Para instalar um pacote execute:
```
mcaddon -start ./caminho/myaddon.mcaddon
```

#### `-rem`
Deve remover um recurso ao pacote

**Uso** `mcaddon -rem <type_pack> <option> [args...]`

**Parâmetros:**
* `<type_pack>`: tipo do pacote -bp ou -rp
* `<option>`: opcao de qual tipo de recurso deve remover
* `[args...]`: argumentos para option

**Exemplos:**

para remover dependência do behavior_pack ou resource_pack no index 0 execute:
```
mcaddon -rem [-bp | -rp] -dependency 0
```

para remover todas as dependências do behavior_pack ou resource_pack execute:
```
mcaddon -rem [-bp | -rp] -dependency all
```

para remover o ultimo index do behavior_pack ou resource_pack execute:
```
mcaddon -rem [-bp | -rp] -dependency pop
```

#### `-add`
Deve adicionar um recurso ao pacote

**Uso:** `mcaddon -add <type_pack> <option> [args...]`

**Parâmetros:**
* `<type_pack>`: tipo do pacote -bp ou -rp
* `<option>`: opcao de qual tipo de recurso deve adicionar
* `[args...]`: argumentos para option

**Exemplos:**

para adicionar recurso de dependência para behavior_pack ou resource_pack em behavior_pack ou resource_pack execute:
```
mcaddon -add [-rp | -bp] -dependency [rp | bp] uuid4
```

para adicionar dependência de modulo para api script execute:
```
mcaddon -add -bp -dependency [server | server-ui | common]
```
isso tambem abilita "capabilities" para fazer operações avancadas com scripts

para adicionar um modulo de javascript com o nome name execute:
```
mcaddon -add -bp -module -javascript name
```

#### `-template`
Cria um template que é uma estrutura de exemplo

**Uso:** `mcaddon -template <name_template> <source> <name>`

**Parâmetros:**
* `<name_template>`: nome do template
* `<source>`: caminho do projeto
* `<nome>`: nome do projeto

**Exemplos:**

para criar um template de api-script no diretorio atual com o nome script execute:
```
mcaddon -template api-script . script
```

#### `-api-test`
Testa a apt script

**Uso:** `mcaddon -api-test <source>`

**Parâmetros:**
* `<source>`: caminho relativo ou absoluto ate o addon.mcaddon

**Exemplos:**

para executar um teste do seu addon execute:
```
mcaddon -api-test .
```

#### `--help`
Mostra um helper na saida

**Uso:** `mcaddon --help`

#### `--version`
mostra a versao do comando

**Uso:** `mcaddon --version`
