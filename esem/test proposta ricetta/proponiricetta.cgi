#
# PAGINA DI PROVA
# n.b. questa pagina fa poche cose ma l'importante è che le faccia giuste, è un solo test e non è la pagina finale ovviamente 
# quello che deve fare è prendere dei dati dal form e salvarli nell'xml 
# per controllare se va bene basta andare a vedere se l'xml è stato aggiornato correttamente
# c'è ancora della pulizia sul codice css da fare secondo me ma ne discutiamo di persona
# tipo allinea, active, le classi dei form, tutte da rivedere e ti spiegherò perchè
#

#!/usr/bin/perl -w

# file che controlla l'amministrazione del sito
# carico le librerie
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
# includo la mia libreria funzioni
require ('libreria_funzioni.pl');

my $session = CGI::Session->load();

my $auth;
if(!($session->is_expired) || !($session->is_empty)){
	# ricavo l'autenticazione
        $auth = $session->param('auth');
}

# recupero dal file commenti.xml i dati dei commenti.
my $file = "../data/cose.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);


# stampo la pagina
print "Content-type:text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it"> 
<head>
    <title>Proponi una ricetta</title>
    <meta name="title" content="4forchette - Progetto di Tecnlogie web"/>
    <meta name="description" content="Sezione proponi una ricetta del sito 4forchette"/>
    <meta name="keywords" content="4forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo"/>
    <meta name="language" content="italian it"/>
    <meta name="author" content="Carlo Sindico ,Luca Alessio"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <!--css-->
    <link rel="stylesheet" href="css/style.css" type="text/css" media="screen"/>
    <link rel="stylesheet" href="css/print.css" type="text/css" media="print"/>
    
</head>
<body>
<div><a class="salta-main" href="#footer"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id="header">
  <div class="main">
    <div class="intestazione">
      <div id="banner"><h1><a href="index.html"> <span xml:lang="en">2FORCHETTE</span> </a></h1></div>
      <div class="header-menu">
        <div id="nav">
          <a href="index.html"><span>HOME</span></a>
          <a class="active">PROPONI UNA RICETTA</a>
          <a href="ricettagiorno.html">RICETTA DEL GIORNO</a>
          <a href="contatti.html">CONTATTACI</a>
        </div>
      </div>
      <div class="allinea"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href="index.html"><span xml:lang="en">Home</span></a><span>&gt;</span>
      Proponi una ricetta
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id="content">
  <div class="main">
    <h1>Informazioni</h1>
         <div class="info"><p>Se vuoi diventare anche tu uno chef inviaci la tua ricetta e noi la valuteremo. Tra tutte le ricette che ci saranno inviate sceglieremo la migliore. Puoi essere anche tu il vincitore!</p>
         <p>Invia un'email. Tutti i campi contrassegnati da asterisco (*) sono obbligatori.</p></div>
    <div class="allinea"></div>
  
<form id="form_new_thing" method="post" action="../cgi-bin/handle_proposta.cgi">
	<p><span> inserisci valore campo stuff</span></p>
	<p><input type="text" name="new_stuff" id="new_stuff"/></p>
	<p><span> inserisci valore campo blabla</span></p>
	<p><input type="text" name="new_bla" id="new_bla"/></p>
	<p><span> inserisci valore campo contenuto</span></p>
	<p><input type="text" name="new_contenuto" id="new_contenuto"/></p>
	<p><input type="submit" value="Submit"></p>
</form>';
<!--==============================footer=================================-->
<div id="footer">
	  <div class="main">
          <div id="inline">

         	<p>             
            <span>4Forchette</span> - Via Molinari 63, 33170, Milano- p. iva 02768250152
       	   </p>
			<p> 
    	<a href="http://validator.w3.org/check?uri=referer"><img
     	src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict"/></a>

        <a href="http://jigsaw.w3.org/css-validator/check/referer">
      	<img src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="CSS Valido!"/></a>
        						
        <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="CSS Valido!"/></a>				
          </p>
          </div>
		<div class="allinea"></div>
	  </div>
	</div>
</body>
</html>

EOF
my $x=1;	
