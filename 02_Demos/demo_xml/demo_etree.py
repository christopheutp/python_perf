import xml.etree.ElementTree as ET

# Charger le document XML en mémoire
tree = ET.parse("utilisateurs.xml")
root = tree.getroot() # <utilisateurs>

# Parcourir chaque utilisateur sous la racine
for utilisateur in root.findall("utilisateur"):
    # .findtext() reupere le texte de l'element , "" par défaut si absent
    nom = (utilisateur.findtext("nom","")or "").strip()
    age = (utilisateur.findtext("age","")or "").strip()
    ville = (utilisateur.findtext("ville","")or "").strip()

    print(f"Nom : {nom}, age : {age}, ville {ville}")