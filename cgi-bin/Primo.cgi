#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;

my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');

print "Content-Type: text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
<head>
    <title>Primi piatti - 2Forchette</title>
    <meta name=\"title\" content=\"2forchette - Primi piatti\"/>
    <meta name=\"description\" content=\"Sezione primi piatti del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
</head>
<body>
<div><a class=\"salta-main\" href=\".lista-menu\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
      <div id=\"banner\"><h1><a href=\"../index.html\">2FORCHETTE</a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>
          <a href=\"cercaricetta.cgi\">CERCA RICETTA</a>
          <a href=\"contatti.cgi\">CONTATTACI</a>
        </div>
      </div>
      <div class=\"allinea\"></div>
            <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
      Primi piatti
      </p>
    </div>
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
    <div class=\"main\">
    <h2>Primi piatti</h2>

    <div class=\"box-img\"><img src=\"../images/amatriciana.jpg\" alt=\"immagine che descrive spaghetti all'amatriciana\"/></div>
    <div>
        <p>

Fiore all’occhiello della cucina italiana, i primi piatti sono indiscussi protagonisti di ogni tipo di menù. Si sposano con qualsiasi ingrediente e possono essere realizzati con pasta, riso e condimenti a base di carne, pesce, uova o verdure. Ogni tipo di pasta ha caratteristiche ben precise e deve essere condita in modo appropriato. La pasta fresca all’uovo, come le tagliatelle, è ideale da condire con sughi elaborati a base di carne, le orecchiette si sposano perfettamente con le cime di rapa, alcuni primi piatti sono gustosi se conditi con vari tipi di sughi “a crudo”, come il pesto. Non mancano poi timballi di pasta al forno, gustosi risotti o arancini di riso.
</p>
    </div>
    <div class=\"allinea\"></div>

    </div>

      <div class=\"contenitore\">
        <div class=\"blocco2\">
          <ul class=\"lista-menu\">";

my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @ricette = $doc->findnodes("/ricetteDB/ricetta[categoria='Primo']");

foreach my $recipe (@ricette)
{
    my $allowed=$recipe->getAttribute('accepted');
	if($allowed=="1")
  	{
		my $nome = $recipe->findvalue('nomePiatto');
	  	my $id = $recipe->getAttribute('IDCode');
	 	my $img = $recipe->findvalue('imgPiatto');
  		print "
      		<li>
       			<a href=\"page_template.cgi?id=$id\">$nome</a>
       			<a href=\"page_template.cgi?id=$id\"><div class=\"box-img\"><img src=\"../images/$img\" alt=\"immagine che descrive $nome\"/></div></a>
     		</li>";
	}
}

  print "</ul></div></div>
    <div class=\"allinea\"></div>
</div>";

    if($auth eq "amministratoreautenticato")
{
	#footer con admin loggato
	print"<!--==============================footer=================================-->
<div id=\"footer\">
    <div class=\"main\">
          <div id=\"inline\">
          <p>
            <span>2Forchette</span> - copyright 2016 CARLO E LUCA produzione riservata - P.IVA 0838456799
           </p>
      <p>
      <a href=\"http://validator.w3.org/check?uri=referer\"><img
      src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0 Strict\"/></a>
        <a href=\"http://jigsaw.w3.org/css-validator/check/referer\">
        <img src=\"http://jigsaw.w3.org/css-validator/images/vcss\"
            alt=\"CSS Valido!\"/></a>
        <a href=\"http://jigsaw.w3.org/css-validator/check/referer\">
        <img src=\"http://jigsaw.w3.org/css-validator/images/vcss-blue\"
        alt=\"CSS Valido!\"/></a>
          </p>
             <p>
          ACCESSO EFFETTUTATO COME ADMIN:
          <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">logout</span></button></a>
          </p>
          </div>
    </div>
  </div>
</body>
</html>";
}
else
{
    #footer senza admin loggato
    print"
<!--==============================footer=================================-->
<div id=\"footer\">
    <div class=\"main\">
          <div id=\"inline\">

          <p>
            <span>2Forchette</span> - copyright 2016 CARLOeLUCA produzione riservata - P.IVA 0838456799
           </p>
      <p>
      <a href=\"http://validator.w3.org/check?uri=referer\"><img
      src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0 Strict\"/></a>

        <a href=\"http://jigsaw.w3.org/css-validator/check/referer\">
        <img src=\"http://jigsaw.w3.org/css-validator/images/vcss\"
            alt=\"CSS Valido!\"/></a>

        <a href=\"http://jigsaw.w3.org/css-validator/check/referer\">
        <img src=\"http://jigsaw.w3.org/css-validator/images/vcss-blue\"
        alt=\"CSS Valido!\"/></a>
          </p>
          </div>
    </div>
  </div>
</body>
</html>";
}

#Last update by Luca 31/05/2016
#bug fix generale
