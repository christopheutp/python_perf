import json

catalogue = {
  "produits": [
    {"id": 1, "nom": "Stylo", "prix": 1.8},
    {"id": 2, "nom": "Cahier", "prix": 2.5},
    {"id": 3, "nom": "Sac",   "prix": 19.9}
  ]
}


# a) Sauvegarde ce dict dans un fichier `catalogue.json` (joli avec `indent=2`).
with open("catalogue.json","w",encoding='UTF-8') as f :
    json.dump(catalogue,f,indent=2)

#    b) Relis le fichier et calcule le **prix total** de tous les produits.
with open("catalogue.json","r",encoding='UTF-8') as f :
    data = json.load(f)

total = sum(p["prix"] for p in data["produits"])

#    c) Ajoute une clé `"total"` au dict rechargé avec ce montant.

data["total"] = total

#    d) Convertis le dict enrichi en **chaîne JSON** et affiche-la.

json_str = json.dumps(data,indent=2)
print(type(json_str))
print(json_str)
   
#    e) Écris aussi ce dict enrichi dans `catalogue_total.json`.
with open("catalogue_total.json","w",encoding="UTF-8") as f :
    json.dump(data,f,indent=2)