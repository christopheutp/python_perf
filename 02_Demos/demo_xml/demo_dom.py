import xml.dom.minidom

# Charger le fichier xml entier en memoire sous forme d'abre DOM
dom_tree = xml.dom.minidom.parse("exemple.xml")

# Recuperent l'element root du document
root_element = dom_tree.documentElement
print(f"Element racine ; {root_element.tagName}")


# Parcourir les noeud enfant de root
for node in root_element.childNodes:
    # On verifie qu'il s'agit d'un element (pas du texte)
    if node.nodeType == node.ELEMENT_NODE:
        print("\nElement : ",node.tagName)

        # parcourir les attributs
        if node.hasAttributes():
            print(" Attributs ")
            for attr_name,attr_value in node.attributes.items():
                print(f" {attr_name} = {attr_value}")

        # Parcourir les enfants
        for child_node in node.childNodes:
            if child_node.nodeType == child_node.TEXT_NODE:
                contenu = child_node.data.strip()
                if contenu:
                    print(" Contenu : ",contenu)

# Exemple modif
first_child = root_element.firstChild
if first_child and first_child.nodeType == first_child.TEXT_NODE:
    first_child.data = "Nouveau contenue"

# Enregistrer le modif
with open("exemple2.xml","w",encoding="utf-8") as new_xml_file:
    dom_tree.writexml(new_xml_file)