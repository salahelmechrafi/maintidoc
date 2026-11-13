import csv, json, sys, os
COLS="document_id,fichier,titre,famille_equipement,equipement_id,type_document,version,nb_pages,langue,format,elements_visuels,provenance,licence,genere_par_ia,outil_ia,verifie_par,corrections,groupe_acces,usage_test,remarques".split(",")
rows=json.load(open(os.path.join(os.path.dirname(__file__),"build_tmp/rows.json")))
with open(os.path.join(sys.argv[1],"inventaire.csv"),"w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=COLS); w.writeheader(); [w.writerow(r) for r in rows]
