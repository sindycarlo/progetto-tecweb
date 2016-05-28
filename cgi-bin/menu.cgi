#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;
# controllo se la sessione esiste gia
my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');


if ($auth ne "amministratoreautenticato")
{print "Content-Type: text/html\n\n";

print"
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
	<head>
		<title>Home 2forchette</title>
		<meta name=\"title\" content=\"2forchette - Progetto di Tecnologie web\"/>
		<meta name=\"description\" content=\"Home page del sito 2forchette\"/>
		<meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico , Luca Alessio\"/>
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
		  <div id=\"banner\"><h1>2FORCHETTE</h1></div>
            <div class=\"header-menu\">
                <div id=\"nav\">
                    <a class=\"active\"><span xml:lang=\"en\">HOME</span></a>
                    <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>
                    <a href=\"contatti.cgi\">CONTATTACI</a>
                    <form id=\"search_bar\" method=\"get\" action=\"cercaricetta.cgi\">
						<input type=\"text\" name=\"search_parameter\" size=\"30\" maxlength=\"30\">
						<input type=\"submit\" value=\"Cerca\">
					</form>
                </div>
            </div>

    </div>
		  <div class=\"allinea\"></div>
		  <div id='breadcrumb'>
		  	<p>Ti trovi in:
			<a><span  xml:lang=\"en\">Home</span></a></p>
		</div> 
		  <div class=\"allinea\"></div>
		   
		</div>
	  </div>
	<!--==============================content=================================-->
	<div id=\"content\">
	  <div class=\"contenitore\">
		<div class=\"blocco2\">
		  ";

my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @ricette = $doc->findnodes("/ricetteDB/ricetta");

if(scalar(@ricette)>=3) #mostro ricette casuali solo se ne ho abbastanza
{
	my @allid;
	#prima rempio un array con tutte le id
	foreach my $recipe (@ricette)
	{
		my $allowed = $recipe->getAttribute('accepted');
		if($allowed != "0")
		{
			my $id = $recipe->getAttribute('IDCode');
			push(@allid,$id);
		}
	}
	#poi ne estraggo tre casuali
	my $rand1 = $allid[rand @allid];
	my $ric1 = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $rand1]")->get_node(1);
	my $titolo1=$ric1->findvalue('nomePiatto');
	my $img1=$ric1->findvalue('imgPiatto');
	my $rand2 = $allid[rand @allid];
	my $ric2 = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $rand2]")->get_node(1);
	my $titolo2=$ric2->findvalue('nomePiatto');
	my $img2=$ric2->findvalue('imgPiatto');
	my $rand3 = $allid[rand @allid];
	my $ric3 = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $rand3]")->get_node(1);
	my $titolo3=$ric3->findvalue('nomePiatto');
	my $img3=$ric3->findvalue('imgPiatto');

	print"
		<ul class=\"lista-menu\">			
		<li>
			<a href=\"page_template.cgi?id=$rand1\">$titolo1</a>
			<div class=\"box-img\"><img src=\"../images/$img1\" alt=\"immagine che descrive $titolo1\"/></div>
		</li>
		<li>
			<a href=\"page_template.cgi?id=$rand2\">$titolo2</a>
			<div class=\"box-img\"><img src=\"../images/$img2\" alt=\"immagine che descrive $titolo2\"/></div>
		</li>
		<li>
			<a href=\"page_template.cgi?id=$rand3\">$titolo3</a>
			<div class=\"box-img\"><img src=\"../images/$img3\" alt=\"immagine che descrive $titolo3\"/></div>
		</li>
		</ul>
			
	    ";
}
#else niente, ho troppe poche ricette, non le mostro nella home
		
		  print"
		</div>
	  </div>
	  <div class=\"allinea\"></div>
	  <div class=\"contenitore\">
		<div class=\"blocco1\">
		  <h2><span>PRIMI</span> PIATTI </h2>
		  <div  class=\"box-img\"><img src=\"../images/primopiatto.jpg\" alt=\"immagine che descrive risotto allo zafferano\"/></div> 
		  <a href=\"Primo.cgi\">Continua a leggere i primi</a>
		  <h2><span>ANTIPASTI</span>SALATI</h2>
		  <div  class=\"box-img\"><img src=\"../images/antipasti.jpg\" alt=\"immagine che descrive verdure grigliate\"/></div> 
		  <a href=\"Antipasti.cgi\">Continua a leggere gli antipasti</a></div>
		<div  class=\"blocco1\">
		  <h2><span>SECONDI</span>PIATTI</h2>
		  <div class=\"box-img\"><img src=\"../images/secondopiatto.jpg\" alt=\"immagine che descrive carne di manzo con patate\"/></div>
		  <a href=\"Secondi.cgi\">Continua a leggere i secondi</a>
		  <h2><span>DESSERT</span>DOLCI</h2>
		  <div  class=\"box-img\"><img src=\"../images/dessert.jpg\" alt=\"immagine che descrive crostata alla vaniglia con ciliege\"/></div>
		  <a href=\"Dessert.cgi\">Continua a leggere i dessert</a></div>
	  </div>
	  <div class=\"allinea\"></div>
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
          <p>
          <a href=\"amministratore_login.cgi\"><span xml:lang=\"en\">Admin Login</span></a>
          </p>
          </div>
	  </div>
	</div>
	</body>
