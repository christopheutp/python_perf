<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <!-- Sortie en XML indentation active -->
    <xsl:output method="xml" indent="yes"/>

    <!-- Premier template quand on rencontre la balise persons -->
    <xsl:template match="/persons">
        <root>
            <!-- appliquer le template a chaque person -->
            <xsl:apply-templates select="person"/>
        </root>
    </xsl:template>

    <!-- template pour chaque person -->
    <xsl:template match="person">
        <!-- on crer un element name avec un attribut username -->
       <name username="{@username}">
        <!-- inserer la valeur de la balise name du xml source -->
        <xsl:value-of select="name"/>
        </name>
    </xsl:template>

</xsl:stylesheet>