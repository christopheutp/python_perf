from lxml import etree

source_doc = etree.parse("source.xml")
xslt_doc   = etree.parse("style.xsl")
transformer = etree.XSLT(xslt_doc)
result = transformer(source_doc)


print(result)


with open("result.xml", "wb") as f:
    f.write(etree.tostring(
        result,                       
        pretty_print=True,
        xml_declaration=True,
        encoding="UTF-8"
    ))