</html>
<!-- Last Update by Luca 28/05/2016 -->"
}


if ($auth eq "amministratoreautenticato")
{
	print "Content-Type: text/html\n\n";

print"
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
	<head>
		<title>Home 2forchette</title>
		<meta name=\"title\" content=\"2forchette - Progetto di Tecnologie web\"/>
		<meta name=\"description\" content=\"Home page del sito 2forchette\"/>
		<meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico , Luca Alessio\"/>
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
		  <div id=\"banner\"><h1>2FORCHETTE</h1></div>
            <div class=\"header-menu\">
                <div id=\"nav\">
                    <a class=\"active\"><span xml:lang=\"en\">HOME</span></a>
                    <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>
                    <a href=\"contatti.cgi\">CONTATTACI</a>
                    <form id=\"search_bar\" method=\"get\" action=\"cercaricetta.cgi\">
						<input type=\"text\" name=\"search_parameter\" size=\"30\" maxlength=\"30\">
						<input type=\"submit\" value=\"Cerca\">
					</form>
                </div>
            </div>

    </div>
		  <div class=\"allinea\"></div>
		  <div id='breadcrumb'>
		  	<p>Ti trovi in:
			<a><span  xml:lang=\"en\">Home</span></a></p>
		</div> 
		  <div class=\"allinea\"></div>
		   
		</div>
	  </div>
	<!--==============================content=================================-->
	<div id=\"content\">
	  <div class=\"contenitore\">
		<div class=\"blocco2\">
		  ";

my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @ricette = $doc->findnodes("/ricetteDB/ricetta");

if(scalar(@ricette)>=3) #mostro ricette casuali solo se ne ho abbastanza
{
	my @allid;
	#prima rempio un array con tutte le id
	foreach my $recipe (@ricette)
	{
		my $allowed = $recipe->getAttribute('accepted');
		if($allowed != "0")
		{
			my $id = $recipe->getAttribute('IDCode');
			push(@allid,$id);
		}
	}
	#poi ne estraggo tre casuali
	my $rand1 = $allid[rand @allid];
	my $ric1 = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $rand1]")->get_node(1);
	my $titolo1=$ric1->findvalue('nomePiatto');
	my $img1=$ric1->findvalue('imgPiatto');
	my $rand2 = $allid[rand @allid];
	my $ric2 = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $rand2]")->get_node(1);
	my $titolo2=$ric2->findvalue('nomePiatto');
	my $img2=$ric2->findvalue('imgPiatto');
	my $rand3 = $allid[rand @allid];
	my $ric3 = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $rand3]")->get_node(1);
	my $titolo3=$ric3->findvalue('nomePiatto');
	my $img3=$ric3->findvalue('imgPiatto');

	print"
		<ul class=\"lista-menu\">			
		<li>
			<a href=\"page_template.cgi?id=$rand1\">$titolo1</a>
			<div class=\"box-img\"><img src=\"../images/$img1\" alt=\"immagine che descrive $titolo1\"/></div>
		</li>
		<li>
			<a href=\"page_template.cgi?id=$rand2\">$titolo2</a>
			<div class=\"box-img\"><img src=\"../images/$img2\" alt=\"immagine che descrive $titolo2\"/></div>
		</li>
		<li>
			<a href=\"page_template.cgi?id=$rand3\">$titolo3</a>
			<div class=\"box-img\"><img src=\"../images/$img3\" alt=\"immagine che descrive $titolo3\"/></div>
		</li>
		</ul>
			
	    ";
}
#else niente, ho troppe poche ricette, non le mostro nella home
		
		  print"
		</div>
	  </div>
	  <div class=\"allinea\"></div>
	  <div class=\"contenitore\">
		<div class=\"blocco1\">
		  <h2><span>PRIMI</span> PIATTI </h2>
		  <div  class=\"box-img\"><img src=\"../images/primopiatto.jpg\" alt=\"immagine che descrive risotto allo zafferano\"/></div> 
		  <a href=\"Primo.cgi\">Continua a leggere i primi</a>
		  <h2><span>ANTIPASTI</span>SALATI</h2>
		  <div  class=\"box-img\"><img src=\"../images/antipasti.jpg\" alt=\"immagine che descrive verdure grigliate\"/></div> 
		  <a href=\"Antipasti.cgi\">Continua a leggere gli antipasti</a></div>
		<div  class=\"blocco1\">
		  <h2><span>SECONDI</span>PIATTI</h2>
		  <div class=\"box-img\"><img src=\"../images/secondopiatto.jpg\" alt=\"immagine che descrive carne di manzo con patate\"/></div>
		  <a href=\"Secondi.cgi\">Continua a leggere i secondi</a>
		  <h2><span>DESSERT</span>DOLCI</h2>
		  <div  class=\"box-img\"><img src=\"../images/dessert.jpg\" alt=\"immagine che descrive crostata alla vaniglia con ciliege\"/></div>
		  <a href=\"Dessert.cgi\">Continua a leggere i dessert</a></div>
	  </div>
	  <div class=\"allinea\"></div>
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
          <p>
          <a href=\"amministratore_login.cgi\"><span xml:lang=\"en\">Admin Login</span></a>
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
<!-- Last Update by Luca 28/05/2016 -->"
	
}
