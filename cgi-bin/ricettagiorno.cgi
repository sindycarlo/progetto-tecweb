#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;

# leggo l'id da get
my $cgi = new CGI;
my $id = $cgi->param('id');

my $file ="../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);



my $ric = $doc->findnodes("/ricetteDB/ricetta")->get_node(1);

my $titolo=$ric->findvalue('nomePiatto');
my $autore=$ric->findvalue('autore');
my $descrizione=$ric->findvalue('descrizione');
my $imgpiatto=$ric->findvalue('imgPiatto');
my $quantepers=$ric->findvalue('quantePersone');
my $procedimento=$ric->findvalue('procedimento');
my $diff=$ric->findvalue('difficolta');
my $cat=$ric->findvalue('categoria');
my $tempo=$ric->findvalue('tempoPreparazione');


my @nodes =$doc->findnodes("/ricetteDB/ricetta[\@\IDCode = 1]/ingredienti/ingr");

print "Content-Type: text/html\n\n";



print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
    <title>$titolo - 2Forchette.it</title>
    <meta name=\"title\" content=\"2forchette - $titolo\"/>
    <meta name=\"description\" content=\"$titolo\"/>
    <meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
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
      <div id=\"banner\"><h1><a href=\"../index.html\">2FORCHETTE</a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a  href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>
          <a class=\"active\">CERCA RICETTA</a>
          <a href=\"../contatti.html\">CONTATTACI</a>
        </div>
      </div>
      <div class=\"allinea\"></div>
        <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
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

foreach my $node (@nodes)
{
      
  

  print "
  
      
     <li>
     <p>$node</p> 
     </li>
      
   ";
}        


  print  "</ul>
    </div>
    <div class=\"blocco2\">  
  <span>Autore: $autore</span> <span>Categoria: $cat</span>
<p>$descrizione</p>
    <div class=\"allinea\"></div>
      <div class=\"box-img\"><img src=\"../images/$imgpiatto\" alt=\"immagine che descrive un $titolo\"/></div>
      <h2>PREPARAZIONE</h2>
      <div>
  <span>Tempo di preparazione: $tempo minuti</span> <span>Difficolta': $diff</span>
    <p>$procedimento</p>
     </div>
    </div>
    <div class=\"allinea\"></div>
  </div>
</div>

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
</html>
";

#last update by Carlo 16/05/2016
