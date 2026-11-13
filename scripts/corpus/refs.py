# -*- coding: utf-8 -*-
"""Référentiel unique du corpus MaintiDoc (source de vérité pour la cohérence).
Tous les documents, l'inventaire et le contrôle de cohérence lisent ce fichier.
Marque, modèles, sites, personnes : entièrement fictifs."""

MARQUE = "FICTIA Industrie (marque fictive)"
DATE_GEN = "2026-11-13"
OUTIL = "Claude Opus 5.5 (Anthropic, claude.ai)"

MODELES = {
    "PC-80": dict(famille="pompes", nom="Pompe centrifuge monocellulaire FICTIA PC-80",
                  debit="80 m³/h", hmt="32 m", puissance="11 kW", vitesse="2 900 tr/min",
                  pmax="6 bar", t_palier_alerte=80, t_palier_arret=95,
                  equipements=["POMPE-A-01", "POMPE-A-02"]),
    "PC-150": dict(famille="pompes", nom="Pompe centrifuge FICTIA PC-150",
                   debit="150 m³/h", hmt="45 m", puissance="30 kW", vitesse="1 450 tr/min",
                   pmax="8 bar", t_palier_alerte=85, t_palier_arret=100,
                   equipements=["POMPE-B-01"]),
    "CV-37": dict(famille="compresseurs", nom="Compresseur à vis lubrifié FICTIA CV-37",
                  debit="6,2 m³/min", pression="7,5 bar", puissance="37 kW",
                  t_alerte=105, t_arret=110, vidange_h=4000,
                  equipements=["COMP-V-01", "COMP-V-02"]),
    "CP-11": dict(famille="compresseurs", nom="Compresseur à piston bi-étagé FICTIA CP-11",
                  debit="1,4 m³/min", pression="10 bar", puissance="11 kW",
                  equipements=["COMP-P-01"]),
}

EQUIPEMENTS = {
    "POMPE-A-01": ("PC-80", "Station de relevage - ligne 1", "N° série FP80-2019-0417"),
    "POMPE-A-02": ("PC-80", "Station de relevage - ligne 2", "N° série FP80-2020-0122"),
    "POMPE-B-01": ("PC-150", "Circuit eau de refroidissement", "N° série FP150-2021-0033"),
    "COMP-V-01": ("CV-37", "Local air comprimé - poste 1", "N° série FV37-2018-0910"),
    "COMP-V-02": ("CV-37", "Local air comprimé - poste 2", "N° série FV37-2022-0215"),
    "COMP-P-01": ("CP-11", "Atelier mécanique", "N° série FP11-2017-0588"),
}

