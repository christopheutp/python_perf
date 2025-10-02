from lxml import etree # bibliotheque tierce (pip install lxml)

# charger le document xml source
source_doc = etree.parse("source.xml")

# charger la feuille de style XSLT
xslt_doc = etree.parse("style.xsl")


# Creer un transformateur XSLT
transformer = etree.XSLT(xslt_doc)

# Appliquer la transformation
result = transformer(source_doc)

print(result)