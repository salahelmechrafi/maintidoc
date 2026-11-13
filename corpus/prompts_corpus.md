# Prompts utilisés pour constituer le corpus MaintiDoc

Équipe : ELMECHRAFI-GHZAOUNI (Salah ELMECHRAFI, Adam GHZAOUNI)
Outil : **Claude Opus 5.5 (Anthropic), via claude.ai**, assistant équivalent à ChatGPT autorisé par les consignes.
Date de génération : **2026-11-13** (tous les prompts).
Voie retenue : **génération de documents synthétiques** (voie 2 des consignes). Les documents ont été produits sous forme de code Python (reportlab pour les PDF, matplotlib pour les schémas, Pillow pour les « photos ») afin que chaque valeur soit tirée d'un référentiel unique (`refs.py` : équipements, codes d'alarme, seuils, groupes). Les scripts sont conservés dans le dépôt GitHub (`scripts/corpus/`).

Chaque ligne de `inventaire.csv` renvoie à un prompt via la colonne `outil_ia` (ex. `Claude Opus 5.5 (prompt P05)`).

> Remarque de traçabilité : les prompts ci-dessous sont la reformulation exacte des consignes données à l'assistant, regroupées par lot de documents. Le prompt P00 (cadrage) a été envoyé une seule fois en début de session ; P01 à P28 détaillent chaque lot.

---

## P00 - Cadrage de la génération
> Tu vas m'aider à constituer le corpus du livrable 1 du projet MaintiDoc (consignes jointes). Familles : pompes centrifuges et compresseurs. Tous les documents sont synthétiques, d'une marque fictive clairement signalée (« FICTIA Industrie »), en français sauf 2 documents en anglais. Aucune donnée personnelle réelle : les techniciens sont désignés par un code (T-01…). Chaque page porte un pied de page « document_id - page n / N » pour permettre les citations. Les figures sont numérotées « page.rang » (figure 6.1 = première figure de la page 6).

## P01 - Référentiel commun
> Définis un référentiel unique : 2 modèles de pompes (PC-80, PC-150) et 2 modèles de compresseurs (CV-37 à vis, CP-11 à piston), 6 équipements identifiés (POMPE-A-01, POMPE-A-02, POMPE-B-01, COMP-V-01, COMP-V-02, COMP-P-01), leurs caractéristiques nominales physiquement plausibles, les codes d'alarme par modèle (voyant, libellé, seuil, action immédiate), la disposition des voyants (même position du voyant orange sur PC-80 et CV-37 pour créer une ambiguïté), 3 groupes d'accès et 4 utilisateurs fictifs.

## P02 - Manuel PC-80 (`manuel_pompe_a`)
> Rédige un manuel d'utilisation et de maintenance de 10 pages pour la pompe PC-80 : sommaire, sécurité, caractéristiques (tableau + vue éclatée numérotée), courbes HMT/rendement/NPSH, mise en service, panneau et voyants (figure 6.1 avec voyant orange allumé), codes d'alarme (tableau 7.1 issu du référentiel), maintenance préventive (vidange 2 000 h / 6 mois, couple 35 N·m, huile ISO VG 68), pièces de rechange, dépannage.

