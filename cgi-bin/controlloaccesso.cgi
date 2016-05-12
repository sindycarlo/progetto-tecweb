#!/usr/bin/perl -w

# file che controlla l'accesso amministratore
# carico le librerie
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;

# includo la mia libreria funzioni
require ('libreria_funzioni.pl');


# leggo i dati dal POST e li inserisco nell'hash DATI
my %DATI = &leggi_post();

if(!%DATI){
	print redirect("../index.html");
}

# creo e inizializzo le variabili con i dati del post
my $username = $DATI{'username'};
my $password = $DATI{'password'};
my $auth="amministratoreautenticato";
my $file = "../data/amministratore.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

# estrazione radice
my $root = $doc->getDocumentElement;

# array degli elementi username
my @user = $root->getElementsByTagName('username');


	# prelevo il valore della password dal file xml dal nodo con username = a quella passata dal form
	my $pwd = $doc->findvalue("amministratori/amministratore[username=\"$username\"]/password");
	# confronto le password
	if ($pwd ne $password)#se le password non coincidono;
	{
		print "Content-Type: text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Admin Login</title>
  <meta name=\"title\" content=\"2forchette - Progetto di Tecnlogie web\"/>
    <meta name=\"description\" content=\"Login Area amministrativa del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <!--css-->
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
    

</head>
<body>
<div><a class=\"salta-main\" href=\"#footer\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
      <div id=\"banner\"><h1><a href=\"../index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"allinea\"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in:
      <a><span>Errore</span></a>
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
  <div class=\"main\">
    <h2>Login</h2>
    <div class=\"box-contact\">
    <span lang=\"en\">Password</span> sbagliata o vuota, riprova di nuovo <a href=\"./amministratore.cgi\"><span lang=\"en\">Login</span></a>
    </div>
      </div>
    
  </div>
<!--==============================footer=================================-->
<div id=\"footer\">
    <div class=\"main\">
          <div id=\"inline\">

          <p>             
            <span>2Forchette</span> - Via Molinari 63, 33170, Milano- p. iva 02768250152
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
</body>";

}
