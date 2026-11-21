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

### Aplicativos

Os três pacotes abaixo são apontados diretamente para os lançamentos oficiais dos respectivos desenvolvedores. Os tamanhos e hashes são os metadados publicados pela API de Releases do GitHub.

#### Remote PKG Installer NextGen v0.0.10

Aplicativo GPL-3.0 de [AldySan](https://github.com/AldySan/ps4_remote_pkg_installer_nextgen), para receber transferências de PKG pela rede local e usar o gerenciador BGFT do PS4.

- Arquivo: `RemotePkgInstallerNextGen-0.0.10.pkg`
- Tamanho: 6.619.136 bytes
- SHA-256 oficial: `b5056590f8c114335d06477a4833503507a38aaeef1550a0b0672ea5fb13f057`
- [Lançamento oficial](https://github.com/AldySan/ps4_remote_pkg_installer_nextgen/releases/tag/v0.0.10)

#### Playfin v2.3.1

Cliente Jellyfin para PS4, publicado por [LowganDev](https://github.com/LowganDev/PlayfinPS4), com reprodução de mídia, música e TV ao vivo.

- Arquivo: `IV0001-PLFN00000_00-PLFN000000100000.pkg`
- Tamanho: 54.722.560 bytes
- Licença: GPL-3.0
- O lançamento oficial inclui o pacote de fontes correspondente (`playfin-2.3.1-sources.tar`), incluindo Playfin e as bibliotecas usadas na compilação.
- SHA-256 oficial: `f75c9fbbf17dab9ef1f1ca86995866aff73e13d0107063a8fd22a340d050ea9b`
- [Lançamento oficial](https://github.com/LowganDev/PlayfinPS4/releases/tag/2.3.1)

#### Librarian v01.00

Leitor nativo de Wikipedia/Kiwix, livros, quadrinhos, documentos e audiolivros, publicado por [jw-notes](https://github.com/jw-notes/Librarian).

- Arquivo: `IV0000-LIBR00001_00-LIBRARIANPS40000.pkg`
- Tamanho: 26.542.080 bytes
- Licença principal: GPL-3.0-or-later com termos adicionais na seção 7; MuPDF incluído sob AGPL-3.0.
- O lançamento oficial inclui os fontes correspondentes do Librarian, MuPDF e módulos OpenOrbis, além de `SHA256SUMS`.
- SHA-256 oficial: `df0b8b4fd4fedaa8bb530a3084bf46d48bafcd7c3cb32da4ed98a2c428ffaae1`
- [Lançamento oficial](https://github.com/jw-notes/Librarian/releases/tag/v01.00)

### Emuladores PS4

Todos os pacotes abaixo vêm do GitHub oficial do projeto/port para PS4. Os projetos declaram licenças GPL; a redistribuição deve preservar os avisos e disponibilizar o código-fonte correspondente e as licenças de terceiros aplicáveis.

#### DuckStation PS4 v00.03 — PlayStation

- Arquivo: `DuckStation-v00.03.pkg`
- Tamanho: 59.441.152 bytes
- Licença: GPL-3.0
- SHA-256 oficial: `f2647245aee92d202078a10fd60422fb19b9c31a1f0a70aeb4cec3258b72ba7c`
- [Código-fonte e lançamento oficial](https://github.com/NeomaMonroy/DuckStation-PS4/releases/tag/v00.03)

#### PPSSPP v0.3-a50bb197 — PSP

- Arquivo: `IV0000-PPSS00001_00-PPSSPPHOMEBREW00.pkg`
- Tamanho: 100.728.832 bytes
- Licença: GPL-2.0-or-later
- SHA-256 oficial: `9d6d8f8b8550ec7a84fcc7990a5b0abed1c43b7ab94c66e39581bc3a33afbea4`
- [Código-fonte e lançamento oficial](https://github.com/ps4-homebrew-dev/ppsspp/releases/tag/v0.3-a50bb197)

#### Flycast v0.2-7adbf3ca — Dreamcast, Naomi e Atomiswave

- Arquivo: `IV0000-FLYH00001_00-FLYCAST000000000.pkg`
- Tamanho: 81.330.176 bytes
- Licença: GPL-2.0-or-later
- SHA-256 oficial: `be0c52aee8358c55f999f506eef6b306a325952873e31cc88ffd5603028b2a07`
- [Código-fonte e lançamento oficial](https://github.com/ps4-homebrew-dev/flycast/releases/tag/v0.2-7adbf3ca)

#### DolphinPS4 v04.19 — GameCube e Wii

- Arquivo: `DolphinPS4-v04.19.pkg`
- Tamanho: 206.831.616 bytes
- Licença: GPL-2.0-or-later
- SHA-256 oficial: `c97e8790a51f496dd7849fa837ef61f15290ba8f5bd73cfe090a07cf2f959650`
- [Código-fonte e lançamento oficial](https://github.com/iHaiDeeZ/DolphinPS4/releases/tag/v04.19)

#### Harissa64 v0.3.1 — Nintendo 64

- Arquivo: `Harissa64-PS4-0.3.1.pkg`
- Tamanho: 31.522.816 bytes
- Licença principal: GPL-2.0; componentes de terceiros seguem as licenças descritas em `THIRD_PARTY.md`.
- SHA-256 oficial: `88007ec5de209a0ad605c053bd5c84d6b1722aff6977f9b7c88230d8a944cef8`
- [Código-fonte e lançamento oficial](https://github.com/kernel64/Harissa64-PS4/releases/tag/v0.3.1)

#### Item aguardando autorização/licença — PS4 GB-JIT

O GB-JIT v1.0.0 foi retirado do catálogo ativo porque o repositório do autor consultado não declara uma licença de software. O tamanho e o hash do pacote são conhecidos, mas isso, por si só, não concede permissão para redistribuição. O item só deve voltar após publicação de uma licença compatível ou confirmação explícita do titular dos direitos.

## Critério de inclusão e distribuição

1. A URL do PKG deve apontar para um lançamento oficial do desenvolvedor ou para um espelho com autorização documentada.
2. O tamanho deve ser confirmado em bytes nos metadados do lançamento.
3. A licença deve permitir redistribuição do programa. Para GPL/AGPL, é necessário preservar avisos, fornecer a licença e garantir acesso ao código-fonte correspondente conforme os termos aplicáveis.
4. O catálogo aponta diretamente para os lançamentos dos autores; não mantém cópias dos PKGs. Qualquer futura hospedagem/espelhamento pela GAME ROOM BR exige cumprir as obrigações de cada licença e dos componentes de terceiros.
5. Não incluir jogos comerciais, BIOS, ROMs ou outros conteúdos protegidos sem autorização.

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

**Limitação:** essa validação verifica a estrutura e o formato dos endereços. Ela não baixa os PKGs nem confirma que o servidor remoto continua disponível ou que os bytes do arquivo correspondem ao tamanho/hash publicado. O cliente atual confere o tamanho recebido e o cabeçalho PKG, mas ainda não valida integralmente o SHA-256 durante o download.

## Endereços usados pelo PS4

Todos os catálogos são publicados como arquivos Raw do GitHub no branch `main`:

- PS1: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps1.json
- PS2: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps2.json
- PS4: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps4.json
- Aplicativos: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/apps.json
- Emuladores PS4: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/ps4/emulators.json
- Homebrew: https://raw.githubusercontent.com/thiagosagat/gameroombr-catalogs/main/homebrew.json
