import os
from collections import Counter

print("contenu du repertoire courant")
print(os.listdir("."))

print("fichier ?")
print("demo.txt",os.path.isfile("demo.txt"))


taille = os.path.getsize("demo.txt")
print(taille)

# lire le contenu du fichier et compter combien de fois chaque caractere apparait
with open("demo.txt","r",encoding="utf-8") as f:
    contenu = f.read()
print("contenu du fichier :")
print(contenu)

compteur = Counter(contenu)
print("Compteur des caracteres dans mon contenu")
print(compteur)