# -*- coding: utf-8 -*-
"""Famille 1 : pompes centrifuges (PC-80 : POMPE-A-01/02 ; PC-150 : POMPE-B-01)."""
import figures as FG
from refs import CODES, MODELES, G_P, G_R, G_ALL

PB = ("pb",)


def table_codes(model, cap):
    rows = [[c, v, l, s, a] for c, (v, l, s, a) in CODES[model].items()]
    return ("table", cap, ["Code", "Voyant", "Libellé", "Condition", "Action immédiate"], rows,
            [36, 52, 100, 110, 185])


def D(**k):
    k.setdefault("folder", "famille_1"); k.setdefault("famille", "pompes"); k.setdefault("lang", "fr")
    k.setdefault("format", "pdf_texte"); k.setdefault("usage", "normal"); k.setdefault("gen_ia", "oui")
    k.setdefault("corrections", "aucune"); k.setdefault("remarques", "")
    return k


def docs():
    m = MODELES["PC-80"]; mb = MODELES["PC-150"]
    L = []

    # ------------------------------------------------------------------ 1 manuel PC-80 (10 p)
    L.append(D(id="manuel_pompe_a", titre="Manuel d'utilisation et de maintenance - pompe centrifuge PC-80",
               equip="POMPE-A-01 ; POMPE-A-02", type="manuel", version="v3.1 (2025-03)", groups=G_P, prompt="P02",
               verifie_par="Salah", ref="MAN-PC80-FR v3.1", ref_court="manuel_pompe_a v3.1",
               remarques="voyant orange décrit p.6 (fig 6.1) ; codes p.7 ; référence principale pour POMPE-A",
               blocks=[
        ("h1", "Manuel d'utilisation et de maintenance<br/>Pompe centrifuge monocellulaire FICTIA PC-80"),
        ("p", "Édition v3.1 - mars 2025. Ce manuel s'applique aux pompes PC-80 installées sur le site de démonstration "
              "sous les repères <b>POMPE-A-01</b> (station de relevage, ligne 1) et <b>POMPE-A-02</b> (ligne 2). Il remplace l'édition v2.4 de 2022."),
        ("h2", "Sommaire"),
        ("table", None, ["Chapitre", "Contenu", "Page"], [["1", "Consignes de sécurité", "2"], ["2", "Description et caractéristiques", "3"],
            ["3", "Courbes de fonctionnement", "4"], ["4", "Installation et mise en service", "5"], ["5", "Panneau de commande et voyants", "6"],
            ["6", "Codes d'alarme", "7"], ["7", "Maintenance préventive", "8"], ["8", "Pièces de rechange et lubrifiants", "9"],
            ["9", "Dépannage et contacts", "10"]], [60, 330, 60]),
        ("p", "Les numéros de figure suivent le numéro de page (ex. figure 6.1 = première figure de la page 6), ce qui permet de citer "
              "une figure sans ambiguïté."),
        ("warn", "Ce manuel ne remplace pas la formation du personnel ni les procédures de consignation du site (fiche FS-CONS-01)."),
        PB,
        ("h1", "1. Consignes de sécurité"),
        ("p", "Toute intervention sur la pompe est réalisée par un technicien habilité, pompe à l'arrêt et <b>consignée</b> électriquement "
              "(sectionneur Q1 ouvert et cadenassé) et hydrauliquement (vannes V1 et V2 fermées, corps de pompe purgé)."),
        ("ul", ["Ne jamais faire fonctionner la pompe à sec : la garniture mécanique est détruite en quelques secondes.",
                "Ne jamais fermer complètement la vanne de refoulement V2 plus de 2 minutes en marche (échauffement du liquide).",
                "Porter gants, lunettes et chaussures de sécurité ; le corps de pompe peut dépasser 60 °C.",
                "Vérifier l'absence de pression avant de desserrer un bouchon ou une bride.",
                "Le capot d'accouplement doit être en place avant toute remise sous tension."]),
        ("p", "Les pictogrammes apposés sur la pompe (danger électrique, surface chaude, pièces tournantes) doivent rester lisibles. "
              "Toute plaque endommagée est remplacée."),
        PB,
        ("h1", "2. Description et caractéristiques"),
        ("p", "La PC-80 est une pompe centrifuge horizontale à aspiration axiale, roue fermée en fonte, palier à bain d'huile et "
              "garniture mécanique simple. Elle est accouplée à un moteur asynchrone de 11 kW piloté par variateur."),
        ("table", "Tableau 3.1 - Caractéristiques nominales PC-80",
         ["Grandeur", "Valeur"], [["Débit nominal", m["debit"]], ["Hauteur manométrique (HMT)", m["hmt"]], ["Puissance moteur", m["puissance"]],
                                  ["Vitesse", m["vitesse"]], ["Pression maximale de refoulement", m["pmax"]],
                                  ["Lubrification palier", "bain d'huile ISO VG 68, 0,6 L"], ["Température max. du liquide", "80 °C"],
                                  ["Masse (pompe + moteur)", "142 kg"]], [220, 230]),
        ("fig", FG.vue_eclatee_pompe("vue_eclatee_pc80"), "Figure 3.1 - Vue éclatée simplifiée de la PC-80 et repères des sous-ensembles", 15),
        PB,
        ("h1", "3. Courbes de fonctionnement"),
        ("p", "La pompe doit fonctionner entre 50 % et 110 % du débit nominal. En dessous, la recirculation interne provoque vibrations "
              "et échauffement ; au-delà, le NPSH requis augmente et le risque de cavitation (alarme A09) devient important."),
        ("fig", FG.courbe_pompe("PC-80", 80, 32, "courbe_pc80"), "Figure 4.1 - Courbes HMT, rendement et NPSH requis de la PC-80", 15),
        ("p", "Règle pratique : le NPSH disponible de l'installation doit rester supérieur d'au moins 0,5 m au NPSH requis lu sur la figure 4.1."),
        PB,
        ("h1", "4. Installation et mise en service"),
        ("ol", ["Contrôler l'alignement pompe-moteur (procédure PROC-ALIGN-01) : écart radial ≤ 0,05 mm.",
                "Remplir le palier d'huile ISO VG 68 jusqu'au milieu du voyant de niveau (0,6 L).",
                "Ouvrir complètement la vanne d'aspiration V1 et remplir le corps de pompe ; purger l'air par le bouchon supérieur.",
                "Entrouvrir la vanne de refoulement V2 (environ 1/4 de tour).",
                "Vérifier le sens de rotation par une impulsion brève (flèche sur le corps de pompe).",
                "Démarrer, puis ouvrir progressivement V2 jusqu'au point de fonctionnement.",
                "Pendant la première heure, relever température palier, pression et vibrations toutes les 15 minutes."]),
        ("p", "Valeurs attendues après 1 heure : température palier entre 45 et 70 °C, vibrations inférieures à 2,8 mm/s eff., "
              "aucune fuite visible à la garniture."),
        PB,
        ("h1", "5. Panneau de commande et voyants"),
        ("p", "Le panneau local comporte quatre voyants H1 à H4, un sélecteur marche/arrêt et un bouton d'arrêt d'urgence (AU)."),
        ("fig", FG.panneau("PC-80", "panneau_pc80", actif="orange"), "Figure 6.1 - Panneau de commande PC-80 (voyant orange H2 allumé)", 14),
        ("table", "Tableau 6.1 - Signification des voyants PC-80",
         ["Voyant", "Repère", "Signification"], [["Vert", "H1", "Pompe en marche, aucun défaut"],
          ["Orange fixe", "H2", "Alerte : la pompe continue de tourner. Lire le code (A03, A04, A06, A07 ou A09) sur la supervision"],
          ["Orange clignotant", "H2", "Perte de communication capteur (A10)"],
          ["Rouge", "H3", "Défaut : arrêt automatique (A01, A02, A05, A08)"], ["Bleu", "H4", "Mode manuel local sélectionné"]], [80, 50, 320]),
        ("p", "<b>Important :</b> un voyant orange seul ne suffit pas à identifier la cause. Le code affiché par la supervision ou "
              "le terminal portable doit être relevé avant toute action."),
        PB,
        ("h1", "6. Codes d'alarme"),
        table_codes("PC-80", "Tableau 7.1 - Codes d'alarme de la PC-80"),
        ("p", "Une alarme orange qui se répète plus de trois fois en 24 heures doit faire l'objet d'un ticket de maintenance."),
        PB,
        ("h1", "7. Maintenance préventive"),
        ("table", "Tableau 8.1 - Opérations périodiques PC-80",
         ["Périodicité", "Opération", "Référence"], [["Hebdomadaire", "Contrôle visuel fuite garniture, bruit, niveau d'huile palier", "-"],
          ["Mensuelle", "Relevé vibrations palier (point P1 radial)", "note VIB-PC-EN"],
          ["2 000 h ou 6 mois", "Vidange huile palier (ISO VG 68, 0,6 L)", "PROC-VID-PC80 v2"],
          ["Annuelle", "Contrôle alignement, serrage boulons de socle", "PROC-ALIGN-01"],
          ["8 000 h ou sur alarme A07", "Remplacement garniture mécanique", "PROC-GAR-PC80"]], [110, 240, 100]),
        ("p", "Le couple de serrage du bouchon de vidange est de <b>35 N·m</b> (joint cuivre neuf à chaque vidange)."),
        PB,
        ("h1", "8. Pièces de rechange et lubrifiants"),
        ("table", "Tableau 9.1 - Pièces de rechange recommandées",
         ["Référence", "Désignation", "Qté conseillée en stock"], [["PR-80-101", "Garniture mécanique Ø 32 mm carbure/carbone", "2"],
          ["PR-80-102", "Joint torique corps de pompe", "4"], ["PR-80-103", "Roulement palier 6308", "2"],
          ["PR-80-104", "Joint cuivre bouchon de vidange", "10"], ["LUB-68", "Huile minérale ISO VG 68 (bidon 5 L)", "1"]], [90, 260, 100]),
        ("p", "L'utilisation d'une huile de grade différent (par exemple ISO VG 46) n'est pas autorisée sur la PC-80 à partir de cette édition."),
        PB,
        ("h1", "9. Dépannage et contacts"),
        ("table", "Tableau 10.1 - Symptômes fréquents",
         ["Symptôme", "Cause probable", "Vérification"], [["Débit insuffisant", "Vanne V1 partiellement fermée, crépine encrassée", "Pression aspiration"],
          ["Bruit de gravier", "Cavitation", "Code A09, guide GD-CAV-01"], ["Palier chaud", "Niveau d'huile bas, huile dégradée, désalignement", "Code A04"],
          ["Fuite à l'arbre", "Garniture usée", "Code A07"]], [120, 200, 130]),
        ("p", "Contact support (fictif) : support-pompes@fictia.example - les tickets sont créés via l'outil de maintenance du site, "
              "après validation par un responsable."),
    ]))

    # ------------------------------------------------------------------ 2 manuel PC-150 (6 p)
    L.append(D(id="manuel_pompe_b", titre="Manuel d'utilisation - pompe centrifuge PC-150",
               equip="POMPE-B-01", type="manuel", version="v1.4 (2024-09)", groups=G_P, prompt="P03", verifie_par="Adam",
               ref="MAN-PC150-FR v1.4", ref_court="manuel_pompe_b v1.4",
               remarques="voyant orange B04 = palier > 85 °C (seuil différent de la PC-80) : négatif difficile",
               blocks=[
        ("h1", "Manuel d'utilisation<br/>Pompe centrifuge FICTIA PC-150"),
        ("p", "Édition v1.4 - septembre 2024. Applicable à la pompe <b>POMPE-B-01</b> du circuit d'eau de refroidissement."),
        ("table", "Tableau 1.1 - Caractéristiques nominales PC-150", ["Grandeur", "Valeur"],
         [["Débit nominal", mb["debit"]], ["HMT", mb["hmt"]], ["Puissance moteur", mb["puissance"]], ["Vitesse", mb["vitesse"]],
          ["Pression maximale", mb["pmax"]], ["Lubrification", "roulements graissés à vie (graisse lithium NLGI 2)"]], [220, 230]),
        ("warn", "Contrairement à la PC-80, la PC-150 ne comporte pas de bain d'huile : ne jamais y verser d'huile."),
        PB,
        ("h1", "2. Courbes de fonctionnement"),
        ("fig", FG.courbe_pompe("PC-150", 150, 45, "courbe_pc150"), "Figure 2.1 - Courbes caractéristiques de la PC-150", 15),
        ("p", "Plage d'utilisation recommandée : 60 à 120 % du débit nominal."),
        PB,
        ("h1", "3. Panneau de commande"),
        ("fig", FG.panneau("PC-150", "panneau_pc150", actif="orange"), "Figure 3.1 - Panneau de la PC-150 (trois voyants, pas de voyant bleu)", 14),
        ("p", "Le voyant orange H2 signale une alerte (B03, B04, B06, B07). Le voyant rouge H3 signale un arrêt automatique."),
        PB,
        ("h1", "4. Codes d'alarme"),
        table_codes("PC-150", "Tableau 4.1 - Codes d'alarme de la PC-150"),
        PB,
        ("h1", "5. Maintenance"),
        ("table", "Tableau 5.1 - Opérations périodiques", ["Périodicité", "Opération"],
         [["Mensuelle", "Relevé vibrations (seuil d'alerte 4,5 mm/s)"], ["3 000 h", "Regraissage roulements : 15 g par roulement"],
          ["Annuelle", "Contrôle alignement et accouplement"], ["Sur alarme B07", "Inspection et nettoyage de la roue"]], [120, 330]),
        ("p", "La PC-150 est amorcée selon la procédure PROC-AMO-PC150 après chaque vidange du circuit."),
        PB,
        ("h1", "6. Dépannage"),
        ("table", "Tableau 6.1 - Symptômes", ["Symptôme", "Cause probable", "Action"],
         [["Pas de débit au démarrage", "Pompe désamorcée", "Procédure d'amorçage"], ["Palier chaud (B04)", "Excès ou manque de graisse", "Contrôler quantité de graisse"],
          ["Vibrations (B06)", "Désalignement, roue encrassée", "Alignement, nettoyage"]], [130, 170, 150]),
    ]))

    # ------------------------------------------------------------------ 3 & 4 tableaux de codes
    L.append(D(id="codes_alarme_pompe_a", titre="Tableau des codes d'alarme - PC-80", equip="POMPE-A-01 ; POMPE-A-02",
               type="codes_alarme", version="v3.1 (2025-03)", groups=G_P, prompt="P04", verifie_par="Salah",
               ref="TAB-ALM-PC80 v3.1", ref_court="codes_alarme_pompe_a v3.1", remarques="aide-mémoire plastifié affiché près du panneau",
               blocks=[("h1", "Aide-mémoire des codes d'alarme - pompes PC-80 (POMPE-A-01 / POMPE-A-02)"),
                       ("p", "Ce tableau reprend le chapitre 6 du manuel MAN-PC80-FR v3.1. En cas de divergence, le manuel fait foi."),
                       table_codes("PC-80", "Tableau 1.1 - Codes d'alarme PC-80"), PB,
                       ("h1", "Lecture des voyants"),
                       ("fig", FG.panneau("PC-80", "panneau_pc80_rouge", actif="rouge"), "Figure 2.1 - Exemple : voyant rouge H3 allumé (arrêt automatique)", 13),
                       ("ul", ["Orange fixe : alerte, la pompe tourne encore.", "Orange clignotant : perte de communication capteur (A10).",
                               "Rouge : arrêt automatique, ne pas réarmer sans avoir identifié la cause.",
                               "Plusieurs voyants allumés : traiter d'abord le défaut rouge."])]))
    L.append(D(id="codes_alarme_pompe_b", titre="Tableau des codes d'alarme - PC-150", equip="POMPE-B-01",
               type="codes_alarme", version="v1.4 (2024-09)", groups=G_P, prompt="P04", verifie_par="Adam",
               ref="TAB-ALM-PC150 v1.4", ref_court="codes_alarme_pompe_b v1.4",
               remarques="codes B.. proches des codes A.. de la PC-80 mais seuils différents ; cite volontairement les codes A.. (tableau 2.1 de correspondance)",
               blocks=[("h1", "Aide-mémoire des codes d'alarme - pompe PC-150 (POMPE-B-01)"),
                       table_codes("PC-150", "Tableau 1.1 - Codes d'alarme PC-150"),
                       ("p", "Attention : les seuils de la PC-150 diffèrent de ceux de la PC-80 (palier : 85 °C au lieu de 80 °C ; vibrations : 4,5 mm/s au lieu de 7,1 mm/s)."),
                       PB, ("h1", "Correspondance avec les codes PC-80"),
                       ("table", "Tableau 2.1 - Codes équivalents (à titre indicatif)", ["PC-150", "PC-80", "Remarque"],
                        [["B01", "A01", "identique"], ["B02", "A02", "seuil 0,2 bar au lieu de 0,3 bar"], ["B04", "A04", "85 °C au lieu de 80 °C"],
                         ["B06", "A06", "4,5 mm/s au lieu de 7,1 mm/s"], ["B07", "-", "pas d'équivalent"], ["-", "A07", "pas de capteur de fuite sur PC-150"]], [80, 80, 290])]))

    # ------------------------------------------------------------------ 5 & 6 procédure de vidange v1 (scannée) / v2 : CONTRADICTOIRES
    def vidange(v):
        old = v == 1
        return [
            ("h1", f"Procédure de vidange de l'huile palier - pompe PC-80 (version {v})"),
            ("p", "Réf. PROC-VID-PC80 v1 - juin 2023" if old else "Réf. PROC-VID-PC80 v2 - février 2025 (annule et remplace la v1 de juin 2023)"),
            ("table", "Tableau 1.1 - Données de la procédure", ["Élément", "Valeur"],
             [["Équipements", "POMPE-A-01, POMPE-A-02"], ["Durée", "30 min"], ["Huile", "ISO VG 46, 0,6 L" if old else "ISO VG 68, 0,6 L"],
              ["Couple bouchon de vidange", "25 N·m" if old else "35 N·m"], ["Joint", "réutilisable si intact" if old else "joint cuivre neuf obligatoire (PR-80-104)"],
              ["Périodicité", "4 000 h" if old else "2 000 h ou 6 mois"]], [200, 250]),
            ("h2", "Préparation"),
            ("ol", ["Arrêter la pompe et consigner selon FS-CONS-01.", "Laisser refroidir le palier sous 40 °C.",
                    "Préparer un bac de récupération de 2 L et des chiffons."]),
            PB,
            ("h1", "Déroulement"),
            ("ol", ["Dévisser le bouchon de remplissage (repère 4, figure 3.1 du manuel).",
                    "Dévisser le bouchon de vidange (repère 7) et laisser s'écouler l'huile 10 minutes.",
                    "Contrôler l'aspect de l'huile : particules métalliques ou aspect laiteux = ouvrir un ticket.",
                    "Remonter le bouchon de vidange au couple de " + ("25 N·m." if old else "35 N·m avec un joint cuivre neuf."),
                    "Remplir avec " + ("de l'huile ISO VG 46" if old else "de l'huile ISO VG 68") + " jusqu'au milieu du voyant de niveau.",
                    "Déconsigner et redémarrer ; vérifier l'absence de fuite après 15 minutes."]),
            ("fig", FG.vue_eclatee_pompe("vue_eclatee_pc80_proc"), "Figure 2.1 - Repères 4 (palier) et 7 (bouchon de vidange)", 12),
            PB,
            ("h1", "Enregistrement"),
            ("p", "Noter dans l'historique de l'équipement : date, heures de fonctionnement, quantité d'huile, aspect de l'huile, technicien (code)."),
            ("table", "Tableau 3.1 - Fiche de relevé", ["Date", "Équipement", "Heures", "Huile (L)", "Aspect", "Technicien"],
             [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]], [60, 85, 60, 60, 110, 75]),
            ("p", "Huile usagée : bidon rouge « huiles usagées » du local déchets." + ("" if old else " Ne jamais mélanger avec les condensats de compresseur.")),
        ]
    L.append(D(id="proc_vidange_pompe_a_v1", titre="Procédure de vidange huile palier PC-80 (v1, 2023)", equip="POMPE-A-01 ; POMPE-A-02",
               type="procedure", version="v1 (2023-06)", groups=G_P, prompt="P05", verifie_par="Adam", format="pdf_scanne", scan=True,
               usage="contradictoire", ref="PROC-VID-PC80 v1", ref_court="proc_vidange_pompe_a_v1",
               remarques="contredit proc_vidange_pompe_a_v2 et manuel_pompe_a (couple 25 vs 35 N·m ; huile VG 46 vs VG 68) ; version obsolète scannée",
               blocks=vidange(1)))
    L.append(D(id="proc_vidange_pompe_a_v2", titre="Procédure de vidange huile palier PC-80 (v2, 2025)", equip="POMPE-A-01 ; POMPE-A-02",
               type="procedure", version="v2 (2025-02)", groups=G_P, prompt="P05", verifie_par="Salah", usage="contradictoire",
               ref="PROC-VID-PC80 v2", ref_court="proc_vidange_pompe_a_v2",
               remarques="version en vigueur ; contredit la v1 (couple de serrage, grade d'huile, périodicité)", blocks=vidange(2)))

    # ------------------------------------------------------------------ 7 garniture
    L.append(D(id="proc_garniture_pompe_a", titre="Procédure de remplacement de la garniture mécanique PC-80", equip="POMPE-A-01 ; POMPE-A-02",
               type="procedure", version="v2 (2024-11)", groups=G_P, prompt="P06", verifie_par="Salah",
               ref="PROC-GAR-PC80 v2", ref_court="proc_garniture_pompe_a v2", remarques="déclenchée par l'alarme A07",
               blocks=[
        ("h1", "Remplacement de la garniture mécanique - PC-80"),
        ("p", "Réf. PROC-GAR-PC80 v2 - novembre 2024. Déclencheur : alarme <b>A07</b> (fuite garniture) ou 8 000 heures de fonctionnement."),
        ("table", "Tableau 1.1 - Ressources", ["Élément", "Détail"], [["Durée", "2 h 30 (2 techniciens)"], ["Pièces", "PR-80-101 garniture, PR-80-102 joint torique"],
            ["Outillage", "clés plates 17/19, extracteur, clé dynamométrique, pâte de montage silicone"], ["Habilitation", "mécanique + consignation"]], [120, 330]),
        ("warn", "Consigner électriquement ET hydrauliquement. Purger le corps de pompe : le liquide peut être chaud."),
        PB,
        ("h1", "Dépose"),
        ("ol", ["Déposer le capot d'accouplement et désaccoupler (repère 5).", "Déposer les 8 vis du corps de pompe (couple de remontage 45 N·m).",
                "Extraire l'ensemble palier + roue en arrière (conception « back pull-out »), sans déposer la volute de la tuyauterie.",
                "Débloquer l'écrou de roue (filet à gauche) et extraire la roue.", "Extraire la partie tournante puis le grain fixe de la garniture."]),
        ("fig", FG.garniture("garniture_pc80"), "Figure 2.1 - Coupe simplifiée de la garniture mécanique", 14),
        PB,
        ("h1", "Repose"),
        ("ol", ["Nettoyer le logement ; aucune rayure n'est tolérée sur l'arbre au niveau du joint torique.",
                "Monter le grain fixe à la main avec de la pâte silicone ; ne jamais toucher les faces de friction.",
                "Monter la partie tournante, régler la cote de compression du ressort à 7,5 mm.",
                "Remonter la roue (écrou au couple de 60 N·m), puis l'ensemble palier dans la volute avec un joint torique neuf.",
                "Réaccoupler et contrôler l'alignement (PROC-ALIGN-01)."]),
        PB,
        ("h1", "Essais"),
        ("p", "Remplir et purger la pompe, déconsigner, démarrer vanne V2 entrouverte. Une légère humidité est tolérée pendant les 30 premières minutes (rodage). "
              "Au-delà, un goutte-à-goutte supérieur à 1 goutte par minute impose un nouveau démontage."),
        ("p", "Acquitter l'alarme A07 sur la supervision et renseigner l'historique (pièces utilisées, heures)."),
    ]))

    # ------------------------------------------------------------------ 8 alignement
    L.append(D(id="proc_alignement_pompes", titre="Procédure d'alignement pompe-moteur (PC-80 et PC-150)", equip="POMPE-A-01 ; POMPE-A-02 ; POMPE-B-01",
               type="procedure", version="v1.2 (2024-05)", groups=G_P, prompt="P06", verifie_par="Adam",
               ref="PROC-ALIGN-01 v1.2", ref_court="proc_alignement_pompes v1.2",
               blocks=[
        ("h1", "Alignement d'un groupe pompe-moteur au comparateur"),
        ("p", "Réf. PROC-ALIGN-01 v1.2. Applicable aux PC-80 et PC-150. Un désalignement est l'une des premières causes d'alarme de vibrations (A06 / B06) et d'échauffement palier (A04 / B04)."),
        ("fig", FG.alignement("alignement"), "Figure 1.1 - Montage du comparateur sur l'accouplement", 14),
        PB,
        ("h1", "Méthode"),
        ("ol", ["Consigner le groupe.", "Contrôler le « pied boiteux » : aucune cale ne doit bouger de plus de 0,05 mm au desserrage.",
                "Fixer le comparateur sur le moyeu côté pompe, palpeur sur le moyeu moteur.",
                "Relever les valeurs à 0°, 90°, 180°, 270° en radial puis en axial.", "Corriger d'abord le plan vertical (cales), puis le plan horizontal.",
                "Serrer les boulons du moteur en croix et refaire un relevé final."]),
        ("table", "Tableau 2.1 - Tolérances", ["Vitesse", "Écart radial max.", "Écart angulaire max."],
         [["1 450 tr/min (PC-150)", "0,08 mm", "0,07 mm / 100 mm"], ["2 900 tr/min (PC-80)", "0,05 mm", "0,05 mm / 100 mm"]], [150, 150, 150]),
        PB,
        ("h1", "Enregistrement"),
        ("p", "Reporter les relevés avant/après dans l'historique de l'équipement. Si l'écart initial dépassait le double de la tolérance, "
              "rechercher une cause (tuyauterie qui contraint, socle fissuré) et ouvrir un ticket."),
    ]))

    # ------------------------------------------------------------------ 9 amorçage
    L.append(D(id="proc_amorcage_pompe_b", titre="Procédure d'amorçage - pompe PC-150", equip="POMPE-B-01", type="procedure",
               version="v1 (2024-09)", groups=G_P, prompt="P06", verifie_par="Adam", ref="PROC-AMO-PC150 v1", ref_court="proc_amorcage_pompe_b v1",
               blocks=[
        ("h1", "Amorçage de la pompe PC-150 (POMPE-B-01)"),
        ("p", "La PC-150 n'est pas auto-amorçante. Elle doit être amorcée après chaque vidange du circuit ou après une alarme B02 (marche à sec)."),
        ("ol", ["Vérifier que la vanne d'aspiration est ouverte et la vanne de refoulement fermée.", "Ouvrir le purgeur d'air situé sur le haut de la volute.",
                "Remplir par l'entonnoir d'amorçage jusqu'à écoulement d'eau sans bulles au purgeur.", "Fermer le purgeur, démarrer, puis ouvrir lentement la vanne de refoulement.",
                "Si la pression ne s'établit pas en 20 secondes, arrêter et recommencer (maximum 3 essais)."]),
        PB,
        ("h1", "Défauts fréquents"),
        ("table", "Tableau 2.1 - Défauts à l'amorçage", ["Constat", "Cause", "Action"],
         [["Bulles persistantes", "Prise d'air à l'aspiration", "Contrôler joints de bride"], ["Alarme B02 répétée", "Clapet de pied non étanche", "Ouvrir un ticket"],
          ["Pression instable", "Niveau bâche trop bas", "Rétablir le niveau"]], [130, 160, 160]),
    ]))

    # ------------------------------------------------------------------ 10 consignation
    L.append(D(id="fiche_securite_consignation", titre="Fiche sécurité - consignation des équipements tournants", equip="POMPE-A-01 ; POMPE-A-02 ; POMPE-B-01",
               type="fiche_securite", version="v4 (2025-01)", groups=G_ALL, prompt="P07", verifie_par="Salah",
               ref="FS-CONS-01 v4", ref_court="fiche_securite_consignation v4",
               remarques="fiche transversale, aussi applicable aux compresseurs (cf. FS-AIR-01)",
               blocks=[
        ("h1", "Fiche sécurité FS-CONS-01 - Consignation"),
        ("p", "Toute intervention mécanique sur une pompe ou un compresseur exige une consignation complète. Seul un agent habilité peut consigner."),
        ("fig", FG.consignation("consignation"), "Figure 1.1 - Les six étapes de la consignation", 16),
        ("ol", ["<b>Préparer</b> : identifier toutes les énergies (électrique, hydraulique, pneumatique, thermique).",
                "<b>Séparer</b> : ouvrir le sectionneur Q1, fermer les vannes d'isolement.", "<b>Condamner</b> : cadenas personnel sur chaque organe.",
                "<b>Identifier</b> : étiquette « consigné » datée et signée (code agent).", "<b>Vérifier</b> l'absence de tension et de pression.",
                "<b>Purger</b> les énergies résiduelles (pression, fluide chaud, air comprimé)."]),
        PB,
        ("h1", "Règles complémentaires"),
        ("ul", ["Un cadenas par intervenant ; la déconsignation est faite par celui qui a consigné.",
                "Une consignation interrompue (changement d'équipe) est reprise par une nouvelle vérification d'absence d'énergie.",
                "L'assistant documentaire ne peut en aucun cas autoriser une intervention : la consignation reste une décision humaine."]),
        ("warn", "Le voyant éteint d'un panneau ne prouve pas l'absence de tension."),
    ]))

    # ------------------------------------------------------------------ 11 FDS huile
    L.append(D(id="fds_huile_iso_vg68", titre="Fiche de données de sécurité simplifiée - huile minérale ISO VG 68 (LUB-68)", equip="POMPE-A-01 ; POMPE-A-02",
               type="fiche_securite", version="v2 (2024-06)", groups=G_P, prompt="P07", verifie_par="Adam", ref="FDS-LUB-68 v2", ref_court="fds_huile_iso_vg68 v2",
               remarques="FDS synthétique simplifiée, ne remplace pas une FDS réglementaire",
               blocks=[
        ("h1", "FDS simplifiée - Huile LUB-68 (ISO VG 68)"),
        ("p", "Document synthétique, structure inspirée des 16 rubriques d'une FDS. Il ne remplace pas la FDS du fournisseur réel."),
        ("table", "Tableau 1.1 - Identification et propriétés", ["Rubrique", "Contenu"],
         [["Produit", "Huile minérale de lubrification ISO VG 68 (fictive)"], ["Usage", "Paliers de pompes PC-80"], ["Viscosité à 40 °C", "68 mm²/s"],
          ["Point éclair", "> 200 °C"], ["Classement", "non classée dangereuse (données fictives)"]], [150, 300]),
        PB,
        ("h1", "Premiers secours et manipulation"),
        ("ul", ["Contact peau : laver à l'eau et au savon.", "Projection oculaire : rincer 15 minutes à l'eau.", "Ingestion : ne pas faire vomir, consulter un médecin.",
                "Port de gants nitrile recommandé."]),
        PB,
        ("h1", "Stockage et élimination"),
        ("p", "Stocker à l'abri du gel, sur rétention. Les huiles usagées sont collectées dans le bidon rouge et éliminées par la filière agréée du site."),
    ]))

    # ------------------------------------------------------------------ 12 & 13 schémas
    L.append(D(id="schema_hydraulique_pompe_a", titre="Schéma hydraulique de la station de relevage (POMPE-A-01)", equip="POMPE-A-01",
               type="schema", version="v2 (2025-01)", groups=G_P, prompt="P08", verifie_par="Salah", ref="SCH-HYD-PA01 v2", ref_court="schema_hydraulique_pompe_a v2",
               remarques="localise les capteurs associés aux codes A02, A03, A04, A09",
               blocks=[("h1", "Schéma hydraulique - station de relevage, ligne 1 (POMPE-A-01)"),
                       ("fig", FG.schema_hydraulique("schema_hyd"), "Figure 1.1 - Schéma hydraulique simplifié avec repères des capteurs", 16),
                       ("table", "Tableau 1.1 - Repères", ["Repère", "Organe", "Alarme associée"],
                        [["V1", "Vanne d'aspiration", "-"], ["PS1", "Pressostat d'aspiration", "A02, A09"], ["PT2", "Capteur de pression refoulement", "A03"],
                         ["TT1", "Sonde température palier", "A04, A05"], ["CL", "Clapet anti-retour", "-"], ["V2", "Vanne de refoulement", "-"]], [70, 220, 160])]))
    L.append(D(id="schema_electrique_pompe_a", titre="Schéma électrique de principe - pompe PC-80", equip="POMPE-A-01 ; POMPE-A-02",
               type="schema", version="v2 (2025-01)", groups=G_P, prompt="P08", verifie_par="Adam", ref="SCH-ELEC-PC80 v2", ref_court="schema_electrique_pompe_a v2",
               blocks=[("h1", "Schéma électrique de principe - PC-80"),
                       ("fig", FG.schema_electrique_pompe("schema_elec_pc80"), "Figure 1.1 - Schéma de puissance et de commande simplifié", 14),
                       ("p", "Toute intervention sur ce circuit est réservée au personnel habilité électriquement. L'assistant documentaire n'agit jamais sur le circuit.")]))

    # ------------------------------------------------------------------ 14-16 historiques
    def hist(eq, rows, cap):
        return ("table", cap, ["Date", "N° intervention", "Code / motif", "Opération", "Ticket", "Technicien"], rows, [52, 70, 75, 165, 55, 50])
    L.append(D(id="historique_pompe_a_01", titre="Historique des interventions - POMPE-A-01", equip="POMPE-A-01", type="historique",
               version="v (2026-10)", groups=G_P, prompt="P09", verifie_par="Salah", ref="HIST-POMPE-A-01", ref_court="historique_pompe_a_01",
               remarques="mêmes données que le futur service MCP get_equipment_history(POMPE-A-01) ; codes techniciens anonymisés",
               corrections="vidange préventive de 2026-07 manquante ajoutée (incohérence avec la périodicité 6 mois)",
               blocks=[("h1", "Historique des interventions - POMPE-A-01 (PC-80)"),
                       ("p", "Extraction de l'outil de maintenance (fictif). Les techniciens sont désignés par un code anonyme."),
                       hist("POMPE-A-01", [["2025-01-14", "INT-2025-0007", "préventif", "Vidange huile palier VG 68 (0,6 L)", "TK-1031", "T-04"],
                                           ["2025-04-02", "INT-2025-0061", "A04", "Palier 83 °C : niveau d'huile bas, complément 0,1 L", "TK-1088", "T-02"],
                                           ["2025-04-20", "INT-2025-0079", "A04", "Récidive A04 : alignement corrigé (radial 0,12 mm)", "TK-1102", "T-04"],
                                           ["2025-07-09", "INT-2025-0140", "préventif", "Vidange huile palier", "TK-1167", "T-01"],
                                           ["2025-10-30", "INT-2025-0228", "A07", "Remplacement garniture mécanique", "TK-1240", "T-04"],
                                           ["2026-01-12", "INT-2026-0004", "préventif", "Vidange huile palier", "TK-1302", "T-02"],
                                           ["2026-05-18", "INT-2026-0097", "A09", "Crépine d'aspiration colmatée, nettoyée", "TK-1377", "T-01"],
                                           ["2026-07-08", "INT-2026-0128", "préventif", "Vidange huile palier", "TK-1401", "T-02"],
                                           ["2026-09-03", "INT-2026-0171", "A06", "Vibrations 7,4 mm/s : roulement 6308 remplacé", "TK-1430", "T-04"]],
                            "Tableau 1.1 - Interventions 2025-2026"), PB,
                       ("h1", "Synthèse"),
                       ("p", "Heures de fonctionnement au 2026-10-01 : 31 420 h. Alarmes les plus fréquentes : A04 (2), A07, A09, A06. "
                             "Aucun ticket ouvert au 2026-10-31.")]))
    L.append(D(id="historique_pompe_a_02", titre="Historique des interventions - POMPE-A-02", equip="POMPE-A-02", type="historique",
               version="v (2026-10)", groups=G_P, prompt="P09", verifie_par="Adam", ref="HIST-POMPE-A-02", ref_court="historique_pompe_a_02",
               blocks=[("h1", "Historique des interventions - POMPE-A-02 (PC-80)"),
                       hist("POMPE-A-02", [["2025-02-03", "INT-2025-0019", "préventif", "Vidange huile palier", "TK-1045", "T-02"],
                                           ["2025-08-11", "INT-2025-0161", "A03", "Vanne V2 trouvée fermée aux 3/4 après travaux réseau", "TK-1190", "T-01"],
                                           ["2026-02-24", "INT-2026-0039", "préventif", "Vidange + contrôle alignement", "TK-1331", "T-04"],
                                           ["2026-10-21", "INT-2026-0199", "A04", "Palier 81 °C : huile noircie, vidange anticipée", "TK-1458", "T-02"]],
                            "Tableau 1.1 - Interventions 2025-2026"),
                       ("p", "Ticket ouvert au 2026-10-31 : TK-1461 « surveiller température palier après vidange anticipée ».")]))
    L.append(D(id="historique_pompe_b_01", titre="Historique des interventions - POMPE-B-01", equip="POMPE-B-01", type="historique",
               version="v (2026-10)", groups=G_P, prompt="P09", verifie_par="Adam", ref="HIST-POMPE-B-01", ref_court="historique_pompe_b_01",
               blocks=[("h1", "Historique des interventions - POMPE-B-01 (PC-150)"),
                       hist("POMPE-B-01", [["2025-03-10", "INT-2025-0044", "préventif", "Regraissage roulements 15 g", "TK-1070", "T-03"],
                                           ["2025-06-22", "INT-2025-0118", "B02", "Désamorçage après vidange circuit, réamorcée", "TK-1149", "T-03"],
                                           ["2025-12-05", "INT-2025-0262", "B07", "Roue encrassée (tartre), nettoyée", "TK-1281", "T-05"],
                                           ["2026-04-14", "INT-2026-0072", "B04", "Palier 88 °C : excès de graisse retiré", "TK-1360", "T-03"],
                                           ["2026-08-29", "INT-2026-0165", "préventif", "Regraissage + alignement", "TK-1425", "T-05"]],
                            "Tableau 1.1 - Interventions 2025-2026"), PB,
                       ("h1", "Synthèse"), ("p", "Heures au 2026-10-01 : 18 760 h. Aucun ticket ouvert.")]))

    # ------------------------------------------------------------------ 17 plan préventif pompes
    L.append(D(id="plan_preventif_pompes", titre="Plan de maintenance préventive 2026 - pompes", equip="POMPE-A-01 ; POMPE-A-02 ; POMPE-B-01",
               type="procedure", version="v2026.1 (2026-01)", groups=G_R, prompt="P10", verifie_par="Salah", ref="PMP-POMPES-2026", ref_court="plan_preventif_pompes 2026",
               remarques="réservé aux responsables (planification et coûts) : sert aux tests de contrôle d'accès",
               corrections="échéances de vidange POMPE-A-01 (2026-12 -> 2027-01) et POMPE-A-02 (2026-11 -> 2027-04) recalées sur les historiques",
               blocks=[("h1", "Plan de maintenance préventive 2026 - famille pompes"),
                       ("p", "Document de pilotage réservé aux responsables maintenance (charges, coûts prévisionnels)."),
                       ("table", "Tableau 1.1 - Planning 2026", ["Équipement", "Opération", "Périodicité", "Prochaine échéance", "Charge (h)", "Coût pièces (MAD)"],
                        [["POMPE-A-01", "Vidange huile palier", "2 000 h / 6 mois", "2027-01", "0,5", "120"], ["POMPE-A-01", "Alignement", "annuelle", "2027-04", "2", "0"],
                         ["POMPE-A-02", "Vidange huile palier", "2 000 h / 6 mois", "2027-04", "0,5", "120"], ["POMPE-A-02", "Garniture (préventif)", "8 000 h", "2027-02", "5", "2 400"],
                         ["POMPE-B-01", "Regraissage", "3 000 h", "2027-01", "0,5", "60"], ["POMPE-B-01", "Contrôle roue", "annuelle", "2026-12", "3", "0"]],
                        [65, 100, 75, 70, 50, 70]), PB,
                       ("h1", "Budget et indicateurs"),
                       ("p", "Budget préventif pompes 2026 : 18 500 MAD (fictif). Objectif : moins de 2 arrêts non planifiés par pompe et par an.")]))

    # ------------------------------------------------------------------ 18 guide cavitation (ambigu)
    L.append(D(id="guide_diagnostic_cavitation", titre="Guide de diagnostic - cavitation ou vibrations mécaniques ?", equip="POMPE-A-01 ; POMPE-A-02 ; POMPE-B-01",
               type="procedure", version="v1 (2025-05)", groups=G_P, prompt="P11", verifie_par="Salah", usage="ambigu",
               ref="GD-CAV-01 v1", ref_court="guide_diagnostic_cavitation v1",
               remarques="symptômes communs à A06 et A09 : le système doit demander une précision plutôt que trancher",
               blocks=[
        ("h1", "Cavitation ou vibrations mécaniques : comment les distinguer ?"),
        ("p", "Sur les PC-80, les alarmes A06 (vibrations) et A09 (cavitation suspectée) peuvent s'allumer avec le même voyant orange et des symptômes voisins. "
              "Ce guide aide à orienter le diagnostic ; il ne fournit pas de diagnostic garanti."),
        ("table", "Tableau 1.1 - Indices", ["Indice", "Plutôt cavitation (A09)", "Plutôt mécanique (A06)"],
         [["Bruit", "« gravier » dans la volute", "ronflement régulier, cognement"], ["Évolution avec V2", "diminue si l'on ferme légèrement V2", "inchangé"],
          ["Pression aspiration", "basse (< 0,6 bar)", "normale"], ["Spectre vibratoire", "large bande, haute fréquence", "pic à 1x ou 2x la vitesse"]], [110, 170, 170]),
        PB,
        ("h1", "Démarche"),
        ("ol", ["Relever le code exact : A06, A09 ou les deux.", "Relever la pression d'aspiration (PS1) et la position de V1.", "Écouter la pompe (casque antibruit).",
                "Si les deux codes sont présents, traiter d'abord la cavitation : elle peut provoquer les vibrations."]),
        ("p", "<b>Cas ambigu :</b> si seul le voyant orange est connu (sans code), plusieurs causes restent possibles (A03, A04, A06, A07, A09). Il faut alors demander le code ou une mesure complémentaire."),
        PB,
        ("h1", "Exemples"),
        ("p", "Exemple 1 : POMPE-A-01, mai 2026 - A09 + bruit de gravier, crépine colmatée (INT-2026-0097). Exemple 2 : POMPE-A-01, septembre 2026 - A06 seul, roulement usé (INT-2026-0171)."),
    ]))

    # ------------------------------------------------------------------ 19 note vibrations (EN)
    L.append(D(id="note_vibrations_pompes_en", titre="Technical note - vibration monitoring of centrifugal pumps (EN)", equip="POMPE-A-01 ; POMPE-A-02 ; POMPE-B-01",
               type="procedure", version="v1.0 (2025-02)", groups=G_P, prompt="P12", verifie_par="Adam", lang="en",
               ref="VIB-PC-EN v1.0", ref_court="note_vibrations_pompes_en v1.0", remarques="document en anglais (signalé) ; tests multilingues",
               corrections="légende de la figure 2.1 : seuil 4,5 mm/s faussement attribué à une zone ISO 10816-3, remplacé par le seuil constructeur PC-150 (B06)",
               blocks=[
        ("h1", "Technical note: vibration monitoring of PC-80 and PC-150 pumps"),
        ("p", "This note explains how to measure bearing vibration on FICTIA centrifugal pumps and how to interpret alarm codes A06 (PC-80) and B06 (PC-150)."),
        ("table", "Table 1.1 - Measurement points", ["Point", "Location", "Direction"], [["P1", "Pump bearing, coupling side", "radial horizontal"],
            ["P2", "Pump bearing, coupling side", "radial vertical"], ["P3", "Motor bearing, drive end", "radial horizontal"]], [60, 220, 170]),
        ("p", "Measure velocity RMS (10-1000 Hz) with the pump at nominal flow, after at least 30 minutes of operation."),
        PB,
        ("h1", "Trend analysis"),
        ("fig", FG.tendance_vibrations("tendance_vib"), "Figure 2.1 - Vibration trend before bearing replacement (synthetic data)", 15),
        ("p", "A steady increase followed by a sharp rise is typical of rolling bearing wear. On POMPE-A-01 the bearing was replaced when 7.4 mm/s was reached (alarm A06)."),
        PB,
        ("h1", "Thresholds"),
        ("table", "Table 3.1 - Alarm thresholds", ["Model", "Alert (orange)", "Code"], [["PC-80", "7.1 mm/s", "A06"], ["PC-150", "4.5 mm/s", "B06"]], [150, 150, 150]),
        ("p", "Note: the PC-150 runs at 1,450 rpm and has a stricter threshold. Do not apply PC-80 thresholds to the PC-150."),
    ]))

    # ------------------------------------------------------------------ 20 checklist mise en service PC-150 (scannée)
    L.append(D(id="checklist_mise_en_service_pompe_b", titre="Check-list de mise en service - PC-150", equip="POMPE-B-01", type="procedure",
               version="v1 (2021-04)", groups=G_P, prompt="P13", verifie_par="Adam", format="pdf_scanne", scan=True,
               ref="CL-MES-PC150 v1", ref_court="checklist_mise_en_service_pompe_b v1", remarques="document scanné avec cases cochées : test OCR",
               blocks=[("h1", "Check-list de mise en service - POMPE-B-01 (PC-150)"),
                       ("p", "Date de mise en service : 2021-04-12. Formulaire rempli à la main puis scanné."),
                       ("table", "Tableau 1.1 - Contrôles avant démarrage", ["N°", "Contrôle", "OK", "Remarque"],
                        [["1", "Socle scellé, boulons serrés", "☑", ""], ["2", "Alignement ≤ 0,08 mm", "☑", "0,06 mm"], ["3", "Sens de rotation vérifié", "☑", ""],
                         ["4", "Pompe amorcée (PROC-AMO-PC150)", "☑", ""], ["5", "Roulements graissés", "☑", "graisse d'origine"], ["6", "Protection accouplement en place", "☑", ""],
                         ["7", "Capteurs pression et température raccordés", "☐", "sonde palier livrée le 2021-04-15"]], [30, 250, 40, 130]),
                       PB, ("h1", "Relevés après 1 heure"),
                       ("table", "Tableau 2.1 - Relevés", ["Grandeur", "Valeur relevée", "Attendu"],
                        [["Pression refoulement", "4,3 bar", "4 à 5 bar"], ["Débit", "148 m³/h", "150 m³/h"], ["Vibrations P1", "1,9 mm/s", "< 4,5 mm/s"],
                         ["Température palier", "52 °C", "< 85 °C"]], [150, 150, 150]),
                       ("p", "Mise en service validée par : responsable maintenance (code R-01).")]))
    return L
