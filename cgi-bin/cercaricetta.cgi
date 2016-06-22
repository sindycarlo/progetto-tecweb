#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use HTML::Entities;
use File::Copy;
use File::Basename; # serve per uploadare i file
use Time::localtime; # per conoscere la data corrente
use CGI::Pretty qw(:html3);
use POSIX;
use URI;
use utf8;
# controllo se la sessione esiste gia
my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');
my $cgi = CGI->new(); # create new CGI object

my $parametro = $cgi->param('search_parameter');
my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @ricette = $doc->findnodes("/ricetteDB/ricetta");




# stampo la pagina
print "Content-type:text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Cerca ricetta</title>
  <meta name=\"title\" content=\"2forchette - Cerca ricetta\"/>
    <meta name=\"description\" content=\"Sezione Cerca ricetta del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"shortcut icon\" href=\"../images/favicon.ico\" type=\"image/x-icon\"/>	
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
</head>
<body>
<div><a class=\"salta-main\" href=\"#footer\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
     <div id=\"banner\"><h1><a href=\"../index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
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
      Cerca ricetta
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
<div class=\"full\">
  <div class=\"main\">
    <h2>Risultati ricerca per \"$parametro\"</h2><div class=\"search-box\"><ul>";
    
my $empty = 0;

foreach my $recipe (@ricette)
{
	my $nome = $recipe->findvalue("nomePiatto");
	decode_entities($nome);
	$parametro=~ s/^\s+|\s+$//g;
	my $allowed = $recipe->getAttribute('accepted');
	if ( index(lc $nome, lc $parametro) != -1 and $allowed == "1") #cerco ricette che nel nome contengono il testo immesso dall'utente ma che sono anche state approvate dall'amministratore
	{
		my $id = $recipe->getAttribute('IDCode');
		print "<li><p><a href=\"page_template.cgi?id=$id\">$nome</a></p></li>";
		$empty = 1;
	}
}

if ($empty == 0)
{
	print"<li>Siamo spiacenti, nessuna ricetta presente nel sito soddisfa i criteri di ricerca :(</li>";
}

print"</ul></div></div></div>
</div>";


    if($auth eq "amministratoreautenticato")
{
	#footer con admin loggato
	print"<!--==============================footer=================================-->
<div id=\"footer\">
<a href=\"#header\"><span id=\"up\">TORNA SU</span></a>
    <div class=\"main\">
          <div id=\"inline\">
          <p>
            <span>2Forchette</span> - copyright 2016 CARLO E LUCA produzione riservata - P.IVA 0838456799
           </p>
    			 <p>
		 <img src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0 Strict\"/>

       	 <img src=\"http://jigsaw.w3.org/css-validator/images/vcss\" alt=\"CSS Valido!\"/>

       	 <img src=\"../images/valid_wcag_aaa.gif\" alt=\"Totally Valid WCAG 2.0 AAA\" />

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
<a href=\"#header\"><span id=\"up\">TORNA SU</span></a>
    <div class=\"main\">
          <div id=\"inline\">

          <p>
            <span>2Forchette</span> - copyright 2016 CARLO E LUCA produzione riservata - P.IVA 0838456799
           </p>
     	
     	<p>
		 <img src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0 Strict\"/>

       	 <img src=\"http://jigsaw.w3.org/css-validator/images/vcss\" alt=\"CSS Valido!\"/>

       	 <img src=\"../images/valid_wcag_aaa.gif\" alt=\"Totally Valid WCAG 2.0 AAA\" />

         </p>
          </div>
    </div>
  </div>
</body>
</html>";
}
#Last Update by Carlo 1/06/2016
#bug fix risolti

