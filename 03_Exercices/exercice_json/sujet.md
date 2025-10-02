# Exercice

**But :** manipuler `dump/load` et `dumps/loads`.

1. Crée un dict Python nommé `catalogue` comme suit :

   ```python
   {
     "produits": [
       {"id": 1, "nom": "Stylo", "prix": 1.8},
       {"id": 2, "nom": "Cahier", "prix": 2.5},
       {"id": 3, "nom": "Sac",   "prix": 19.9}
     ]
   }
   ```
2. a) Sauvegarde ce dict dans un fichier `catalogue.json` (joli avec `indent=2`).
   b) Relis le fichier et calcule le **prix total** de tous les produits.
   c) Ajoute une clé `"total"` au dict rechargé avec ce montant.
   d) Convertis le dict enrichi en **chaîne JSON** et affiche-la.
   e) Écris aussi ce dict enrichi dans `catalogue_total.json`.