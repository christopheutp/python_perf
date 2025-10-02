<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <!-- On demande une sortie HTML -->
  <xsl:output method="html" indent="yes" encoding="UTF-8"/>

  <!-- Point d'entrée : racine <persons> -->
  <xsl:template match="/persons">
    <html>
      <head>
        <meta charset="UTF-8"/>
        <title>Liste des personnes</title>
      </head>
      <body>
        <h1>Liste des personnes</h1>
        <ul>
          <!-- Pour chaque <person>, on appelle le template ci-dessous -->
          <xsl:apply-templates select="person"/>
        </ul>
      </body>
    </html>
  </xsl:template>

  <!-- Rendu d'une personne -->
  <xsl:template match="person">
    <li>
      <strong><xsl:value-of select="name"/></strong>
      (<em><xsl:value-of select="family-name"/></em>)
      — username: <xsl:value-of select="@username"/>
    </li>
  </xsl:template>
</xsl:stylesheet>
