# -*- coding: utf-8 -*-
"""Figures techniques (schémas simplifiés) dessinées par code pour le corpus synthétique."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch, FancyArrowPatch, Polygon
from refs import VOYANTS

OUT = os.path.join(os.path.dirname(__file__), "build_fig")
os.makedirs(OUT, exist_ok=True)
COL = {"vert": "#2e9d3a", "orange": "#f08c00", "rouge": "#d62828", "bleu": "#1f6fd1"}


def _save(fig, name):
    p = os.path.join(OUT, name + ".png")
    fig.savefig(p, dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return p


def _ax(w=7, h=4):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, txt, fc="#eef2f7", fs=8):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", fc=fc, ec="#222", lw=1))
    ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=fs)


def arrow(ax, x1, y1, x2, y2, txt=None, c="#222"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=12, lw=1.3, color=c))
    if txt:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.12, txt, ha="center", fontsize=7, color=c)


def courbe_pompe(model, qn, hn, name):
    q = np.linspace(0, qn * 1.4, 100)
    h = hn * 1.25 - (hn * 0.25) * (q / qn) ** 2
    eta = 78 * (2 * (q / qn) - (q / qn) ** 2)
    npsh = 1.5 + 2.5 * (q / qn) ** 2
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.plot(q, h, lw=2, label="HMT (m)")
    ax.plot(q, np.clip(eta, 0, None) / 2, lw=1.5, ls="--", label="Rendement (% / 2)")
    ax.plot(q, npsh, lw=1.5, ls=":", label="NPSH requis (m)")
    ax.axvline(qn, color="grey", lw=0.8); ax.text(qn, hn * 1.3, " point nominal", fontsize=8)
    ax.set_xlabel("Débit Q (m³/h)"); ax.set_ylabel("m"); ax.grid(alpha=0.3); ax.legend(fontsize=8)
    ax.set_title(f"Courbes caractéristiques {model} (données fictives)", fontsize=10)
    return _save(fig, name)


def vue_eclatee_pompe(name):
    fig, ax = _ax(7, 3.6)
    ax.add_patch(Circle((2, 2), 1.3, fc="#d9dee6", ec="#222"))          # volute
    ax.add_patch(Circle((2, 2), 0.7, fc="#b9c2cf", ec="#222"))          # roue
    ax.add_patch(Rectangle((3.3, 1.7), 1.2, 0.6, fc="#cfd6df", ec="#222"))  # garniture/lanterne
    ax.add_patch(Rectangle((4.5, 1.4), 1.6, 1.2, fc="#e6e9ee", ec="#222"))  # palier
    ax.add_patch(Rectangle((6.1, 1.85), 0.6, 0.3, fc="#999", ec="#222"))    # accouplement
    ax.add_patch(Rectangle((6.7, 1.2), 2.3, 1.6, fc="#c6d3e3", ec="#222"))  # moteur
    ax.plot([0.2, 9.2], [2, 2], color="#555", lw=0.8, ls="-.")
    pts = [(1.2, 3.4, "1 Volute"), (2.0, 0.3, "2 Roue"), (3.9, 3.0, "3 Garniture mécanique"),
           (5.3, 3.2, "4 Palier (huile)"), (6.4, 0.6, "5 Accouplement"), (7.9, 3.3, "6 Moteur 11 kW"),
           (4.9, 0.5, "7 Bouchon de vidange")]
    anchors = [(1.6, 3.2), (2.0, 1.4), (3.9, 2.3), (5.3, 2.6), (6.4, 1.85), (7.9, 2.8), (4.9, 1.4)]
    for (tx, ty, t), (axx, ayy) in zip(pts, anchors):
        ax.annotate(t, (axx, ayy), (tx, ty), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_xlim(0, 9.5); ax.set_ylim(0, 3.8)
    return _save(fig, name)


def panneau(model, name, actif=None, ecran=None):
    vs = VOYANTS[model]
    fig, ax = _ax(7, 3)
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 9.6, 3.4, boxstyle="round,pad=0.05", fc="#cfd3d8", ec="#333", lw=1.5))
    ax.text(5, 3.25, f"FICTIA {model} - panneau de commande", ha="center", fontsize=9, weight="bold")
    x0 = 1.0
    for i, (c, lab) in enumerate(vs):
        x = x0 + i * 1.6
        on = (actif == c)
        ax.add_patch(Circle((x, 2.1), 0.42, fc=COL[c] if on else COL[c] + "55", ec="#222", lw=1.2))
        ax.text(x, 1.35, lab, ha="center", fontsize=7)
        ax.text(x, 2.85, f"H{i+1}", ha="center", fontsize=7, color="#444")
    if ecran:
        ax.add_patch(Rectangle((7.3, 1.5), 2.2, 1.1, fc="#123", ec="#000"))
        ax.text(8.4, 2.05, ecran, ha="center", va="center", fontsize=9, color="#7fffb0", family="monospace")
    ax.add_patch(Circle((8.6 if not ecran else 8.4, 0.8), 0.35, fc="#c00", ec="#222")); ax.text(8.6 if not ecran else 8.4, 0.25, "AU", ha="center", fontsize=7)
    ax.add_patch(Rectangle((1.0, 0.55), 1.0, 0.35, fc="#2a2", ec="#222")); ax.text(1.5, 0.3, "I marche", ha="center", fontsize=7)
    ax.add_patch(Rectangle((2.6, 0.55), 1.0, 0.35, fc="#555", ec="#222")); ax.text(3.1, 0.3, "O arrêt", ha="center", fontsize=7)
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.8)
    return _save(fig, name)


def schema_hydraulique(name):
    fig, ax = _ax(8, 3.4)
    box(ax, 0.2, 0.6, 1.4, 1.6, "Bâche\nd'aspiration")
    box(ax, 2.0, 1.1, 0.7, 0.6, "V1"); ax.text(2.35, 0.85, "vanne asp.", ha="center", fontsize=6)
    box(ax, 3.1, 1.1, 0.6, 0.6, "PS1"); ax.text(3.4, 0.85, "pressostat\n(A02/A09)", ha="center", fontsize=6, va="top")
    ax.add_patch(Circle((4.6, 1.4), 0.55, fc="#cfe0f5", ec="#222")); ax.text(4.6, 1.4, "P1\nPC-80", ha="center", va="center", fontsize=7)
    box(ax, 5.6, 1.1, 0.6, 0.6, "PT2"); ax.text(5.9, 0.85, "capteur\n(A03)", ha="center", fontsize=6, va="top")
    box(ax, 6.5, 1.1, 0.6, 0.6, "CL"); ax.text(6.8, 0.85, "clapet", ha="center", fontsize=6, va="top")
    box(ax, 7.4, 1.1, 0.7, 0.6, "V2"); ax.text(7.75, 0.85, "vanne ref.", ha="center", fontsize=6, va="top")
    for a, b in [(1.6, 2.0), (2.7, 3.1), (3.7, 4.05), (5.15, 5.6), (6.2, 6.5), (7.1, 7.4)]:
        arrow(ax, a, 1.4, b, 1.4)
    arrow(ax, 8.1, 1.4, 8.9, 1.4, "réseau")
    ax.add_patch(Circle((4.6, 2.35), 0.2, fc="white", ec="#222")); ax.text(4.6, 2.7, "TT1 palier (A04/A05)", ha="center", fontsize=6)
    ax.set_xlim(0, 9.2); ax.set_ylim(0.3, 3.0)
    return _save(fig, name)


def schema_electrique_pompe(name):
    fig, ax = _ax(7, 4)
    y = 3.4
    for x in (1, 1.4, 1.8):
        ax.plot([x, x], [3.8, 0.9], color="#222", lw=1)
    ax.text(1.4, 3.9, "L1 L2 L3 400 V", ha="center", fontsize=8)
    for yy, t in [(3.1, "Q1 sectionneur porte-fusibles"), (2.4, "U1 variateur 11 kW (A08)"), (1.7, "F2 relais thermique (A01)")]:
        ax.add_patch(Rectangle((0.8, yy - 0.2), 1.2, 0.4, fc="#eef", ec="#222")); ax.text(2.2, yy, t, fontsize=8, va="center")
    ax.add_patch(Circle((1.4, 0.7), 0.35, fc="#cde", ec="#222")); ax.text(1.4, 0.7, "M1", ha="center", va="center", fontsize=8)
    box(ax, 5.0, 2.2, 1.8, 1.4, "Automate\nK1\nentrées capteurs\nPS1 PT2 TT1\nVT1 LS1", fs=7)
    arrow(ax, 5.0, 2.9, 3.9, 2.4, "ordre marche")
    ax.text(5.9, 1.8, "sorties voyants H1..H4", ha="center", fontsize=7)
    ax.set_xlim(0, 7.2); ax.set_ylim(0.2, 4.1)
    return _save(fig, name)


def garniture(name):
    fig, ax = _ax(7, 3)
    ax.add_patch(Rectangle((0.3, 1.3), 6.4, 0.4, fc="#bbb", ec="#222")); ax.text(6.8, 1.5, "arbre", fontsize=8, va="center")
    for (x, w, c, t, ty) in [(1.5, 0.5, "#9fc5e8", "grain fixe (carbure)", 2.6), (2.0, 0.5, "#f6b26b", "grain tournant (carbone)", 0.2),
                              (2.5, 0.9, "#ccc", "ressort", 2.6), (3.4, 0.4, "#93c47d", "joint torique", 0.2)]:
        ax.add_patch(Rectangle((x, 1.7), w, 0.6, fc=c, ec="#222")); ax.add_patch(Rectangle((x, 0.7), w, 0.6, fc=c, ec="#222"))
        ax.annotate(t, (x + w / 2, 2.3 if ty > 1 else 0.7), (x, ty), fontsize=7, arrowprops=dict(arrowstyle="-", lw=0.6))
    ax.text(0.3, 2.9, "Coupe simplifiée - garniture mécanique simple PC-80", fontsize=8, weight="bold")
    ax.set_xlim(0, 7.5); ax.set_ylim(0, 3.1)
    return _save(fig, name)


def alignement(name):
    fig, ax = _ax(7, 3)
    ax.add_patch(Rectangle((0.5, 1.0), 2.5, 1.2, fc="#cfe0f5", ec="#222")); ax.text(1.75, 1.6, "Pompe", ha="center", fontsize=8)
    ax.add_patch(Rectangle((3.6, 0.95), 2.8, 1.3, fc="#c6d3e3", ec="#222")); ax.text(5.0, 1.6, "Moteur", ha="center", fontsize=8)
    ax.add_patch(Rectangle((3.0, 1.35), 0.6, 0.5, fc="#999", ec="#222"))
    ax.add_patch(Circle((3.3, 2.6), 0.25, fc="white", ec="#222")); ax.plot([3.3, 3.3], [2.35, 1.85], color="#222")
    ax.text(3.7, 2.6, "comparateur (radial / axial)", fontsize=7, va="center")
    ax.text(0.5, 0.4, "Tolérances : écart radial ≤ 0,05 mm ; écart angulaire ≤ 0,05 mm / 100 mm", fontsize=7)
    ax.set_xlim(0, 7); ax.set_ylim(0, 3.1)
    return _save(fig, name)


def circuit_air_huile(name):
    fig, ax = _ax(8.5, 4)
    box(ax, 0.1, 2.6, 1.3, 0.7, "Filtre à air\n(C05)")
    box(ax, 1.9, 2.6, 1.4, 0.7, "Élément vis\nTT11 (C01/C02)")
    box(ax, 3.8, 2.4, 1.6, 1.1, "Réservoir\nséparateur")
    box(ax, 5.9, 2.6, 1.4, 0.7, "Séparateur\nΔp (C06)")
    box(ax, 7.6, 2.6, 1.4, 0.7, "Clapet de\npression mini")
    box(ax, 7.6, 1.2, 1.4, 0.7, "Refroidisseur\nair")
    box(ax, 7.6, 0.1, 1.4, 0.7, "Purgeur\n(C08)")
    box(ax, 3.8, 0.9, 1.6, 0.7, "Vanne\nthermostatique")
    box(ax, 1.9, 0.9, 1.4, 0.7, "Filtre à huile")
    box(ax, 3.8, 0.0, 1.6, 0.6, "Refroidisseur huile")
    for a in [((1.4, 2.95), (1.9, 2.95)), ((3.3, 2.95), (3.8, 2.95)), ((5.4, 2.95), (5.9, 2.95)),
              ((7.3, 2.95), (7.6, 2.95)), ((8.3, 2.6), (8.3, 1.9)), ((8.3, 1.2), (8.3, 0.8))]:
        arrow(ax, *a[0], *a[1])
    arrow(ax, 4.6, 2.4, 4.6, 1.6, c="#b45f06"); arrow(ax, 3.8, 1.25, 3.3, 1.25, c="#b45f06")
    arrow(ax, 2.6, 1.6, 2.6, 2.6, c="#b45f06"); arrow(ax, 4.6, 0.9, 4.6, 0.6, c="#b45f06")
    ax.text(9.1, 1.55, "sortie\nréseau\n7,5 bar", fontsize=7)
    ax.text(0.1, 0.2, "— air    — huile (orange)", fontsize=7)
    ax.set_xlim(0, 9.8); ax.set_ylim(-0.1, 3.5)
    return _save(fig, name)


def schema_elec_comp(name):
    fig, ax = _ax(7, 3.6)
    box(ax, 0.2, 2.6, 1.6, 0.7, "Q1 sectionneur", fs=7)
    box(ax, 2.2, 2.6, 1.4, 0.7, "KM1 ligne", fs=7)
    box(ax, 4.0, 3.0, 1.4, 0.6, "KM2 étoile", fs=7)
    box(ax, 4.0, 2.2, 1.4, 0.6, "KM3 triangle", fs=7)
    box(ax, 5.9, 2.4, 1.0, 0.9, "M1\n37 kW", fs=7)
    box(ax, 2.2, 0.6, 2.4, 1.1, "Contrôleur CTR-37\nécran + voyants\nentrées PT1 TT11", fs=7)
    box(ax, 5.0, 0.6, 1.9, 1.1, "Protection moteur\n(C09) + AU (C10)", fs=7)
    for a in [((1.8, 2.95), (2.2, 2.95)), ((3.6, 2.95), (4.0, 3.3)), ((3.6, 2.95), (4.0, 2.5)),
              ((5.4, 3.3), (5.9, 2.9)), ((5.4, 2.5), (5.9, 2.8))]:
        arrow(ax, *a[0], *a[1])
    ax.text(0.2, 0.2, "Démarrage étoile-triangle, temporisation 8 s", fontsize=7)
    ax.set_xlim(0, 7.2); ax.set_ylim(0, 3.8)
    return _save(fig, name)


def piston(name):
    fig, ax = _ax(7, 3.4)
    box(ax, 0.3, 1.0, 1.4, 1.4, "Cylindre\nBP")
    box(ax, 2.3, 1.2, 1.2, 1.0, "Refroid.\ninter-étage")
    box(ax, 4.0, 1.0, 1.4, 1.4, "Cylindre\nHP\n(P03)")
    box(ax, 5.9, 0.7, 1.0, 2.0, "Réservoir\n270 L\n(P04/P05)")
    for a in [((1.7, 1.7), (2.3, 1.7)), ((3.5, 1.7), (4.0, 1.7)), ((5.4, 1.7), (5.9, 1.7))]:
        arrow(ax, *a[0], *a[1])
    ax.text(0.3, 0.3, "Two-stage piston compressor CP-11 - simplified diagram (fictitious)", fontsize=7)
    ax.set_xlim(0, 7.2); ax.set_ylim(0, 3.0)
    return _save(fig, name)


def tendance_vibrations(name):
    rng = np.random.default_rng(3)
    d = np.arange(0, 120, 5)
    v = 2.2 + 0.015 * d + rng.normal(0, 0.15, len(d)); v[-5:] += np.linspace(0.5, 3.0, 5)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.plot(d, v, marker="o", ms=3)
    ax.axhline(4.5, color="orange", ls="--", label="PC-150 alert threshold B06 (4.5 mm/s)")
    ax.axhline(7.1, color="red", ls="--", label="PC-80 alarm A06 (7.1 mm/s)")
    ax.set_xlabel("Days"); ax.set_ylabel("Velocity RMS (mm/s)"); ax.legend(fontsize=7); ax.grid(alpha=0.3)
    ax.set_title("Bearing vibration trend - POMPE-A-01 (synthetic data)", fontsize=9)
    return _save(fig, name)


def purgeur(name):
    fig, ax = _ax(7, 2.8)
    box(ax, 0.3, 1.0, 1.6, 1.0, "Réservoir /\nrefroidisseur")
    box(ax, 2.5, 1.0, 1.2, 1.0, "Vanne\nd'isolement")
    box(ax, 4.3, 1.0, 1.4, 1.0, "Purgeur\nélectronique")
    box(ax, 6.2, 1.0, 1.4, 1.0, "Séparateur\neau/huile")
    for a in [((1.9, 1.5), (2.5, 1.5)), ((3.7, 1.5), (4.3, 1.5)), ((5.7, 1.5), (6.2, 1.5))]:
        arrow(ax, *a[0], *a[1])
    ax.text(0.3, 0.4, "Les condensats huileux ne sont jamais rejetés directement à l'égout.", fontsize=7)
    ax.set_xlim(0, 7.8); ax.set_ylim(0.2, 2.3)
    return _save(fig, name)


def consignation(name):
    fig, ax = _ax(8, 2.4)
    steps = ["1 Préparer", "2 Séparer\n(Q1 ouvert)", "3 Condamner\n(cadenas)", "4 Identifier\n(étiquette)", "5 Vérifier\nabsence énergie", "6 Purger\npression/fluide"]
    for i, s in enumerate(steps):
        box(ax, 0.1 + i * 1.35, 0.8, 1.15, 0.9, s, fc="#fff2cc", fs=7)
        if i < 5:
            arrow(ax, 1.25 + i * 1.35, 1.25, 1.45 + i * 1.35, 1.25)
    ax.set_xlim(0, 8.2); ax.set_ylim(0.5, 2.0)
    return _save(fig, name)
