# Milestone 01: Kickoff do Projeto de Pesquisa

> **Aula-ponte (milestone)** entre a Aula 03 (Regressão Linear) e a Aula 04 (Regressão Logística). **Sem limite de tempo
> fixo** — dura o que precisar. Ver convenção em [CLAUDE.md](../CLAUDE.md#milestones--aulas-ponte-para-o-projeto-real).

______________________________________________________________________

## Objetivo

Traduzir o que foi aprendido nas Aulas 01–03 em **progresso concreto na tese do Rafael** (identificação acústica de
abelhas — ver [RESEARCH.md](../RESEARCH.md)). Sair da aula com:

1. **Inventário fechado do dataset real** — sabemos exatamente o que existe, em que formato, com que rótulos.
1. **Escopo técnico definido** — sabemos a tarefa principal (qual classificação, qual nível taxonômico, voo vs
   sonicação).
1. **Primeira inspeção de áudio real** — Rafael viu pela primeira vez o som dele em espectrograma + MFCC.
1. **Primeiro classificador minúsculo rodando** — k-NN sobre MFCC médio, mesmo com 2 espécies. Prova de conceito.
1. **Lista de próximos passos** — o que precisa entrar em cada uma das aulas 04–09 para que a tese avance em paralelo.

> **Não é o projeto-tese pronto.** Este milestone é fundamento. A implementação completa da pesquisa do Rafael será em
> outro repositório, depois do curso.

______________________________________________________________________

## Pré-requisitos — o que trazer para a aula

Esse checklist tem 3 blocos. **Bloco A** e **Bloco B** devem chegar à aula **já preenchidos** pelo Rafael (Bloco B
alinhado previamente com a Marina). **Bloco C** é o que decidimos juntos na sessão.

> Use [project-scope.md](project-scope.md) como template para registrar as respostas.

### Bloco A — Dados em mãos (Rafael, antes da aula)

- [ ] Quantos arquivos de áudio já foram gravados (USP-RP + Alfenas)?
- [ ] Onde estão armazenados? Quanto de disco ocupam (GB)?
- [ ] Formato: WAV / FLAC / MP3?
- [ ] Sample rate (44.1 kHz / 48 kHz / outro)?
- [ ] Profundidade de bits (16 / 24)?
- [ ] Mono ou estéreo?
- [ ] Duração média por gravação? Duração total acumulada?
- [ ] Existe metadado: data, hora, local (GPS ou texto), temperatura, condição climática?
- [ ] **Já existe rotulagem por espécie?** Em que formato — nome de arquivo, planilha à parte, anotação manual em
  Audacity / Raven / outro?
- [ ] Traga **pelo menos 1 arquivo representativo por classe gravada** (se for só uma espécie até agora, traga 2–3
  arquivos da mesma).

### Bloco B — Domínio e protocolo de coleta (Rafael, alinhado com Marina antes)

- [ ] Quantas espécies pretende cobrir no escopo final da tese?
- [ ] Quais espécies **já têm áudio gravado** até o momento? (lista)
- [ ] Tipo de gravação: **voo livre**, **sonicação em flor**, **dentro da colmeia**, ou combinação?
- [ ] Equipamento: gravador (marca/modelo) + microfone (modelo, direcional ou omni)?
- [ ] Distância microfone–abelha padronizada? Se sim, qual?
- [ ] Há **replicação biológica** (mesmo indivíduo ou colônia gravado em sessões diferentes)?
- [ ] Há espécies sabidamente difíceis de distinguir morfologicamente neste pool? (caso difícil)
- [ ] Há viés de captura conhecido (espécie X mais fácil de gravar que Y)?
- [ ] Há controle de tamanho corporal (medida do indivíduo gravado)?

### Bloco C — Definições técnicas a fechar na aula (todos juntos)

- [ ] **Tarefa principal**: classificação multi-classe? binária (espécie focal vs outras)? regressão (predizer tamanho
  corporal a partir do som)?
- [ ] **Nível taxonômico do alvo**: espécie / gênero / tribo?
- [ ] **Sinal de entrada**: voo, sonicação, ambos, ou hive-internal?
- [ ] **Hipótese existente da Marina/Rafael**: já há intuição? (ex.: "voo separa melhor que sonicação nesse pool",
  "_Melipona_ se confunde entre si")
- [ ] **Métrica de sucesso primária**: acurácia / macro-F1 / recall em espécies raras?
- [ ] **Baseline desejado**: o que conta como "funcionou"?
  - Referências da literatura: BuzzTrap 90,9% em voo (Cerrado/MG, RF, 5 espécies); Ribeiro 73,4% em sonicação
    (Viçosa/MG, SVM, 15 espécies). Ver
    [RESEARCH.md §3](../RESEARCH.md#3-estudos-brasileiros--n%C3%BAcleo-central--priorizar).
- [ ] **Versionamento de dados**: Git LFS, DVC, ou pasta externa fora do repo?

______________________________________________________________________

## Estrutura da sessão

Sem tempos rígidos. Sugestão de ordem:

1. **Recap rápido** — o que aprendemos nas Aulas 01–03 e como cada peça vai aparecer no projeto real.
1. **Passar o checklist** — Blocos A e B na tela, conferir respostas, anotar lacunas no
   [project-scope.md](project-scope.md).
1. **Primeira inspeção** — abrir um áudio real do Rafael no notebook: waveform, espectrograma, mel-spectrogram, MFCC.
1. **Feature engineering inicial** — extrair MFCC médio (vetor 40-d) por arquivo. Construir um DataFrame minúsculo com
   `arquivo → species → mfcc_0 ... mfcc_39`.
1. **Primeiro classificador** — `train_test_split` estratificado + `KNeighborsClassifier` + acurácia + confusion matrix.
   **Com humildade**: dataset é pequeno, isso é prova-de-conceito, não resultado de tese.
1. **Bloco C** — fechar as decisões técnicas em [project-scope.md](project-scope.md).
1. **Próximos passos** — mapear o que cada aula 04–09 precisa entregar para que a tese avance.

______________________________________________________________________

## Entregáveis da aula

- [ ] [project-scope.md](project-scope.md) preenchido (Blocos A, B, C).
- [ ] `class-03b-audio-foundation.ipynb` — notebook executado top-to-bottom (gerado pelo Lucca conforme os dados que o
  Rafael trouxer).
- [ ] Lista de "o que cada aula seguinte precisa endereçar para o projeto" — registrada no
  [project-scope.md](project-scope.md).

______________________________________________________________________

## Ferramentas novas que entram aqui

- [`librosa`](https://librosa.org/) — biblioteca de áudio em Python. Carrega WAV, calcula espectrogramas, MFCCs.
  Equivalente conceitual ao `tuneR`/`seewave` do R.
- [`soundfile`](https://python-soundfile.readthedocs.io/) — leitura/escrita de WAV/FLAC. Backend do librosa.
- `matplotlib.specgram` — espectrograma rápido pra inspeção visual.

Essas ferramentas serão instaladas no `pyproject.toml` antes da aula.

______________________________________________________________________

## Notas para o professor

Ver [teacher-notes.md](teacher-notes.md).
