# RESEARCH — Bioacústica de abelhas + ML

Compilação viva de referências para ancorar o conteúdo da mentoria no problema real do Rafael: **identificação de
espécies de abelha a partir de áudio**, com ênfase em espécies brasileiras (meliponíneos / *Bombus* / *Centris* / etc.).

Atualize livremente. Quando adicionar paper novo, prefira o formato `Autor Ano — título curto` com URL canônica (PMC >
DOI > preprint).

> **Onde ficam as decisões do projeto-tese**: este documento é **referencial** (literatura, contexto, dataset). As
> decisões metodológicas e o desenvolvimento da pesquisa do Rafael vivem em
> [github.com/Rafamsa/beedentidade](https://github.com/Rafamsa/beedentidade) como issues. Issue âncora atual:
> [#2 — Project Scope (Milestone 01)](https://github.com/Rafamsa/beedentidade/issues/2).

______________________________________________________________________

## 0. Sobre o pesquisador

**Rafael Martins da Silva Afeto** (cita como `MARTINS-AFETO, R.S.`) — mestrando em Ciências Ambientais na **UNIFAL/MG**,
orientado por **Marina Wolowski Torres**.

- **Lattes**: <http://lattes.cnpq.br/4438838867822049>
- **Blog / divulgação científica**: <https://rafamsa.github.io/>
- **Tese**: *Identificação de abelhas via pistas acústicas com Aprendizado de Máquina* (iniciada em 2025)

### Background relevante

| Área | Evidência | Implicação | | --- | --- | --- | | Bioacústica | Curso UNIFAL 30h (2021) + projeto anterior com
vocalização de seriemas *Cariama cristata* | Já entende gravação, espectrograma, segmentação manual | | Meliponicultura
| Embrapa Urbana (2022) + Embrapa Sem Ferrão (2023) + curso ministrado (2023) | Conhece bem as abelhas, biologicamente |
| Programação | Curso de Análise de Dados em R (ENAP, 2023) | R-user; **Python/sklearn é o gap a fechar** | |
Eletroeletrônica | Técnico SENAI (2018–2019) | Hardware (microfone, ADC, Raspberry Pi) não é barreira | | Comunicação
científica | Bolsista +Ciência (jornalista, 2024–2026, 40h/sem) + Inkscape (2023, 40h) | Visual learner; valoriza
diagramas e plots bem-feitos | | Inglês | TOEFL ITP B1 | Aulas em PT-BR; termos técnicos em EN ok; evitar parágrafos
longos em EN |

### Trabalho prévio diretamente análogo

> Projeto 2023–2024 (UNIFAL): *Individualidade e sinais honestos em vocalizações territoriais de seriemas Cariama
> cristata* — orient. Rogério Grassetto T. da Cunha. Range Finder + câmera para medir tamanho, microfone + gravador para
> captar vocalização, correlação tamanho ↔ assinatura individual.

Isso é metodologicamente irmão da tese: medir traço físico → comparar com assinatura acústica. A pergunta de tese só
troca "individualidade" por "espécie" e "seriema" por "abelha".

### Geografia da coleta de dados

As espécies-alvo da tese vivem em **duas regiões principais**:

1. **Alfenas / MG e entorno** (sul de Minas Gerais) — base do Rafael, raio de até ~3h de viagem. Inclui cidades vizinhas
   com mata atlântica preservada, fragmentos urbanos e áreas rurais. Bioma: Mata Atlântica + transição para Cerrado.
1. **Ribeirão Preto / SP** — Meliponário e Apiário da **USP/FFCLRP** (Faculdade de Filosofia, Ciências e Letras de
   Ribeirão Preto). Coleção viva de meliponíneos majoritariamente. Bioma: Cerrado (transição).

**Status**: parceria com a USP-RP **já estabelecida**, coletas realizadas. Coletas em **Alfenas/MG validadas** após
inspeção de áudio — 5 espécies confirmadas (ver §0.5.2 abaixo). **Overlap intencional** entre os dois sites em 3
espécies, abrindo espaço para análise de variação geográfica intra-específica.

**Implicação metodológica**:

- Dataset cobre **dois biomas / dois sites**: Cerrado (Ribeirão Preto) e Mata Atlântica + transição (Alfenas). Menos
  estreito do que a leva inicial sugeria, mas ainda SE-restrito — não generalizar para Amazônia/Caatinga.
- A USP/Ribeirão tem um dos meliponários mais antigos e bem documentados do país (linhagem Lucas Garófalo / Vera
  Imperatriz-Fonseca historicamente).
- "Espécies brasileiras" no contexto desta tese significa, na prática, **espécies do SE (Cerrado + Mata Atlântica)** —
  focar a literatura e os exemplos nessas. Estudos amazônicos (ex.: Yasuní, Ecuador) servem como contraste, não como
  baseline.
- O overlap de 3 espécies entre Alfenas e USP-RP permite, em princípio, testar se a assinatura acústica de uma mesma
  espécie é estável entre sites — análise paralela à classificação inter-específica.

______________________________________________________________________

## 0.5 Dataset em mãos

### 0.5.1 USP-RP (leva inicial)

#### Espécies gravadas

| Nome popular | Nome científico | Sexo | Captura | Aculeação | | --- | --- | --- | --- | --- | | Abelha europeia |
*Apis mellifera* | fêmea | microfone externo (shotgun) | com ferrão | | Borá | *Tetragona clavipes* | fêmea | microfone
externo (shotgun) | sem ferrão | | Mirim | *Plebeia droryana* | fêmea | gravador (direto) | sem ferrão | | Jataí |
*Tetragonisca angustula* | fêmea | gravador (direto) | sem ferrão | | Mandaçaia | *Melipona quadrifasciata* | fêmea |
gravador (direto) | sem ferrão | | Marmelada-amarela | *Frieseomelitta varia* | fêmea | gravador (direto) | sem ferrão |
| Tubuna | *Scaptotrigona bipunctata* | fêmea | gravador (direto) | sem ferrão | | Abelha-canudo | *Scaptotrigona
depilis* | fêmea | gravador (direto) | sem ferrão | | Abelha-canudo | *Scaptotrigona depilis* | **macho** | gravador
(direto) | sem ferrão |

**Total**: 8 espécies (7 meliponíneos + 1 *Apis*) + 1 variante de sexo (*S. depilis* macho).

#### Observações taxonômicas e metodológicas

- *Apis mellifera* é a **única com ferrão** no pool — o resto é Meliponini. Útil pra discussões iniciais (pertence a
  tribo diferente; é um "outgroup" acústico potencialmente mais fácil de separar).
- *S. depilis* aparece em **fêmea e macho**. Isso abre uma sub-pergunta natural: **a assinatura acústica difere entre
  sexos da mesma espécie?** Pode virar análise paralela à classificação inter-específica (relevante: machos voam
  diferente, são menores em algumas espécies e não fazem sonicação).
- Dois protocolos de captura coexistem (microfone externo vs gravador direto). Isso é uma **variável de confusão
  potencial** — *A. mellifera* e *T. clavipes* foram gravados de forma diferente do resto. Decisão pra Bloco C do
  milestone: tratar protocolo como feature, fazer balanceamento, ou re-gravar?

#### Hardware

- **Gravador**: **Zoom H4n Handy Recorder** (portátil). Mesmo modelo usado por Ferreira et al. 2023 no Chile — ⭐
  **excelente compatibilidade com a literatura**.
- **Microfone externo**: shotgun unidirecional (modelo a confirmar).
- Especificações do H4n nativas: até 24-bit / 96 kHz, 2 canais cardioides + 2 entradas XLR/TRS. Tipicamente gravações de
  campo saem em **WAV 16-bit / 44,1 ou 48 kHz**.

#### Volume e densidade

- **~30 min de gravação crua por espécie** (média). Para 9 classes ≈ **270 min ≈ 4,5h** brutas.

- Janelamento standard da literatura (ver §1): **0,5 a 2 segundos** por amostra (revisão MDPI 2024).

- Estimativa de segmentos disponíveis, antes de qualquer descarte de silêncio/ruído:

  | Janela | Overlap | Segmentos por espécie | Total (9 classes) | | --- | --- | --- | --- | | 1 s | 0% | 1.800 | 16.200
  | | 1 s | 50% | 3.600 | 32.400 | | 2 s | 0% | 900 | 8.100 | | 0,5 s | 0% | 3.600 | 32.400 |

- Mesmo descartando metade como silêncio/ruído, fica entre **4.000 e 16.000 segmentos úteis** — comparável a Ferreira
  2023 (3.595 segmentos, 16 espécies, "grande" pra área) e **>10× maior** que Ribeiro 2021 (321 segmentos, 15 espécies).
  Dataset é **competitivo** em volume, embora menor em diversidade de espécies.

### 0.5.2 Alfenas/MG (validada após inspeção de áudio)

#### Espécies confirmadas

| Nome popular | Nome científico | Também em USP-RP? | | --- | --- | --- | | Tubuna | *Scaptotrigona bipunctata* | sim |
| — | *Scaptotrigona postica* | não | | Borá | *Tetragona clavipes* | sim | | Jataí | *Tetragonisca angustula* | sim | |
Uruçu-amarela | *Melipona rufiventris* (a confirmar) | não |

**Total**: 5 espécies, todas Meliponini. **3 em overlap** com USP-RP (*S. bipunctata*, *T. clavipes*, *T. angustula*),
**2 exclusivas** de Alfenas (*S. postica*, Uruçu-amarela).

#### Observações

- Nome científico exato de **Uruçu-amarela** ainda a confirmar — tipicamente *Melipona rufiventris*, mas pode ser *M.
  mondury* dependendo da fonte/região. Marcar como pendência taxonômica até bater com a Marina.
- *S. bipunctata* e *S. postica* coexistirem no mesmo dataset abre sub-pergunta natural: a assinatura acústica
  intra-gênero (Scaptotrigona) é separável? — análise interessante para a tese.
- Overlap de 3 espécies com USP-RP é **intencional** e habilita estudo de variação geográfica intra-específica (mesma
  espécie, dois biomas: Cerrado vs Mata Atlântica/transição).

#### Hardware

- **Gravador**: mesmo Zoom H4n Handy Recorder usado em USP-RP. ✓ compatível com a literatura (Ferreira 2023).
- **Sem microfone shotgun externo** em Alfenas — todas as capturas foram **gravador direto** (cardioides nativos do
  H4n).
- **Implicação**: o eixo "protocolo de captura" fica mais limpo no dataset combinado — só *A. mellifera* e *T. clavipes*
  (USP-RP) usaram shotgun externo; todo o resto, incluindo as 5 espécies de Alfenas, é gravador direto. Isso simplifica
  o balanceamento mas mantém a confusão potencial nas duas espécies originais com shotgun.

### 0.5.3 Pendências

- Volume/densidade efetivos do dataset de Alfenas — atualizar quando contagem de minutos brutos estiver feita.
- Confirmar nome científico da Uruçu-amarela (*M. rufiventris* vs *M. mondury*).
- Modelo exato do microfone shotgun (USP-RP) ainda a confirmar.
- Sample rate e bit depth efetivos a confirmar inspecionando os arquivos (Bloco A do milestone).
- Rotulagem atual: separação por arquivo/pasta por espécie (a confirmar formato exato).

______________________________________________________________________

## 1. Panorama do problema

### Por que abelhas são acusticamente separáveis?

A frequência do batimento de asa (**wingbeat frequency**) é inversamente proporcional ao tamanho corporal e modulada por
temperatura ambiente e estresse. A sonicação torácica (vibração usada para extrair pólen de flores tipo *Solanum*) tem
assinatura ainda mais espécie-específica que o voo livre. Isso é a base biológica que justifica o pipeline acústico.

- [Towards acoustic monitoring of bees: wingbeat sounds are related to species and individual traits — Royal Society B 2024](https://royalsocietypublishing.org/rstb/article/379/1904/20230111)
- [The sound field generated by tethered stingless bees (*Melipona scutellaris*) — PubMed 2008](https://pubmed.ncbi.nlm.nih.gov/18281331/)
- [Vibratory Communication in Stingless Bees (Meliponini) — Springer chapter 2014](https://link.springer.com/chapter/10.1007/978-3-662-43607-3_18)

### Diversidade & taxonomia (Meliponini)

Brasil tem ~244 espécies descritas de stingless bees (de ~605 globais). Contexto taxonômico ajuda a desenhar o desenho
experimental (qual nível tratar — espécie, gênero, tribo).

- [Stingless bee classification and biology — ZooKeys 2023, review](https://zookeys.pensoft.net/article/104944/)

______________________________________________________________________

## 2. Pipeline canônico

```
Gravação de campo (1–10 cm da abelha)
    └─> Segmentação (separar voo / sonicação / silêncio)
        └─> Extração de features
            ├─ Classical: MFCC (~40 coeficientes), fundamental frequency
            └─ Deep:      Log-Mel spectrogram (imagem 2D)
        └─> Classificador
            ├─ Shallow: SVM (rei do domínio), RF, LR, KNN, ensembles
            └─ Deep:    CNN (EfficientNet, ResNet), PANNs, Transformers
```

**Lições recorrentes da literatura**:

- MFCC + SVM é o baseline forte e custa pouco. Em datasets pequenos (\<1000 segmentos) ele **bate** CNNs sem pré-treino.
- CNN/Transformer só ganha com **pré-treino pesado** (AudioSet via PANNs) + **augmentation forte** (Mixup, time masking,
  random truncation).
- Sample rate típico: 44.1 kHz ou 48 kHz (depende do gravador); janelas de 0.5–2 s.
- Macro-F1 > accuracy quando há class imbalance (sempre tem).

______________________________________________________________________

## 3. Estudos brasileiros (núcleo central — priorizar)

### Martins & Brito 2021 — BuzzTrap (UFU, Uberlândia/MG) — TCC

- URL: <https://repositorio.ufu.br/bitstream/123456789/31978/1/BuzzTrapIdentifica%C3%A7%C3%A3o.pdf>
- TCC em Ciências Biológicas na **UFU**, orientador **Prof. Dr. Vinícius Lourenço Garcia de Brito** (Lab. de Ecologia e
  Comportamento de Abelhas, INBIO/UFU).
- Gravações em **Estação Ecológica do Panga (Cerrado, Uberlândia)** em flores de *Solanum paniculatum* (jurubeba) —
  contexto ecológico idêntico ao tipo de estudo que o Rafael pode fazer.
- Espécies: *Ptiloglossa* sp.1, *Bombus pauloensis*, *Exomalopsis* sp.1, *Oxaea flavescens*, *Xylocopa suspecta*.
- **Pergunta de pesquisa**: voo vs sonicação — qual sinal é melhor para classificação automática?
- Modelo: **Random Forest**.
- **Resultados**:
  - Voo → acurácia global **90,94% ± 5,15%** (98,4% em *X. suspecta*, 84,1% em *B. pauloensis*).
  - Sonicação → **82,22% ± 6,65%** (100% em *O. flavescens*, 69,7% em *B. pauloensis*).
- **Take-away surpreendente**: voo bateu sonicação nesse dataset — contraria intuição comum de que sonicação é mais
  espécie-específica. Vale discutir com a Marina/Rafael por quê (possivelmente diferenças de tamanho corporal bem
  separadas nesse pool).

> **Este é provavelmente o trabalho mais diretamente análogo à tese do Rafael.** Mesma região (Cerrado-MG), mesma
> ferramenta (RF/sklearn), mesmo tipo de pergunta. Ler na íntegra é prioridade alta.

### Ribeiro et al. 2021 — polinizadores de tomate, Viçosa/MG (UFV)

- URL: <https://pmc.ncbi.nlm.nih.gov/articles/PMC8478199/>
- **15 espécies, 8 gêneros**: *Bombus morio*, *B. atratus*, *Melipona bicolor*, *M. quadrifasciata*, *Exomalopsis
  analis*, *Centris* spp., halíctideos.
- Equipamento: SongMeter SM2 a ~10 cm da flor.
- Dataset: 59 arquivos → 321 segmentos (218 sonicação / 103 voo).
- Features: 40 MFCCs. Modelos: SVM, LR, RF, DT, ensemble por voto majoritário.
- **Melhor resultado**: SVM, **73,4% species-level em sonicação**, 60,2% genus-level em voo.
- Limitação central: class imbalance natural (espécies raras pouco amostradas).
- **Contraste com BuzzTrap**: aqui sonicação > voo (oposto do BuzzTrap) — diferença provavelmente devida a número de
  espécies (15 vs 5) e diversidade morfológica do pool. Boa discussão para classe sobre evaluation.

### Otesbelgue et al. 2024 — UFRGS, HMM em *Tetragonisca fiebrigi*

- URL: <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0325732>
- **UFRGS** (PPG em Ecologia, Inst. Biociências) + Mais Abelhas Consultoria Ambiental + Stanford + Baylor + Creighton.
- Detecção de exposição a **clorpirifós** via assinatura acústica da colmeia. 8 colmeias (jan + mar 2024).
- Método: HMM treinado direto sobre áudio raw (48 kHz) via HTK no MATLAB — **não usa MFCC**, treina sequência
  diretamente.
- **F1 > 0,83 para modelos hive-específicos**; 0,61 quando combina colmeias. Cada colmeia tem assinatura acústica única.
- **Take-away pedagógico**: mostra que (i) a tarefa "ID de espécie" é apenas uma; monitoramento de stressor é outra, e
  (ii) modelos de sequência (HMM) podem substituir feature extraction explícita.

### Rodrigues et al. 2022 — UFC, detecção de rainha em *Apis mellifera*

- URL: <https://sol.sbc.org.br/index.php/wcama/article/view/20692> (Anais do WCAMA / SBC)
- Autores: Ícaro de Lima Rodrigues, Davyd B. de Melo, Daniel de Amaral da Silva, Danielo G. Gomes (**UFC**) + Yves
  Rybarczyk (Dalarna).
- Problema: detectar presença/ausência de rainha sem inspeção invasiva.
- Modelos: Hoeffding Tree, Random Forest, **Naive Bayes** (vencedor).
- **97% acurácia com apenas 10 janelas de 1s/dia, 0,93s de tempo de resposta** — abordagem incremental, low-power.
- Útil para discussão de tradeoff custo computacional × precisão.

### Native Bee Scan (ERAD/ERAMIA-NO2) — app de ID de abelhas nativas

- URL: <https://sol.sbc.org.br/index.php/erad-eramia-no2/article/view/26636>
- App brasileiro (Norte do Brasil) para identificação de abelhas nativas com IA. Pode ser visual e/ou acústico — vale
  ler para conhecer iniciativas paralelas e parcerias.

### Detecção de abelhas nativas do Cerrado — Caderno Pedagógico

- URL: <https://ojs.studiespublicacoes.com.br/ojs/index.php/cadped/article/download/19970/11036/51328>
- Trabalho aplicado em espécies de abelhas nativas do Cerrado. Mesmo bioma da pesquisa do Rafael.

______________________________________________________________________

## 3.5 Grupos e comunidades brasileiras

- **Lab. de Ecologia e Comportamento de Abelhas (INBIO/UFU)** — Vinícius Brito. Orientou o BuzzTrap.
  <https://www.inbio.ufu.br/unidades/laboratorio-de-pesquisa/laboratorio-de-ecologia-e-comportamento-de-abelhas>
- **PPG Ecologia / Inst. Biociências UFRGS** — Maria João Ramos Pereira (Otesbelgue et al.). Linha de bioacústica e
  meliponíneos.
- **LABEC — Lab. de Ecologia Comportamental e Bioacústica, UFJF** — referenciado em buscas como grupo brasileiro ativo
  em bioacústica.
- **Lab. de Computação Aplicada (LCA/UFC)** — Danielo Gomes. Linha de ML aplicado a apicultura/meliponicultura.
- **Sociedade Brasileira de Bioacústica (SBBa)** — congresso bianual (CBB). <https://www.sbba.com.br/>
- **WCAMA / SBC** — Workshop de Computação Aplicada à Gestão do Meio Ambiente e Recursos Naturais. Bom venue para o
  Rafael publicar.

### *Heterotrigona itama* — alarme de intrusão (Sudeste Asiático, metodologia transferível)

- URL: <https://www.mdpi.com/2077-0472/15/6/591>
- MFCC + SVM/KNN para classificar sinais de alarme. Boa referência metodológica para tarefas *intra-espécie* (estados
  comportamentais).

______________________________________________________________________

## 4. Metodologia de ponta (não-brasileiros, mas referência metodológica)

### Ferreira et al. 2023 — Chile, polinizadores de mirtilo

- URL: <https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2023.1081050/full> ·
  [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10140520/)
- 16 espécies, 518 indivíduos, **3.595 segmentos** (1.728 sonicação + 1.867 voo). Recorder Zoom H4n Pro a 1–5 cm do
  tórax.
- Comparação direta: Log-Mel-Spectrogram vs MFCC; EfficientNetV2-Small + PANNs vs SVM/RF/LR/DT.
- **Melhor**: EfficientNetV2 + Mixup + RandomTruncation + pré-treino → **macro-F1 58%**. Clássicos travaram em ~35%.
- Take-away: o pulo de qualidade de CNN só aparece com augmentation + pré-treino, **e mesmo assim macro-F1 está longe de
  saturado**.

### Deep learning bee sound ID — ScienceDirect 2023

- URL: <https://www.sciencedirect.com/science/article/abs/pii/S1574954123003035>

### Comparativo de modelos para baixa computação

- URL: <https://pmc.ncbi.nlm.nih.gov/articles/PMC9824169/>
- Relevante se Rafael for rodar inferência em campo (Raspberry Pi, etc.).

### CNN para monitoramento de colmeia (preprint 2025)

- URL: <https://arxiv.org/pdf/2509.17800>

______________________________________________________________________

## 5. Reviews sistemáticas

### Buzzing through Data — MDPI 2024

- URL: <https://www.mdpi.com/2571-5577/7/4/62>
- 22 estudos revisados. **Apenas 5 cobrem stingless bees** apesar de >600 espécies globais. Lacuna explícita de pesquisa
  = oportunidade de tese.

### Automatic synthesis of insects bioacoustics — Springer 2024

- URL: <https://link.springer.com/article/10.1007/s42690-024-01406-2>
- MFCC é a feature mais usada; SVM é o shallow mais comum; CNN depende de augmentation. Confirma o pipeline canônico da
  seção 2.

### Audio classification of insects — arXiv 2025

- URL: <https://arxiv.org/html/2502.13893>
- Cigarras, besouros, cupins, grilos. Não-abelhas, mas overlapping de técnicas e pipelines de pré-processamento.

______________________________________________________________________

## 6. Ferramentas (a confirmar quando começarmos a codar áudio)

- **librosa** — extração de MFCC, mel-spectrogram, onset detection. Standard em Python.
- **torchaudio** — para deep learning em PyTorch (data loaders, transforms GPU-side).
- **scikit-maad** — bioacústica ecológica, índices acústicos.
- **PANNs (Pretrained Audio Neural Networks)** — pré-treino em AudioSet, transfer learning out-of-the-box.
- **Wildlife Acoustics SongMeter** — gravador usado por Ribeiro et al. (referência de hardware de campo).

______________________________________________________________________

## 7. Lacunas / ideias para o trabalho do Rafael

- **Datasets públicos de stingless bees são escassos.** Construir um (mesmo pequeno, bem rotulado) já é contribuição.
- **Class imbalance** é o problema metodológico recorrente — explorar oversampling, focal loss, augmentation por espécie
  rara.
- **Voo livre vs sonicação** geralmente são tratados separadamente; cross-task transfer learning seria inovação
  razoável.
- **Embeddings pré-treinados** (VGGish, PANNs, BirdNET adaptado) ainda foram pouco explorados para meliponíneos.
- **Detecção em ambiente ruidoso** (vento, outros insetos, vozes humanas) — quase ninguém reporta robustez em ruído
  realista.

______________________________________________________________________

## 8. Como esta lista é usada na mentoria

- Cada aula que introduzir um algoritmo deve, idealmente, citar **pelo menos um paper acima** onde aquele algoritmo é
  aplicado a abelhas (preferencialmente brasileiras).
- A seção "✍️ Handwriting Connection" do template do curso pode ganhar uma variante "🐝 Bee Audio Connection" puxando
  dessa lista.
- Quando atualizarmos esse arquivo, manter a estrutura de seções e a ordem de prioridade (espécies brasileiras >
  metodologia de ponta > reviews > ferramentas > lacunas).
