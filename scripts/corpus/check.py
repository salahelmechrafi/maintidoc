# -*- coding: utf-8 -*-
"""Contrôle de cohérence croisée du corpus. Usage : python check.py <dossier_corpus>"""
import os, re, sys, csv, json
import pymupdf as fitz
from refs import CODES, EQUIPEMENTS, GROUPES
import docs_pompes, docs_comp

ROOT = sys.argv[1]
docs = {d["id"]: d for d in docs_pompes.docs() + docs_comp.docs()}
refs_docs = {d["ref"].split(" v")[0].strip(): i for i, d in docs.items()}
all_codes = {c: m for m, cs in CODES.items() for c in cs}
issues = []


def text_of(d):
    return fitz.open(os.path.join(os.path.dirname(__file__), "build_tmp", d + ".pdf")).get_text() if True else ""


for i, d in docs.items():
    t = "\n".join(p.get_text() for p in fitz.open(os.path.join(os.path.dirname(__file__), "build_tmp", i + ".pdf")))
    models_doc = {EQUIPEMENTS[e.strip()][0] for e in d["equip"].split(";")}
    for c in set(re.findall(r"\b([ABCP]\d{2})\b", t)):
        if c not in all_codes:
            issues.append(f"{i}: code inconnu {c}")
        elif all_codes[c] not in models_doc and i != "codes_alarme_pompe_b":  # tableau de correspondance volontaire
            issues.append(f"{i}: code {c} ({all_codes[c]}) cité dans un document {sorted(models_doc)}")
    for e in set(re.findall(r"\b(POMPE-[AB]-0\d|COMP-[VP]-0\d)\b", t)):
        if e not in EQUIPEMENTS:
            issues.append(f"{i}: équipement inconnu {e}")
    for r in set(re.findall(r"\b((?:PROC|FS|SCH|MAN|TAB|GD|VIB|CL|FDS|HIST|PMP|NS|GUIDE|FICHE)-[A-Z0-9-]+)", t)):
        r = r.rstrip("-")
        if r not in refs_docs and not any(k.startswith(r) for k in refs_docs):
            issues.append(f"{i}: référence documentaire introuvable {r}")
    for g in d["groups"].split(";"):
        if g.strip() not in GROUPES:
            issues.append(f"{i}: groupe inconnu {g}")

# inventaire <-> fichiers
inv = list(csv.DictReader(open(os.path.join(ROOT, "inventaire.csv"), encoding="utf-8")))
files = {os.path.relpath(os.path.join(dp, f), ROOT) for dp, _, fs in os.walk(ROOT) for f in fs
         if not f.endswith((".csv", ".md"))}
listed = {r["fichier"] for r in inv}
for f in files - listed: issues.append(f"fichier absent de l'inventaire : {f}")
for f in listed - files: issues.append(f"ligne d'inventaire sans fichier : {f}")
for r in inv:
    if os.path.splitext(os.path.basename(r["fichier"]))[0] != r["document_id"]:
        issues.append(f"nom de fichier != document_id : {r['fichier']}")
ids = [r["document_id"] for r in inv]
if len(ids) != len(set(ids)): issues.append("document_id dupliqués")
print("\n".join(issues) if issues else "OK - aucune incohérence détectée")
print(f"{len(inv)} documents, {sum(1 for r in inv if r['format']=='pdf_scanne')} scannés, "
      f"{sum(1 for r in inv if r['elements_visuels']!='aucun')} avec éléments visuels, "
      f"usages: " + json.dumps({u: sum(1 for r in inv if r['usage_test']==u) for u in ['normal','contradictoire','injection','ambigu']}))

# numérotation des interventions / tickets : unique et croissante avec la date (cohérence future base MCP)
ev = []
for i, d in docs.items():
    if d["type"] == "historique":
        for b in d["blocks"]:
            if b[0] == "table":
                for r in b[3]:
                    ev.append((r[0], r[1], r[4], i))
ev.sort()
for k in (1, 2):
    nums = [e[k] for e in ev]
    if len(nums) != len(set(nums)): print("DOUBLON", k)
    for a, b in zip(ev, ev[1:]):
        if a[k] > b[k] and a[k][:7] == b[k][:7] or (k == 2 and a[k] > b[k]):
            print(f"ordre non chronologique : {a[k]} ({a[0]}, {a[3]}) > {b[k]} ({b[0]}, {b[3]})")
