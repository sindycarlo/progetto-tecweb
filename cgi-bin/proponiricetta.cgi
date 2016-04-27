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
      <div id="banner"><h1><a href="index.html">2FORCHETTE</a></h1></div>
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
         <p>tutti i campi sono da compilare, abbiamo bisogno di tutte le informazioni sulla tua ricetta.</p>
         <p>SI E' SCOLLEGATO IL CSS E NON CAPISCO PERCHE'</p>
         <!--da qualche parte precisare che gli ingredienti vanno inseriti uno a uno e poi si deve andare caporiga-->
         </div>
    <div class="allinea"></div>
  <div class="box-contact">
    <h1>Inviaci la tua ricetta</h1>
    <form id="contact-form" action="handle_proposta.cgi" method="post">
      <div id="fieldset"> <!--ti scrivo le cose da rivedere sul css: qua fieldset comprende tutto,
							ma perchè non hai usato il classico tag <fieldset>? -->
        <div class="colonna1"> <!--anche colonna1 comprende tutto!! da eliminare o questo o fieldset
									altrimenti viene interpretato facilmente come un residuo di copiatura
									anche "colonna1" non capisco il senso del nome
									non credo sia necessario, va integrato in fieldset-->
          <div> <!-- qua c'è un div senza classe e anche dopo ne usi, come mai? (non ricordo la sintassi esatta magari sbaglio io)-->
            <div class="form-txt">Nome piatto </div>
            <label>
              <input type="text" name="n_piatto" title="inserisci il nome del tuo piatto"/>
             </label>
          </div>
          <div>
            <div class="form-txt">Autore </div>
            <label>
              <input type="text" name="n_author" title="inserisci il nome dell'autore"/>
              </label>
          </div>
          <div>
            <div class="form-txt">Breve descrizione </div>
            <label class="message">
              <textarea rows="20" cols="60" name="n_desc">bla bla bla</textarea>
              </label>
          </div>
          <div class="Td">
            <div class="form-txt">Tempo di preparazione </div> <!-- credo sia questa la classe che si deve "sdoppiare" -->
            <label class="name">
              <input type="text" name="n_tempo" title="tempo di preparazione"/>
            </label>
          <div>
            <div class="form-txt">Difficoltà </div>
            <label class="name">
              <select  name="n_difficolta">	<!-- cambiato nome in n_difficolta, meglio non usare accenti -->
                <option value="1">1</option> <!-- questi devo ancora vedere come memorizzarli ma non dovrebbe essere difficile -->
                  <option value="2">2</option>
                  <option value="3">3</option>
              </select>
            </label>
          </div>
          </div>
          <div>
            <div class="form-txt">Numero persone </div>
            <label class="name">
              <input type="text" name="n_ingredienti" title="per quante persone"/>
             </label>
          </div>
          <div>
            <div class="form-txt">Carica un'immagine </div>
            <label class="name">
              <input type="file" name="n_immagine" title="immagine di presentazione"/>
             </label>
          </div>
              <div>
            <div class="form-txt">Categoria </div>
            <label class="name">
              <select  name="n_categoria">
                <option value="1">Primi</option>
                  <option value="2">Secondi</option>
                  <option value="3">Antipasti</option>
                  <option value="4">Dessert</option>
              </select>
            </label>
          </div>
          <div>
            <div class="form-txt">Ingredienti </div>
            <label class="name">
              <input type="text" name="n_ingredienti" title="quanti ingredienti"/>
             </label>
          </div>
           <div>
            <div class="form-txt">Procedimento </div>
            <label class="message">
              <textarea rows="20" cols="60" name="n_proc"> per prima cosa ... </textarea>
              </label>
          </div>
        <div class="buttons"><div class="button"><input type="submit"/></div><div class="button"><input type="reset"/></div>
        </div>
      </div>
        </div>
    </form>
  </div>
  </div>
  </div>

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

<!-- Last Update by Luca 26/04/2016 -->

EOF
