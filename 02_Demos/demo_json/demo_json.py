import os, json  # Module standard pour le JSON

file_path = './file.json'
mon_dict = {'people': ['Albert', 'Martin', 'Louis'], 'mes Chiens': [1, 2, 4, 5]}

# -------------------------------------------------------------------
# Partie FICHIERS : json.dump() et json.load()
# -------------------------------------------------------------------
# - json.dump(obj, fp): sérialise un objet Python -> vers un FICHIER (écriture)
# - json.load(fp): désérialise depuis un FICHIER -> objet Python (lecture)

# Pour manipuler les JSON fichiers, on accède aux deux méthodes ci-dessous
if os.path.exists(file_path):
    file = open(file_path, 'r')
    # json.load() : FICHIER -> OBJET Python
    data = json.load(file)           
    file.close()
    print(data)
else:
    file = open(file_path, 'w')
    # json.dump() : OBJET Python -> FICHIER
    json.dump(mon_dict, file, indent=4)  
    file.close()

# -------------------------------------------------------------------
# Partie CHAINES : json.dumps() et json.loads()
# -------------------------------------------------------------------
# - json.dumps(obj): sérialise un objet Python -> CHAÎNE JSON (en mémoire)
# - json.loads(str): désérialise une CHAÎNE JSON -> objet Python

# Obtenir une chaîne JSON représentant l'objet en mémoire
json_str = json.dumps(mon_dict, indent=4)  
print(json_str)
print(type(json_str))

# Transformer une chaîne JSON en objet Python
data = json.loads(json_str)              
print(data)
print(type(data))
print(data['people'])
