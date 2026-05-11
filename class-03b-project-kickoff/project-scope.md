# Escopo do Projeto de Pesquisa — Documento Vivo

> Preenchido durante o **Milestone 01** (kickoff). Atualizado sempre que decisões mudarem ao longo do curso. Última
> atualização: _AAAA-MM-DD_
>
> **Issue espelho no GitHub**: <https://github.com/Rafamsa/beedentidade/issues/2>
>
> **Status do preenchimento**:
>
> - Bloco A: **parcial** — confirmado volume bruto; falta formato técnico, metadados, rotulagem, storage.
> - Bloco B: **quase completo** — espécies, sinal, hardware definidos; falta modelo do mic, distância, replicação.
> - Bloco C: **vazio** — fechar na sessão do milestone.

______________________________________________________________________

## Convenção de papéis

Cada item pendente tem uma tag de responsável:

| Tag | Quem | O quê | | --- | --- | --- | | **[N]** | Nilton (professor/mentor) | Código, scripts, ferramentas
técnicas, decisões de engenharia | | **[R]** | Rafael (mestrando) | Campo, biologia, contato com a Marina, execução de
experimentos, escrita | | **[M]** | Marina (orientadora) | Direção científica, hipóteses biológicas | | **[R+M]** |
Rafael alinha com Marina | Decisões que dependem de orientação biológica | | **[sessão]** | Decidido junto na aula |
Itens fechados ao vivo durante o milestone |

> Premissa: **o desenvolvimento é majoritariamente do Rafael**. O Nilton entra como apoio técnico, principalmente em
> código que viabiliza/acelera a pesquisa (scripts de extração, baselines de ML, infraestrutura). Decisões biológicas e
> metodológicas são do Rafael + Marina.

______________________________________________________________________

## Identificação

- **Pesquisador**: Rafael Martins da Silva Afeto (MARTINS-AFETO, R.S.)
- **Orientadora**: Marina Wolowski Torres
- **Programa**: Mestrado em Ciências Ambientais — UNIFAL/MG
- **Título de trabalho**: _Identificação de abelhas via pistas acústicas com Aprendizado de Máquina_

______________________________________________________________________

## Bloco A — Inventário do Dataset

### Volume

- **Origem do dataset atual**: Meliponário/Apiário USP-RP (Ribeirão Preto/SP). Gravações de Alfenas/MG **descartadas e
  serão refeitas** — fora do escopo desta versão.
- **Duração média por espécie**: ~30 min de áudio bruto
- **Total bruto estimado**: ~30 min × 9 classes ≈ **270 min ≈ 4,5h**
- **[N]** Número de arquivos (script: contar arquivos por pasta/espécie)
- **[N]** Espaço em disco (script: somar bytes)

### Formato técnico — extração programática

> **[N]** Esses 4 campos serão preenchidos pelo script de inspeção de metadados (`scripts/inspect_audio.py`), rodando
> `soundfile.info()` ou equivalente em todos os arquivos. Saída: CSV com uma linha por arquivo.

- **[N]** Formato de arquivo (WAV / FLAC / MP3)
- **[N]** Sample rate (Hz)
- **[N]** Bit depth (16 / 24)
- **[N]** Canais (mono / estéreo)

### Metadados disponíveis

- **[R]** Data da gravação (campo / planilha de campo)
- **[R]** Hora da gravação (campo / planilha de campo)
- **[R]** Local (GPS ou texto) — provavelmente USP-RP para tudo
- **[R]** Temperatura na hora da coleta
- **[R]** Condição climática
- **[R]** Identificação do indivíduo (se aplicável)
- **[R+M]** Tamanho corporal do indivíduo gravado (medição direta ou referência média da espécie?)
- **[R]** Outros: \_\_\_\_\_

### Rotulagem por espécie

- **[R]** Já existe rotulagem? sim / parcial / não — provavelmente sim, por arquivo/pasta
- **[R]** Formato dos rótulos: nome de arquivo / planilha CSV / Audacity / Raven / outro
- **[N]** Parser do formato de rotulagem (script: ler labels e juntar com inventário de áudio)
- **[R]** Quem rotulou? (Rafael durante a coleta, presumivelmente)
- **[R+M]** Confiança da rotulagem (alta / média / baixa)

### Armazenamento

- **[R]** Localização física dos arquivos (notebook do Rafael? NAS? Drive?)
- **[R]** Backup? sim / não — onde: \_\_\_\_\_
- **[N]** Definir layout final de pastas no projeto (`data/raw/<species>/<file>.wav`?)

______________________________________________________________________

## Bloco B — Domínio e Protocolo

### Espécies gravadas (confirmadas — [R])

9 classes — 8 espécies + 1 variante de sexo. **Apenas _A. mellifera_ tem ferrão**; o resto é Meliponini.

