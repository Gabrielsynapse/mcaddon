# Comando `mcaddon`

## Usage: `mcaddon [options] [args...]`

Esse comando auxilia no desenvolvimento de addons para minecraft
cria estruturas e empacota addon para o teste

### Considerações importantes
* Esse comando foi criado para ser instalado no termux

### Dependências

Para que esse comando funcione corretamente, algumas instalações são nescessarias
* python v3.12.9

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
mcaddon . myaddon
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

#### `-add`
Deve adicionar um recurso ao pacote

**Uso:** `mcaddon -add <type_pack> <option> [args...]`

**Parâmetros:**
* `<type_pack>`: tipo do pacote -bp ou -rp
* `<option>`: opcao de qual tipo de recurso deve adicionar
* `[args...]`: argumentos para option

**Exemplos:**

para adicionar recurso de dependência em behavior_pack execute:
```
mcaddon -add -bp -dependency [rp | bp] uuid4
```

para adicionar recurso de dependência em resource_pack execute:
```
mcaddon -add -rp -dependency [rp | bp] uuid4
```

#### `--help`
Mostra um helper na saida

**Uso:** `mcaddon --help`

#### `--version`
mostra a versao do comando

**Uso:** `mcaddon --version`