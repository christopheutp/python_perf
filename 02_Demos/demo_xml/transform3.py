from lxml import etree

source_doc = etree.parse("source.xml")
xslt_doc   = etree.parse("style_html.xsl")
transform  = etree.XSLT(xslt_doc)
result     = transform(source_doc)

# Écrire un fichier HTML prêt à ouvrir dans le navigateur
with open("result.html", "wb") as f:
    f.write(etree.tostring(result, pretty_print=True, method="html", encoding="UTF-8"))

print("OK -> result.html")