| # | Nome popular | Nome científico | Sexo | Captura | Tribo | | --- | --- | --- | --- | --- | --- | | 1 | Abelha
europeia | _Apis mellifera_ | fêmea | microfone externo (shotgun) | Apini | | 2 | Borá | _Tetragona clavipes_ | fêmea |
microfone externo (shotgun) | Meliponini | | 3 | Mirim | _Plebeia droryana_ | fêmea | gravador direto | Meliponini | | 4
| Jataí | _Tetragonisca angustula_ | fêmea | gravador direto | Meliponini | | 5 | Mandaçaia | _Melipona quadrifasciata_
| fêmea | gravador direto | Meliponini | | 6 | Marmelada-amarela | _Frieseomelitta varia_ | fêmea | gravador direto |
Meliponini | | 7 | Tubuna | _Scaptotrigona bipunctata_ | fêmea | gravador direto | Meliponini | | 8 | Abelha-canudo |
_Scaptotrigona depilis_ | fêmea | gravador direto | Meliponini | | 9 | Abelha-canudo | _Scaptotrigona depilis_ |
**macho** | gravador direto | Meliponini |

**Pontos de atenção**:

- _A. mellifera_ é **outgroup acústico** (única Apini, com ferrão, corpo maior) — esperamos que seja a mais fácil de
  separar. Sanity check: se _Apis_ aparecer confundida com meliponínea, há bug no pipeline.
- _S. depilis_ tem fêmea e macho → **sub-pergunta de dimorfismo acústico inter-sexo**. Pode virar análise paralela.
- Dois _Scaptotrigona_ coexistem no pool (_S. bipunctata_ e _S. depilis_ fêmea) → caso difícil potencial; testar a
  confusão entre congenéricos.

### Espécies-alvo no escopo da tese

- **Escopo atual (USP-RP)**: as 9 acima.
- **[R+M]** Após recaptura em MG: definir quais espécies acrescentar — provavelmente espécies de Mata Atlântica ausentes
  em RP.

### Tipo de sinal gravado

- [x] Voo livre / som da abelha sem flor — **[R]** confirmar
- [ ] Sonicação em flor — **[R]** se aplicável, qual planta?
- [ ] Dentro da colmeia
- [ ] Outro: \_\_\_\_\_

> **[R]** Confirmar: o som gravado é **voo livre** capturado no meliponário/apiário, ou tem componente de sonicação em
> flor? A literatura compara explicitamente os dois (BuzzTrap, Ribeiro) — saber qual estamos usando muda a
> comparabilidade.

### Hardware e protocolo

- **Gravador**: **Zoom H4n Handy Recorder** (portátil). ⭐ Mesmo modelo do Ferreira et al. 2023 (Chile) — comparabilidade
  direta com a literatura.
- **Microfone externo**: shotgun unidirecional — **[R]** confirmar modelo.
- **Quando o microfone externo foi usado?** Em _A. mellifera_ e _T. clavipes_. Demais espécies: gravador direto
  (cápsulas built-in do H4n).
- **[R]** Distância microfone–abelha (cm; padronizada? sim / não)
- **[R]** Tempo médio por sessão de campo
- **[R]** Tem replicação biológica (mesmo indivíduo/colônia em dias diferentes)?

### Viéses conhecidos / candidatos

- **Protocolo de captura misto** (microfone externo vs gravador direto): variável de confusão potencial. Se o
  classificador aprender a distinguir o **protocolo** em vez da **espécie**, _A. mellifera_ + _T. clavipes_ virão
  separadas do resto sem que isso signifique nada biológico. **[sessão]** Decisão pra Bloco C.
- **Viés geográfico**: tudo USP-RP. Generalização para outros locais é hipótese aberta.
- **[R]** Viés temporal/sazonal: gravações concentradas em uma janela?

______________________________________________________________________

## Bloco C — Decisões Técnicas (fechadas na aula)

> Tudo aqui é **[sessão]** salvo indicação contrária.

### Tarefa principal

- [ ] Classificação multi-classe 9 vias (todas as classes contra todas)
- [ ] Classificação multi-classe 8 vias (juntar _S. depilis_ macho + fêmea como uma espécie)
- [ ] Classificação binária (ex.: _Apis_ vs Meliponini — outgroup test)
- [ ] Sub-análise: _S. depilis_ fêmea vs macho (dimorfismo)
- [ ] Regressão (predizer tamanho corporal a partir do som)
- [ ] Outra: \_\_\_\_\_

**Justificativa da escolha**: \_\_\_\_\_

### Nível taxonômico

- [ ] Espécie (default; o que temos rotulado)
- [ ] Gênero (testar agrupando os 2 _Scaptotrigona_)
- [ ] Tribo (Apini vs Meliponini → tarefa binária trivial)

### Sinal de entrada

- [ ] Voo (provável, **[R]** confirmar)
- [ ] Sonicação
- [ ] Ambos
- [ ] Hive-internal

### Tratamento da variável de confusão "protocolo de captura"

