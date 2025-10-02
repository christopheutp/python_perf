from lxml import etree


with open("livres.xml",'r',encoding="UTF-8") as reader:
    content = reader.read()
    source = etree.fromstring(content)
    transform = etree.parse("transform.xsl")
    transformer = etree.XSLT(transform)
    result = transformer(source)

with open("result.xml","w",encoding='UTF-8') as file:
    file.write(str(result))


print(result)