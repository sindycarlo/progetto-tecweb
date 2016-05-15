#!/usr/bin/perl -w

#questa pagina è stata riciclata da secondipiatti.cgi, se vedi cose che non servono toglile pure

# librerie: servono tutte?
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;

# salto la parte delle sessioni/cookie/ecc per ora


# stampo la prima parte della pagina
print "Content-Type: text/html\n\n";


print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\">
<head>
    <title>Secondi piatti - 2Forchette</title>
    <meta name=\"title\" content=\"2forchette - Gestione ricette\"/>
    <meta name=\"description\" content=\"Sezione Gestione ricette del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
</head>
<body>
<div><a class=\"salta-main\" href=\"#footer\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
      <div id=\"banner\"><h1><a href=\"../index.html\"> <span>2FORCHETTE</span></a></h1></div>
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
      <a href=\"amministratore_login.cgi\">Amministratore login</a><span>&gt;</span>
      <span xml:lang=\"en\">Console Amministratore</span>
      </p>
    </div>
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
    <div class=\"main\">
    <h2>Lato Amministrativo</h2>
		<p>Qui puoi vedere tutte le ricette attualmente presenti all'interno del sito. L'amministratore ha la possibilita' di rimuovere le ricette ritenute obsolete, aggiungere quelle proposte dagli utenti e regolare quali ricette saranno in evidenza nella home page.</p>
	<h3>Elenco ricette presenti</h3>";

my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @ricette = $doc->findnodes("/ricetteDB/ricetta");

foreach my $recipe (@ricette)
{
   my $allowed=$recipe->getAttribute('accepted');
  if($allowed=="1")
  {
    my $nome = $recipe->findvalue('nomePiatto');
    my $id = $recipe->getAttribute('IDCode');
    print "
        <li>
          <a href=\"page_template.cgi?id=$id\">$nome</a><a href=\"delete_ricetta.cgi?id=$id\"><input type=\"submit\" value=\"ELIMINA\"</input></a>
       </li>
    ";
  }
}

print  "<h3>Ricette proposte</h3>";

foreach my $recipe (@ricette)
{
   my $allowed=$recipe->getAttribute('accepted');
  if($allowed=="0")
  {
    my $nome = $recipe->findvalue('nomePiatto');
    my $id = $recipe->getAttribute('IDCode');
    print "
        <li>
          <a href=\"page_template.cgi?id=$id\">$nome</a> <a href=\"accept_ricetta.cgi?id=$id\"><input type=\"submit\" value=\"ACCETTA\"</input></a> <a href=\"delete_ricetta.cgi?id=$id\"><input type=\"submit\" value=\"RIFIUTA\"</input></a>
       </li>
    ";
  }
}


print "<h3>Commenti</h3>";
my $file = "../data/commenti_ricetta.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @commento = $doc->findnodes("/commenti/commento");

foreach my $comm (@commento)
{

    my $nomeuser = $comm->findvalue('user');
    my $id = $comm->getAttribute('id');
    print "
        <li>
          <a href=\"contatti.cgi\"><span>Autore del commento: $nomeuser</a> <a href=\"delete_commento.cgi?id=$id\"><input type=\"submit\" value=\"ELIMINA COMMENTO\"</input></a>
       </li>
    ";
}


print "
  </div>
</div>

<!--==============================footer=================================-->
<div id=\"footer\">
    <div class=\"main\">
          <div id=\"inline\">

          <p>
            <span>2Forchette</span> -copyright 2016 CARLOeLUCA produzione riservata - P.IVA 0838456799
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
    <div class=\"allinea\"></div>
    </div>
  </div>
</body>
</html>";
#Last update 15/05/2016 by Carlo
