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

## Registros cadastrados

### Homebrew — Apollo Save Tool v2.4.0

Publicado pelo desenvolvedor original [bucanero](https://github.com/bucanero/apollo-ps4).

- Arquivo: `IV0000-APOL00004_00-APOLLO0000000PS4.pkg`
- Tamanho: 22.806.528 bytes
- Licença do projeto: GPL-3.0-or-later
- SHA-256 publicado pelo GitHub: `ec34add4d2857fa3c947ed5666735a5c35ddb3e47d8be925b36e9ad408f7c090`
- [Lançamento oficial](https://github.com/bucanero/apollo-ps4/releases/tag/v2.4.0)

### Aplicativos — Remote PKG Installer NextGen v0.0.10

Aplicativo GPL-3.0 de [AldySan](https://github.com/AldySan/ps4_remote_pkg_installer_nextgen), que recebe transferências de PKG pela rede local e usa o gerenciador BGFT do PS4.

- Arquivo: `RemotePkgInstallerNextGen-0.0.10.pkg`
- Tamanho: 6.619.136 bytes
- SHA-256 publicado pelo GitHub: `b5056590f8c114335d06477a4833503507a38aaeef1550a0b0672ea5fb13f057`
- [Lançamento oficial](https://github.com/AldySan/ps4_remote_pkg_installer_nextgen/releases/tag/v0.0.10)
- O README do projeto cita teste em firmware 13.50; compatibilidade com outras versões precisa ser testada.

### Emuladores — PS4 GB-JIT v1.0.0

Emulador de Game Boy (DMG-01) de [uomar8](https://github.com/uomar8/ps4-gb-jit), com recompilador JIT, interface nativa e suporte a ROMs próprias do usuário.

- Arquivo: `PS4-GB-JIT-v01.06.pkg`
- Tamanho: 8.192.000 bytes
- SHA-256 publicado pelo GitHub: `3c65b808a78eb5c9a716681d58b48d03fd21cb61c90c57447b1e6f8ad7a4b2f6`
- [Lançamento oficial](https://github.com/uomar8/ps4-gb-jit/releases/tag/v1.0.0)
- **Atenção:** o repositório consultado não declara uma licença de software. O catálogo apenas aponta para o lançamento oficial do autor; o PKG não é espelhado aqui. Obtenha confirmação do autor antes de qualquer redistribuição ou hospedagem própria.

O cliente atual valida tamanho e cabeçalho PKG durante o download, mas ainda não verifica o SHA-256 integralmente. Os hashes acima são os publicados pela API de Releases do GitHub, não uma verificação byte a byte feita pelo cliente GAME ROOM BR.

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