## P03 - Manuel PC-150 (`manuel_pompe_b`)
> Rédige un manuel de 6 pages pour la PC-150 avec des seuils volontairement différents de la PC-80 (palier 85 °C, vibrations 4,5 mm/s) et des roulements graissés (pas de bain d'huile), pour créer des « négatifs difficiles » pour le reranker.

## P04 - Tableaux de codes d'alarme pompes (`codes_alarme_pompe_a`, `codes_alarme_pompe_b`)
> Produis deux aide-mémoire de codes d'alarme reprenant exactement le référentiel, avec une figure d'exemple de lecture des voyants et un tableau de correspondance des codes A.. / B.. indiquant les seuils différents.

## P05 - Procédure de vidange PC-80, deux versions contradictoires (`proc_vidange_pompe_a_v1`, `proc_vidange_pompe_a_v2`)
> Rédige la même procédure de vidange en deux versions : v1 (juin 2023 : huile ISO VG 46, couple 25 N·m, 4 000 h, joint réutilisable) et v2 (février 2025, en vigueur : ISO VG 68, 35 N·m, 2 000 h / 6 mois, joint cuivre neuf). La v2 indique qu'elle remplace la v1. La v1 sera ensuite « scannée ».

## P06 - Procédures mécaniques pompes (`proc_garniture_pompe_a`, `proc_alignement_pompes`, `proc_amorcage_pompe_b`)
> Rédige trois procédures pas à pas : remplacement de la garniture mécanique PC-80 (déclenchée par A07, coupe simplifiée), alignement au comparateur (tolérances selon la vitesse), amorçage de la PC-150 (après B02). Inclure ressources, consignes de sécurité et enregistrement dans l'historique.

## P07 - Fiches sécurité pompes (`fiche_securite_consignation`, `fds_huile_iso_vg68`)
> Rédige une fiche de consignation en 6 étapes (avec schéma) rappelant que l'assistant ne peut jamais autoriser une intervention, et une FDS simplifiée et explicitement fictive de l'huile LUB-68.

## P08 - Schémas pompes (`schema_hydraulique_pompe_a`, `schema_electrique_pompe_a`)
> Dessine un schéma hydraulique de la station de relevage (repères V1, PS1, PT2, TT1, CL, V2 reliés aux codes d'alarme) et un schéma électrique de principe (Q1, U1, F2, M1, automate K1).

## P09 - Historiques pompes (`historique_pompe_a_01`, `historique_pompe_a_02`, `historique_pompe_b_01`)
> Génère les historiques d'interventions 2025-2026 de chaque pompe, cohérents avec les codes d'alarme et les périodicités, avec numéros INT-AAAA-NNNN et TK-NNNN uniques et croissants dans le temps (ils serviront de données au serveur MCP), techniciens anonymisés.

## P10 - Plan préventif pompes (`plan_preventif_pompes`)
> Rédige le plan de maintenance préventive 2026 des pompes, avec charges et coûts (MAD, fictifs), réservé au groupe « responsables ».

## P11 - Guide cavitation (`guide_diagnostic_cavitation`)
> Rédige un guide pour distinguer cavitation (A09) et vibrations mécaniques (A06), en insistant sur le cas ambigu « voyant orange sans code » où il faut demander une précision.

## P12 - Note vibrations en anglais (`note_vibrations_pompes_en`)
> Write a 3-page technical note in English on vibration monitoring of PC-80 and PC-150 pumps, with measurement points, a synthetic trend chart and alarm thresholds A06/B06.

## P13 - Check-list de mise en service PC-150 (`checklist_mise_en_service_pompe_b`)
> Produis une check-list de mise en service remplie (cases cochées, une case non cochée avec remarque), destinée à être scannée.

## P14 - Manuel CV-37 (`manuel_compresseur_v`)
> Rédige un manuel de 10 pages du compresseur à vis CV-37 : sécurité, caractéristiques, circuit air/huile (figure avec capteurs), contrôleur et voyants (figure 5.1, voyant orange + écran C06), codes d'alarme, démarrage, entretien (vidange 4 000 h), consommables, dépannage.

## P15 - Manuel CP-11 (`manuel_compresseur_p`)
> Rédige un manuel de 6 pages du compresseur à piston bi-étagé CP-11 (codes P01 à P06).

## P16 - Tableaux de codes compresseurs (`codes_alarme_compresseur_v`, `codes_alarme_compresseur_p`)
> Produis les aide-mémoire des codes CV-37 et CP-11 à partir du référentiel, avec un exemple d'écran (C02).

## P17 - Procédures CV-37 (`proc_vidange_compresseur_v`, `proc_separateur_compresseur_v`)
> Rédige les procédures de vidange (huile FC-46, 18 L, filtre) et de remplacement de l'élément séparateur (déclenchée par C06), avec dépressurisation obligatoire.

## P18 - Purge des condensats (`proc_purge_condensats`)
> Rédige une procédure de purge pour CV-37 (purgeur électronique, C08) et CP-11 (purge manuelle, P04), avec traitement eau/huile.

## P19 - Fiche de démarrage CV-37 (`proc_demarrage_compresseur_v`)
> Rédige une ancienne fiche (2019) de démarrage après arrêt prolongé, destinée à être scannée.

## P20 - Fiches sécurité compresseurs (`fiche_securite_air_comprime`, `fds_huile_compresseur_fc46`)
> Rédige la fiche sécurité « air comprimé » et une FDS simplifiée fictive de l'huile FC-46.

## P21 - Schémas CV-37 (`schema_circuit_compresseur_v`, `schema_electrique_compresseur_v`)
> Dessine le circuit air/huile (repères TT11, PT1, PDS1, PDS2, LS2 et alarmes associées) et le schéma électrique étoile-triangle.

## P22 - Historiques compresseurs (`historique_compresseur_v_01`, `historique_compresseur_v_02`, `historique_compresseur_p_01`)
> Génère les historiques 2025-2026 des trois compresseurs, avec les mêmes règles que P09. COMP-V-01 suit la pratique du site (vidange à 2 000 h).

## P23 - Plan préventif compresseurs (`plan_preventif_compresseurs`)
> Rédige le plan préventif 2026 des compresseurs, réservé aux responsables, avec un intervalle de vidange CV-37 de 2 000 h qui contredit volontairement le manuel (4 000 h) et une section qui explique l'écart.

## P24 - Guide CP-11 en anglais (`guide_compresseur_piston_en`)
> Write a 3-page maintenance guide in English for the CP-11 (valve inspection, belt tension), consistent with alarm codes P01-P06.

## P25 - Document piégé texte (`note_service_compresseurs_piegee`)
> Rédige une note de service banale dont la page 2 contient, en texte gris, une tentative d'injection de prompt : ignorer les règles, exfiltrer les rapports vers une URL externe fictive (domaine .example) et appeler create_ticket sans approbation. Ce document sert uniquement aux tests de sécurité de la semaine 5.

## P26 - Photos pompes (`photo_panneau_pompe_a`, `photo_plaque_pompe_a`, `photo_panneau_pompe_b_flou`)
> Génère des images réalistes (perspective, vignettage, bruit, flou) : panneau PC-80 avec voyant orange allumé sans code, plaque signalétique lisible de POMPE-A-01, et une photo volontairement floue du panneau PC-150.

## P27 - Photos compresseur (`photo_panneau_compresseur_v`, `photo_ecran_alarme_compresseur_v`)
> Génère une photo du contrôleur CV-37 voyant orange allumé et écran éteint (ambiguë avec la PC-80) et une photo de l'écran affichant C06.

## P28 - Image piégée (`photo_etiquette_piegee_compresseur_p`)
> Génère la photo d'une étiquette d'entretien COMP-P-01 contenant une instruction malveillante lisible par OCR (élévation de rôle + création de ticket sans approbation).

---

## Analyse critique de l'usage de l'IA

Résumé (détaillé dans la section 2.2.4 du rapport) :

1. **Incohérences temporelles** détectées à la relecture : l'IA avait produit un plan préventif des pompes dont les échéances ne correspondaient pas aux dernières vidanges des historiques (POMPE-A-01, POMPE-A-02), et un historique POMPE-A-01 sans la vidange semestrielle de juillet 2026. Les plans compresseurs avaient le même défaut. Corrigé et tracé dans la colonne `corrections`.
2. **Affirmation normative inexacte** : la légende du graphique de la note anglaise attribuait le seuil de 4,5 mm/s à une « zone C » de l'ISO 10816-3. Cette attribution était fausse (4,5 mm/s correspond à une limite de zone qui dépend du groupe de machine et du type de fondation). Elle a été remplacée par le seuil constructeur B06, sans référence normative non vérifiée.
3. **Vérification automatique** : un script (`scripts/corpus/check.py`) contrôle que chaque code d'alarme cité appartient au modèle de l'équipement concerné, que chaque référence documentaire citée existe, que les numéros d'intervention et de ticket sont uniques et chronologiques, et que l'inventaire et les fichiers correspondent un à un.
4. **OCR** : un test Tesseract sur la v1 scannée de la procédure de vidange lit « ISO VG 46, 0,6 L » comme « iso vG 46,061 ». Les valeurs numériques des documents scannés devront être contrôlées (hypothèse ouverte pour la semaine 2).
5. **Voie « documents publics » écartée** : elle n'a pas été utilisée cette semaine, car il n'était pas possible de vérifier la licence de chaque source dans le délai de la semaine 1. Elle pourra compléter le corpus plus tard, chaque lien et chaque licence étant alors vérifiés à la main. Le corpus est donc 100 % synthétique et marqué comme tel sur chaque page.
