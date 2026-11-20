# GAME ROOM BR — catálogos públicos

Este repositório contém somente os arquivos JSON de catálogo consumidos pelo aplicativo GAME ROOM BR para PS4. O código-fonte do aplicativo e o site comercial não ficam aqui.

## Categorias

- `ps1.json` — PlayStation 1
- `ps2.json` — PlayStation 2
- `ps4.json` — PlayStation 4
- `homebrew.json` — aplicativos e projetos Homebrew
- `apps.json` — ferramentas e utilitários

Os arquivos usam o formato FPKGi nativo: objeto raiz `DATA`, em que cada chave é um link HTTPS direto para um arquivo `.pkg`. O campo `size` é obrigatório e deve informar o tamanho exato em bytes.

## Primeiro item Homebrew

O catálogo `homebrew.json` inclui o Apollo Save Tool v2.4.0, publicado pelo desenvolvedor original [bucanero](https://github.com/bucanero/apollo-ps4).

- Página oficial: https://github.com/bucanero/apollo-ps4
- Lançamento: https://github.com/bucanero/apollo-ps4/releases/tag/v2.4.0
- Arquivo: `IV0000-APOL00004_00-APOLLO0000000PS4.pkg`
- Tamanho declarado pela API de Releases: 22.806.528 bytes
- Licença declarada pelo projeto: GNU GPL v3 ou posterior
- SHA-256 publicado pela API de Releases: `ec34add4d2857fa3c947ed5666735a5c35ddb3e47d8be925b36e9ad408f7c090`

O endereço de download aponta para o lançamento oficial do projeto, não para uma cópia hospedada neste repositório. A loja valida o tamanho e o cabeçalho PKG, mas a verificação completa do SHA-256 ainda não é feita pelo cliente.

## Regras para novos cadastros

1. Use sempre uma fonte oficial do desenvolvedor ou um espelho com autorização documentada.
2. Confirme que a licença permite redistribuição ou que o link apenas referencia a distribuição oficial do autor.
3. Use um link HTTPS que termine em `.pkg` e que entregue o arquivo diretamente após os redirecionamentos.
4. Preencha `name` e `size`; use a data em `MM-DD-YYYY`.
5. Mantenha nome da licença, autoria e origem do projeto no objeto sempre que aplicável.
6. Não inclua jogos comerciais, conteúdo protegido sem autorização, arquivos modificados ou pacotes de procedência duvidosa.

## URLs consultadas pelo PS4

- PS1: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps1.json
- PS2: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps2.json
- PS4: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps4.json
- Homebrew: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/homebrew.json
- Aplicativos: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/apps.json
