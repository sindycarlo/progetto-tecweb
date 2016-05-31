#!/usr/bin/perl -w


use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;
use HTML::Parser;
use HTML::Entities;


# recupero dal file commenti.xml i dati dei commenti.
my $file = "../data/commenti_ricetta.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

# controllo se la sessione esiste gia
my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');


if ($auth ne "amministratoreautenticato")
{
# stampo la pagina
print "Content-type:text/html\n\n";


print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Contattaci</title>
  <meta name=\"title\" content=\"2forchette - Contatti\"/>
    <meta name=\"description\" content=\"Sezione contatti del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"4forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
    <script type=\"text/javascript\" src=\"../js/valida_commento.js\"></script>
</head>
<body>
<div><a class=\"salta-main\" href=\"#contact-form\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
     <div id=\"banner\"><h1><a href=\"../index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>          
          <a class=\"active\">CONTATTACI</a>
             <form id=\"tfsearch\" method=\"get\" action=\"cercaricetta.cgi\">
						<input type=\"text\" class=\"tftextinput\" name=\"search_parameter\" size=\"30\" maxlength=\"30\">
						<input type=\"submit\" value=\"Cerca\" class=\"tfbutton\">
					</form>
        </div>
      </div>
      <div class=\"allinea\"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
      Contattaci
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
  <div class=\"main\">
  <div class=\"commenti\">
  <h2>Commenti:</h2>
";

# estrazione dei commenti
my @commenti = $doc->findnodes("/commenti/commento");

# stampa dei commenti
foreach my $commento (@commenti){
	my $user = decode_entities($commento->findvalue('user'));
	my $datac = $commento->findvalue('datacommento');
	my $testo = decode_entities($commento->findvalue('testo'));
        my $id = $commento->getAttribute('id');
	print "
				<span>Commento di : <strong>$user</strong></span>
				<span >Scritto il : <strong>$datac</strong></span>
				<p>$testo</p>";
	
}


print"</div><h2>Modulo commento</h2>
    <div class=\"info\">
    <span>Sezione dedicata ai commenti. Potete lasciare un commento.</span></div>
    <div class=\"box-contact\">
    <form id=\"contact-form\" action=\"inserisci_commento.cgi\" method=\"post\" onsubmit=\"return valida_commento()\">
    <span><p id=\"err_commento\"></p></span>
      <div id=\"fieldset\">

            <div class=\"form-txt\">Il tuo nome </div>
            <label>
              <input type=\"text\" name=\"user\" id=\"user\" title=\"inserisci il tuo nome qui\"/>
             </label>

		 <div class=\"form-txt\">Inserisci un commento </div>
            <label class=\"message\">
              <textarea name=\"commento\" id=\"form_commento\" rows=\"20\" cols=\"60\"></textarea>
              </label>

     <div class=\"allinea\"></div>
          
        
        <div class=\"buttons\"><div class=\"button\"><input type=\"submit\" value=\"Submit\"/></div><div class=\"button\"><input type=\"reset\" value=\"reset\"/></div></div>
        </div>
        
    </form>
    </div>
      </div>
    
  </div>
<!--==============================footer=================================-->
<div id=\"footer\">
	  <div class=\"main\">
	  <div class=\"informazioni\">
	  <h3>Per ulteriori informazioni:</h3>
	   	<p>Mail: lucalessio\@gmail.com</p>
		<p>Mail: sindycarlo\@gmail.com</p>
   		<p>3347421208 (Sindico Carlo)</p>
	  </div>
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
          </div>
	  </div>
	</div>
</body>
</html>
";
}

if($auth eq "amministratoreautenticato")
{
	# stampo la pagina
print "Content-type:text/html\n\n";


print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Contattaci</title>
  <meta name=\"title\" content=\"2forchette - Contatti\"/>
    <meta name=\"description\" content=\"Sezione contatti del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"4forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
    <script type=\"text/javascript\" src=\"../js/valida_commento.js\"></script>
</head>
<body>
<div><a class=\"salta-main\" href=\"#contact-form\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
     <div id=\"banner\"><h1><a href=\"../index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>          
          <a class=\"active\">CONTATTACI</a>
             <form id=\"tfsearch\" method=\"get\" action=\"cercaricetta.cgi\">
						<input type=\"text\" class=\"tftextinput\" name=\"search_parameter\" size=\"30\" maxlength=\"30\">
						<input type=\"submit\" value=\"Cerca\" class=\"tfbutton\">
					</form>
        </div>
      </div>
      <div class=\"allinea\"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
      Contattaci
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
  <div class=\"main\">
  <div class=\"commenti\">
  <h2>Commenti:</h2>
";

# estrazione dei commenti
my @commenti = $doc->findnodes("/commenti/commento");

# stampa dei commenti
foreach my $commento (@commenti){
	my $user = decode_entities($commento->findvalue('user'));
	my $datac = $commento->findvalue('datacommento');
	my $testo = decode_entities($commento->findvalue('testo'));
        my $id = $commento->getAttribute('id');
	print "
				<span>Commento di : <strong>$user</strong></span>
				<span >Scritto il : <strong>$datac</strong></span>
				<p>$testo</p>";
	
}


print"</div><h2>Modulo commento</h2>
    <div class=\"info\">
    <span>Sezione dedicata ai commenti. Potete lasciare un commento.</span></div>
    <div class=\"box-contact\">
    <form id=\"contact-form\" action=\"inserisci_commento.cgi\" method=\"post\" onsubmit=\"return valida_commento()\">
    <span><p id=\"err_commento\"></p></span>
      <div id=\"fieldset\">

            <div class=\"form-txt\">Il tuo nome </div>
            <label>
              <input type=\"text\" name=\"user\" id=\"user\" title=\"inserisci il tuo nome qui\"/>
             </label>

		 <div class=\"form-txt\">Inserisci un commento </div>
            <label class=\"message\">
              <textarea name=\"commento\" id=\"form_commento\" rows=\"20\" cols=\"60\"></textarea>
              </label>

     <div class=\"allinea\"></div>
          
        
        <div class=\"buttons\"><div class=\"button\"><input type=\"submit\" value=\"Submit\"/></div><div class=\"button\"><input type=\"reset\" value=\"reset\"/></div></div>
        </div>
        
    </form>
    </div>
      </div>
    
  </div>
<!--==============================footer=================================-->
<div id=\"footer\">
	  <div class=\"main\">
	  <div class=\"informazioni\">
	  <h3>Per ulteriori informazioni:</h3>
	   	<p>Mail: lucalessio\@gmail.com</p>
		<p>Mail: sindycarlo\@gmail.com</p>
   		<p>3347421208 (Sindico Carlo)</p>
	  </div>
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
</html>
";
}
