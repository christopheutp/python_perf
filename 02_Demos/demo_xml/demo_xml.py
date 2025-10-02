import xml.sax


# Creer une classe qui va recevoir les evenements SAX
# Elle herite de ContentHandler (sui definit les methodes de callback que le parser appelera)
class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()

    # Appeler a chaque fois que le parser rencontre une balise ouvrante <...>
    def startElement(self, name, attrs):
        print(f"Element trouve : {name}")
        # si il y'a des attributs dans la balise <... attribut=value>
        if attrs:
            print(" Attributs :")
            for attr_name,attr_value in attrs.items():
                print(f" {attr_name} = {attr_value}")

    # Appeler quans de parser rencontre balise fermante </....>
    def endElement(self, name):
        print(f"Fin element : {name}")

    # Appeler quand le parler lit du texte entre les balises
    def characters(self, content):
        if content.strip():
            print(f" Contenu texte : {content}")

# Creer une instance du gestionnaire d'evenements
handler = XMLHandler()

# Creer un parser sax
parser = xml.sax.make_parser()

# Associer notre gestionnaire au parser
parser.setContentHandler(handler)

# lire notre fichier xml
with open("exemple.xml",'r') as xml_file:
    parser.parse(xml_file)