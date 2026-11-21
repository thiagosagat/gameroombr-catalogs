# GAME ROOM BR — catálogos públicos

Este repositório contém os arquivos JSON consumidos pelo aplicativo GAME ROOM BR para PS4. O código-fonte do aplicativo e o site comercial ficam em repositórios separados.

## Estrutura usada pelo aplicativo

As cinco categorias principais da loja são PS1, PS2, PS4, APLICATIVOS e HOMEBREW. Os arquivos abaixo são fontes/subcatálogos ligados a essas categorias:

| Arquivo | Uso na loja |
|---|---|
| `ps1.json` | Jogos de PS1 |
| `ps2.json` | Jogos de PS2 |
| `ps4.json` | Jogos de PS4 |
| `ps4/dlc.json` | DLCs de PS4 |
| `ps4/updates.json` | Atualizações de PS4 |
| `ps4/demos.json` | Demos de PS4 |
| `ps4/themes.json` | Temas de PS4 |
| `ps4/psp.json` | Conteúdo PSP exibido no submenu de PS2 |
| `homebrew.json` | Aplicativos e projetos Homebrew |
| `apps.json` | Aplicativos |
| `ps4/emulators.json` | Emuladores exibidos no submenu de Aplicativos |

Os arquivos usam o formato FPKGi nativo: objeto raiz `DATA`, com cada chave contendo uma URL HTTPS direta para um arquivo `.pkg`. Os campos `name` e `size` são obrigatórios; `size` é o tamanho exato em bytes.

## Primeiro item Homebrew

O catálogo `homebrew.json` inclui o Apollo Save Tool v2.4.0, publicado pelo desenvolvedor original [bucanero](https://github.com/bucanero/apollo-ps4).

- Página oficial: https://github.com/bucanero/apollo-ps4
- Lançamento: https://github.com/bucanero/apollo-ps4/releases/tag/v2.4.0
- Arquivo: `IV0000-APOL00004_00-APOLLO0000000PS4.pkg`
- Tamanho registrado na API de Releases: 22.806.528 bytes
- Licença declarada pelo projeto: GNU GPL v3 ou posterior
- SHA-256 publicado na API de Releases: `ec34add4d2857fa3c947ed5666735a5c35ddb3e47d8be925b36e9ad408f7c090`

O endereço de download aponta para a publicação oficial do desenvolvedor. O cliente atual valida tamanho e cabeçalho PKG, mas ainda não verifica o SHA-256 integralmente.

## Validação automática

A cada atualização em `main` ou Pull Request para `main`, o GitHub Actions executa:

1. Testes unitários do validador.
2. Verificação de todos os arquivos JSON.
3. Verificação da estrutura `DATA`, URLs HTTPS terminadas em `.pkg`, campos obrigatórios, tamanhos, hashes declarados e URLs duplicadas.

Para executar localmente:

```bash
python -m unittest discover -s tests -v
python scripts/validate_catalogs.py
```

**Limitação:** essa validação verifica a estrutura e o formato dos endereços. Ela não baixa os PKGs nem confirma que o servidor remoto continua disponível ou que o conteúdo do arquivo corresponde ao tamanho/hash publicado.

## Regras para novos cadastros

1. Use uma fonte oficial do desenvolvedor ou um espelho com autorização documentada.
2. Confirme a permissão de redistribuição quando o arquivo for hospedado por nós.
3. Use um link HTTPS direto para um arquivo `.pkg`.
4. Preencha `name` e `size` com valores conferidos.
5. Inclua autoria, licença e origem quando aplicável.
6. Não inclua jogos comerciais ou conteúdo protegido sem autorização.

## Endereços usados pelo PS4

Todos os catálogos são publicados como arquivos Raw do GitHub no branch `main`:

- PS1: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps1.json
- PS2: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps2.json
- PS4: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps4.json
- Aplicativos: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/apps.json
- Homebrew: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/homebrew.json