- [ ] Ignorar e ver se o classificador é robusto (perigoso)
- [ ] Codificar protocolo como feature explícita
- [ ] Avaliar com hold-out estratificado por protocolo (mais conservador)
- [ ] Re-gravar _A. mellifera_ + _T. clavipes_ com gravador direto (caro) — **[R+M]**

### Hipóteses iniciais — [R+M]

- \_\_\_\_\_ (ex.: "_Apis_ será trivialmente separada das meliponíneas")
- \_\_\_\_\_ (ex.: "os dois _Scaptotrigona_ serão o par mais difícil")
- ______________________________________________________________________

### Métrica de sucesso primária

- [ ] Acurácia (não recomendado — 9 classes possivelmente desbalanceadas)
- [ ] **Macro-F1** (recomendado)
- [ ] Recall ponderado por raridade
- [ ] Outro: \_\_\_\_\_

### Baseline desejado

- **[R+M]** Mínimo aceitável: \_\_\_\_\_ %
- **Referências da literatura usada como âncora** (ver
  [RESEARCH.md §3](../RESEARCH.md#3-estudos-brasileiros--n%C3%BAcleo-central--priorizar)):
  - BuzzTrap (5 espécies, RF, voo): **90,9%**
  - Ribeiro 2021 (15 espécies, SVM, sonicação): **73,4%**
  - Com 9 classes, interpolando: ~80% é plausível como teto inicial.

### Versionamento de dados — [N]

- [ ] Git LFS (limite 1 GB grátis no GitHub — provavelmente OK se WAVs forem comprimidos para FLAC)
- [x] DVC (mais sério, mais setup)
- [ ] Pasta externa (Drive / nuvem / NAS) fora do repo
- [ ] Outra: \_\_\_\_\_

______________________________________________________________________

## Scripts e ferramentas a desenvolver — [N]

Compromisso técnico do Nilton para destravar o trabalho do Rafael. Vão para o repositório da pesquisa (`beedentidade`,
não este repo do curso).

| Script | Função | Prioridade | Status | | --- | --- | --- | --- | | `inspect_audio.py` | Lê todos os arquivos, emite
CSV com sample rate, bit depth, channels, duração, tamanho, formato | Alta — destrava Bloco A | 🔜 | | `segment_audio.py`
| Quebra cada arquivo em janelas (0,5–2s, overlap configurável). Remove silêncio com VAD ou threshold de energia | Alta
— destrava feature extraction | 🔜 | | `extract_features.py` | Extrai MFCC (e opcionalmente mel-spectrogram, ZCR, RMS)
por segmento. Saída: parquet ou CSV | Média — depois do segment | 🔜 | | `baseline_classifier.py` | RF/SVM sobre MFCC
médio. Train/test split estratificado por espécie e por protocolo. Macro-F1 + confusion matrix | Média — primeira
validação | 🔜 | | `plot_dataset_overview.py` | Mosaico de espectrogramas (1 por classe), distribuições de duração/sample
rate por classe | Baixa — relatório/figura | 🔜 |

### Princípios

- **CLI primeiro**: todo script roda standalone com argumentos (não notebook). Notebook é só visualização.
- **Idempotente**: rodar 2× não muda nada (skip se output existe, ou flag `--overwrite`).
- **Reprodutível**: `random_state=42` em todo lugar, versões pinned no `pyproject.toml`.
- **Sem assumir o ambiente do Rafael**: se rodar na máquina dele, roda. Documentar setup mínimo.

______________________________________________________________________

## Mapa Curso ↔ Projeto

O que cada aula seguinte do **curso de mentoria** entrega para o **projeto de tese**:

| Aula | Tópico | O que entrega para o projeto | | --- | --- | --- | | 04 | Regressão Logística | Primeiro classificador
binário sério (ex.: _Apis_ vs Meliponini), com probabilidades e curva ROC | | 05 | Random Forest | Classificador
multi-classe 9 vias, alinhado com BuzzTrap; feature importance dos MFCCs | | 06 | SVM | Comparação com RF; kernel
não-linear; teste no par difícil (_Scaptotrigona_ spp.) | | 07 | Clustering | K-Means sobre MFCC sem rótulos → ver se os
clusters caem nas espécies certas | | 08 | PCA / t-SNE | Visualização 2D do espaço acústico das 9 classes; sub-análise
_S. depilis_ fêmea vs macho | | 09 | Avaliação rigorosa | Cross-validation estratificada por protocolo + espécie;
comparação formal RF vs SVM vs LR |

______________________________________________________________________

## Lacunas conhecidas (a resolver até o próximo milestone)

- [ ] **[R]** Confirmar modelo exato do microfone shotgun
- [ ] **[N]** Rodar `inspect_audio.py` e completar Bloco A — formato técnico
- [ ] **[R]** Confirmar tipo de sinal (voo livre? sonicação? combinado?)
- [ ] **[sessão]** Decidir tratamento da variável "protocolo de captura"
- [ ] **[R+M]** Recapturar dataset de Alfenas/MG