# Codes d'alarme : code -> (voyant, libellé, seuil / condition, action immédiate)
CODES = {
    "PC-80": {
        "A01": ("rouge", "Défaut thermique moteur", "déclenchement relais thermique F2", "Arrêt automatique. Consigner, contrôler l'intensité et la ventilation moteur."),
        "A02": ("rouge", "Marche à sec / manque d'eau", "pression aspiration < 0,3 bar pendant 5 s", "Arrêt automatique. Vérifier niveau bâche et vanne d'aspiration V1."),
        "A03": ("orange", "Pression de refoulement haute", "pression refoulement > 6 bar", "Vérifier l'ouverture de la vanne de refoulement V2 et le clapet."),
        "A04": ("orange", "Température palier élevée", "palier côté accouplement > 80 °C", "Contrôler niveau et état de l'huile palier, puis l'alignement."),
        "A05": ("rouge", "Température palier critique", "palier > 95 °C", "Arrêt automatique. Ne pas redémarrer avant contrôle du palier."),
        "A06": ("orange", "Vibrations élevées", "vitesse vibratoire > 7,1 mm/s eff.", "Contrôler alignement, fixation du socle et état des roulements."),
        "A07": ("orange", "Fuite garniture mécanique", "capteur de fuite humide pendant 30 s", "Planifier le remplacement de la garniture (procédure dédiée)."),
        "A08": ("rouge", "Défaut variateur", "défaut remonté par le variateur U1", "Lire le code du variateur, consigner avant toute intervention."),
        "A09": ("orange", "Cavitation suspectée", "pression aspiration < 0,6 bar et bruit/vibrations", "Vérifier crépine, vanne V1 et niveau ; voir guide cavitation."),
        "A10": ("orange clignotant", "Perte de communication capteur", "absence de signal capteur > 10 s", "Contrôler câblage et connecteurs des capteurs."),
    },
    "PC-150": {
        "B01": ("rouge", "Défaut thermique moteur", "déclenchement relais thermique", "Arrêt automatique. Contrôler intensité et ventilation."),
        "B02": ("rouge", "Marche à sec", "pression aspiration < 0,2 bar pendant 5 s", "Arrêt automatique. Vérifier amorçage et niveau."),
        "B03": ("orange", "Pression de refoulement haute", "pression refoulement > 8 bar", "Vérifier vannes et circuit aval."),
        "B04": ("orange", "Température palier élevée", "palier > 85 °C", "Contrôler graissage des roulements (graisse, pas d'huile)."),
        "B05": ("rouge", "Température palier critique", "palier > 100 °C", "Arrêt automatique. Contrôle roulements obligatoire."),
        "B06": ("orange", "Vibrations élevées", "vitesse vibratoire > 4,5 mm/s eff.", "Contrôler alignement et roulements."),
        "B07": ("orange", "Débit faible", "débit < 40 m³/h en marche", "Vérifier vanne refoulement et encrassement de la roue."),
        "B08": ("rouge", "Arrêt d'urgence", "bouton AU actionné", "Identifier la cause avant réarmement."),
    },
    "CV-37": {
        "C01": ("orange", "Température de sortie élément élevée", "> 105 °C", "Contrôler niveau d'huile et propreté du refroidisseur."),
        "C02": ("rouge", "Température de sortie élément critique", "> 110 °C", "Arrêt automatique. Laisser refroidir avant contrôle."),
        "C03": ("rouge", "Surpression réseau", "> 8,5 bar", "Arrêt automatique. Contrôler capteur et soupape."),
        "C04": ("rouge", "Sens de rotation inversé", "détecté au démarrage", "Inverser deux phases (électricien habilité)."),
        "C05": ("orange", "Filtre à air colmaté", "Δp filtre à air > 50 mbar", "Remplacer la cartouche du filtre à air."),
        "C06": ("orange", "Séparateur d'huile colmaté", "Δp séparateur > 1 bar", "Remplacer l'élément séparateur (procédure dédiée)."),
        "C07": ("orange", "Entretien dû", "compteur d'heures atteint", "Planifier l'entretien selon le plan préventif."),
        "C08": ("orange", "Défaut purgeur de condensats", "pas de purge détectée en 30 min", "Contrôler le purgeur électronique et son filtre."),
        "C09": ("rouge", "Défaut thermique moteur", "déclenchement protection moteur", "Arrêt. Contrôler intensité et ventilation."),
        "C10": ("rouge", "Arrêt d'urgence activé", "bouton AU actionné", "Identifier la cause avant réarmement."),
        "C11": ("orange", "Température ambiante basse", "< 1 °C", "Risque de gel des condensats : chauffer le local."),
        "C12": ("rouge", "Défaut capteur de pression", "signal hors plage", "Arrêt. Contrôler capteur PT1 et câblage."),
    },
    "CP-11": {
        "P01": ("rouge", "Défaut thermique moteur", "relais thermique", "Arrêt. Contrôler intensité."),
        "P02": ("orange", "Niveau d'huile carter bas", "contact niveau ouvert", "Compléter avec l'huile préconisée."),
        "P03": ("rouge", "Température refoulement HP élevée", "> 180 °C", "Arrêt. Contrôler clapets et refroidissement."),
        "P04": ("orange", "Purge réservoir à effectuer", "temporisation 8 h atteinte", "Purger le réservoir (procédure purge)."),
        "P05": ("rouge", "Soupape de sécurité ouverte", "pressostat > 11 bar", "Arrêt. Contrôler pressostat de régulation."),
        "P06": ("orange", "Courroie à contrôler", "compteur 500 h", "Contrôler tension et usure de la courroie."),
    },
}

# Voyants des panneaux (ordre gauche -> droite). Même disposition pour PC-80 et CV-37 : source d'ambiguïté voulue.
VOYANTS = {
    "PC-80": [("vert", "MARCHE"), ("orange", "ALERTE"), ("rouge", "DÉFAUT"), ("bleu", "MANU")],
    "PC-150": [("vert", "MARCHE"), ("orange", "ALERTE"), ("rouge", "DÉFAUT")],
    "CV-37": [("vert", "EN CHARGE"), ("orange", "ALERTE / ENTRETIEN"), ("rouge", "DÉFAUT")],
    "CP-11": [("vert", "MARCHE"), ("orange", "ALERTE"), ("rouge", "DÉFAUT")],
}

GROUPES = {
    "techniciens_pompes": "Techniciens de maintenance affectés aux pompes",
    "techniciens_compresseurs": "Techniciens de maintenance affectés aux compresseurs",
    "responsables": "Responsables maintenance (accès à tout le corpus)",
}
UTILISATEURS = {
    "tech_pompe_01": ["techniciens_pompes"],
    "tech_pompe_02": ["techniciens_pompes"],
    "tech_comp_01": ["techniciens_compresseurs"],
    "resp_maint_01": ["responsables"],
}

G_P = "techniciens_pompes ; responsables"
G_C = "techniciens_compresseurs ; responsables"
G_ALL = "techniciens_pompes ; techniciens_compresseurs ; responsables"
G_R = "responsables"
