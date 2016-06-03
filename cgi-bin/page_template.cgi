#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use HTML::Entities;
use utf8;
use URI;

require ('funzioni.pl');

my $cgi = new CGI;
my $id = $cgi->param('id');

# controllo se la sessione esiste gia
my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');

my $file ="../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);

my $ric = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $id]")->get_node(1);

my $titolo=$ric->findvalue('nomePiatto');
my $autore=$ric->findvalue('autore');
my $descrizione=$ric->findvalue('descrizione');
my $imgpiatto=$ric->findvalue('imgPiatto');
my $quantepers=$ric->findvalue('quantePersone');
my $procedimento=$ric->findvalue('procedimento');
my $diff=$ric->findvalue('difficolta');
my $cat=$ric->findvalue('categoria');
my $tempo=$ric->findvalue('tempoPreparazione');

decode_entities($titolo);
decode_entities($autore);
decode_entities($descrizione);
decode_entities($quantepers);
decode_entities($procedimento);
decode_entities($tempo);


my @ingredients =$doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $id]/ingredienti/ingr/text()");


print "Content-Type: text/html\n\n";

print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
    <title>$titolo - 2Forchette.it</title>
    <meta name=\"title\" content=\"2forchette - $titolo\"/>
    <meta name=\"description\" content=\"$titolo\"/>
    <meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo, $titolo, $cat\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
</head>
<body>
<div><a class=\"salta-main\" href=\".list\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
      <div id=\"banner\"><h1><a href=\"menu.cgi\">2FORCHETTE</a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a  href=\"menu.cgi\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>
          <a href=\"contatti.cgi\">CONTATTACI</a>
          <form id=\"tfsearch\" method=\"get\" action=\"cercaricetta.cgi\">
            <div>
            <input type=\"text\" class=\"tftextinput\" name=\"search_parameter\" size=\"30\" maxlength=\"30\"/>
            <input type=\"submit\" value=\"Cerca\" class=\"tfbutton\"/>
            </div>
          </form>
        </div>
      </div>
      <div class=\"allinea\"></div>
        <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
      <a href=\"$cat.cgi\">$cat</a><span>&gt;</span>
      $titolo
      </p>
    </div>
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
  <div class=\"contenitore\">
        <h1>$titolo</h1>
    <div class=\"side-bar\">
      <h1>INGREDIENTI</h1>
      <div id=\"num-pers\">(per $quantepers persone)</div>
      <ul class=\"list\">";

foreach my $singleing (@ingredients)
{
	print "	
	<li>
		<p>$singleing</p> 
    </li>
	";
}        

  print  "</ul>
    </div>
    <div class=\"blocco2\">  
	<p><strong>Autore:</strong> $autore</p> <p><strong>Categoria:</strong> $cat</p>
<p>$descrizione</p>
    <div class=\"allinea\"></div>
      <div class=\"box-img\"><img src=\"../images/$imgpiatto\" alt=\"immagine che rappresenta $titolo\"/></div>
      <h2>PREPARAZIONE</h2>
      <div>
	<p><strong>Tempo di preparazione:</strong> $tempo minuti</p> <p><strong>Difficolta':</strong> $diff</p>
  	<p>$procedimento</p>
     </div>
    </div>
    <div class=\"allinea\"></div>
  </div>
</div>";


if($auth eq "amministratoreautenticato")
{
	#footer con admin loggato
print "<!--==============================footer=================================-->
<div id=\"footer\">
<a href=\"#header\"><span id=\"up\">TORNA SU</span></a>
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
          <p>
          ACCESSO EFFETTUTATO COME ADMIN:
          <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">logout</span></button></a>
          </p>
          </div>
	  </div>
	</div>
</body>
</html>
";
}
else {
	#footer senza admin loggato
	print "<!--==============================footer=================================-->
<div id=\"footer\">
<a href=\"#header\"><span id=\"up\">TORNA SU</span></a>
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
</html>
";
}
#last update by Carlo 1/06/2016
#bug fix risolti
