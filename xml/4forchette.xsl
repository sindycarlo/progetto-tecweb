<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<body>
				<h2>ELENCO RICETTE TEST</h2>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>
	
	<xsl:template match="ricetteDB">
		<p><xsl:apply-templates select="ricetta"/></p>
	</xsl:template>
	
	<xsl:template match="ricetta">
		<xsl:apply-templates select="nomePiatto"/>
		<xsl:apply-templates select="autore"/>
		<xsl:apply-templates select="descrizione"/>
		<xsl:apply-templates select="imgPiatto"/>
		<xsl:apply-templates select="difficolta"/>		
		<xsl:apply-templates select="valutazioneUtenti"/>
		<xsl:apply-templates select="quantePersone"/>
		<xsl:apply-templates select="ingredienti"/>
		<xsl:apply-templates select="tempoPreparazione"/>
		<xsl:apply-templates select="tempoCottura"/>
		<xsl:apply-templates select="procedimento"/>		
		<!-- <xsl:apply-templates select="commenti"/> -->
	</xsl:template>
	<!-- aggiungere qualche <br/> dove serve -->
	<xsl:template match="nomePiatto">
		<h3><xsl:value-of select="."/></h3>
	</xsl:template>
	
	<xsl:template match="autore">
		 Autore: <span><xsl:value-of select="."/></span>
	</xsl:template>
	
	<xsl:template match="descrizione">
		 <p><xsl:value-of select="."/></p>
	</xsl:template>
	
	<xsl:template match="imgPiatto">
		 <br/><span><xsl:value-of select="."/></span><br/><br/> <!-- fare prove sulla visualizzazione -->
	</xsl:template>
	
	<xsl:template match="difficolta">
		 <span>Difficoltà: <xsl:value-of select="."/>/3</span><br/>
	</xsl:template>

	<xsl:template match="valutazioneUtenti">
		 <span>Valutazione utenti: <xsl:value-of select="."/>/5</span><br/>
	</xsl:template>
	
	<xsl:template match="quantePersone">
		 <span>Ingredienti per <xsl:value-of select="."/> persone</span><br/>
	</xsl:template>
	
	<xsl:template match="ingredienti">
		 <ul><xsl:apply-templates select="ingr"/></ul>
	</xsl:template>
	
	<xsl:template match="ingr">
		 <li><span><xsl:value-of select="."/></span></li>
	</xsl:template>
	
	<xsl:template match="tempoPreparazione">
		 Tempo di preparazione: <span><xsl:value-of select="."/></span><br/>
	</xsl:template>
	
	<xsl:template match="tempoCottura">
		 Tempo di cottura: <span><xsl:value-of select="."/></span><br/>
	</xsl:template>
	
	<xsl:template match="procedimento">
		 <h4>Procedimento</h4><p><xsl:value-of select="."/></p>
	</xsl:template>
	
	<!--
	<xsl:template match="commenti">
		 Autore: <span><xsl:value-of select="."/></span><br/>
	</xsl:template>   -->
</xsl:stylesheet>
