# MaintiDoc : livrable 1 (cadrage, corpus et architecture)

**Équipe ELMECHRAFI-GHZAOUNI** · Module IA générative multimodale · EMSI 2026

| Membre | Rôle principal |
|---|---|
| Salah ELMECHRAFI | ingestion, recherche multimodale, VLM, fine-tuning du reranker |
| Adam GHZAOUNI | API, contrôle d'accès, serveur MCP, workflow LangGraph, interface |

## Objectif du projet
MaintiDoc est un assistant documentaire multimodal et agentique pour la maintenance de **pompes centrifuges** et de **compresseurs**. Il répond à une question accompagnée d'une photo en citant la page et la figure qui justifient chaque affirmation, et il peut consulter l'historique d'un équipement via un outil MCP. Il prépare aussi des tickets de maintenance, mais leur création exige toujours une approbation humaine. Il ne pilote aucune machine et ne garantit aucun diagnostic.

## Contenu du ZIP
```
L1_MaintiDoc_ELMECHRAFI-GHZAOUNI/
├── L1_MaintiDoc_ELMECHRAFI-GHZAOUNI_Rapport.pdf     rapport (parties 2.1 à 2.6)
├── L1_MaintiDoc_ELMECHRAFI-GHZAOUNI_LienGitHub.txt  URL du dépôt
├── README.md                                        ce fichier
└── L1_MaintiDoc_ELMECHRAFI-GHZAOUNI_Corpus/
    ├── inventaire.csv          44 documents, 20 colonnes, UTF-8
    ├── prompts_corpus.md       prompts P00 à P28 + analyse critique
    ├── documents/famille_1/    20 PDF pompes (dont 2 scannés)
    ├── documents/famille_2/    18 PDF compresseurs (dont 1 scanné)
    └── images/                 6 photographies synthétiques
```
Le corpus est **100 % synthétique** (marque fictive « FICTIA Industrie », mention sur chaque page). Il comprend 2 paires de documents contradictoires, 2 documents piégés (injection de prompt) et 4 cas ambigus, signalés dans la colonne `usage_test`.

## Structure du dépôt GitHub
```
maintidoc/
├── README.md
├── .gitignore                 exclut .env, secrets, poids de modèles, caches
├── docs/
│   ├── diagrammes/            sources Graphviz (.dot) + rendus PDF/PNG
│   └── livrables/             rapport du livrable 1
├── corpus/
│   ├── inventaire.csv
│   ├── prompts_corpus.md
│   ├── documents/famille_1/   documents/famille_2/
│   └── images/
└── scripts/corpus/            génération reproductible du corpus et contrôle de cohérence
```
Pour régénérer et vérifier le corpus : `pip install reportlab matplotlib pillow pymupdf`, puis `python scripts/corpus/build.py corpus && python scripts/corpus/write_inv.py corpus && python scripts/corpus/check.py corpus`.
