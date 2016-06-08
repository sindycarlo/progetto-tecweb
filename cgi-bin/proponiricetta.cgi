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

my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');

print "Content-type:text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it"> 
<head>
    <title>Proponi una ricetta - 2Forchette</title>
    <meta name="title" content="2Forchette - Proponi una ricetta"/>
    <meta name="description" content="Sezione proponi una ricetta del sito 2forchette"/>
    <meta name="keywords" content="2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo"/>
    <meta name="language" content="italian it"/>
    <meta name="author" content="Carlo Sindico ,Luca Alessio"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta http-equiv="Content-Script-Type" content="text/javascript"/>
    <link rel="stylesheet" href="../css/style.css" type="text/css" media="screen"/>
    <link rel="stylesheet" href="../css/print.css" type="text/css" media="print"/>
    <script type="text/javascript" src="../js/proponi_ricetta.js"></script>
</head>

<body>
<div><a class="salta-main" href="#contact-form"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id="header">
  <div class="main">
    <div class="intestazione">
      <div id="banner"><h1><a href="../index.html">2FORCHETTE</a></h1></div>
      <div class="header-menu" id="nav">
        <!-- spostato nav dentro-->
          <a href="../index.html"><span xml:lang="en">HOME</span></a>
          <a class="active">PROPONI UNA RICETTA</a>
          <a href="contatti.cgi">CONTATTACI</a>
          <form id=\"tfsearch\" method=\"get\" action=\"cercaricetta.cgi\">
          <div>
				  <input type=\"text\" class=\"tftextinput\" title=\"searchinput\" name=\"search_parameter\" size=\"30\" maxlength=\"30\"/>
				  <input type=\"submit\" value=\"Cerca\" title=\"searchbutton\"  class=\"tfbutton\"/>
          </div>
	       </form>
      </div>
      <div class="allinea"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in: 
		<a href="../index.html"><span xml:lang="en">Home</span></a><span>&gt;</span>
	      Proponi una ricetta
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id="content">
  <div class="main">
    <h1>Proponi una ricetta!</h1>
        <div class="info">
         <p>Sai preparare qualche prelibatezza unica? Insegnalo anche a noi!</p>
		 <p>Compila il seguente modulo per inviarci la tua ricetta!</p>
		 <p>(N.B. L'amministratore ha bisogno di tempo per leggere e approvare tutte le vostre leccornie, la pubblicazione sul sito non sara' istantanea!)</p>
         <h2>ATTENZIONE!</h2>
         <ul>
			<li><p>Tutti i campi vanno compilati, abbiamo bisogno di tutte le informazioni possibili sulla tua ricetta!</p></li>
			<li><p>E' necessaria un'immagine, anche l'occhio vuole la sua parte! Al momento sono supportati i formati .jpg, .png, e .jpeg.</p></li>
			<li><p>La dimensione dell' immagine non deve superare i 5 MB.</p></li>
			<li><p>E' necessario rispettare una precisa sintassi per l'inserimento degli ingredienti: dopo ogni singolo ingrediente inserisci un ";" (punto e virgola) e vai a capo!</p></li>
		 </ul>
         </div>
     <div class="allinea"></div>
  <div class="box-contact">
    <h1>Inviaci la tua ricetta</h1>
    <form id="contact-form" action="handle_proposta.cgi" method="post" enctype="multipart/form-data" onsubmit="return valida_campi()">
      <div id="fieldset">

            <div class="form-txt">Nome piatto </div>
            
              <input type="text" name="n_piatto" id="n_piatto" title="Inserisci il nome del tuo piatto"/>
             

          
            <div class="form-txt">Autore </div>
            
              <input type="text" name="n_author" id="n_author" title="Inserisci il nome dell'autore"/>
              
          
          
            <div class="form-txt">Breve descrizione </div>
              
              <textarea rows="20" cols="60" name="n_desc" id="n_desc"></textarea>
              

          <div class="Td">
          <div class="td">
            <div class="form-txt">Tempo (minuti)</div>
            
              <input type="text" name="n_tempo" id="n_tempo" title="Inserisci il tempo di preparazione"/>
           
           </div>
             <div class="td">
            <div class="form-txt">Difficolta'</div>
            
              <select  name="n_difficolta" title="n_difficolta">	
                <option value="1">1</option> 
                  <option value="2">2</option>
                  <option value="3">3</option>
              </select>
            
            </div>
             <div class="td">
           <div class="form-txt">Numero persone</div>
            
              <input type="text" name="n_persone" id="n_persone" title="Inserisci il numero di persone"/>
             
             </div>
             <div class="td">
             <div class="form-txt">Categoria</div>
            
              <select  name="n_categoria" title="n_categoria">
                <option value="Primi">Primi</option>
                  <option value="Secondi">Secondi</option>
                  <option value="Antipasti">Antipasti</option>
                  <option value="Dessert">Dessert</option>
              </select>
            
            </div>
          </div>


            <div class="form-txt">Carica un immagine </div>
            
              <input type="file" name="immagine" title="Carica un immagine di presentazione"/>
            
          

            <div class="form-txt">Ingredienti (ogni ingrediente deve terminare con il simbolo ; ed essere in una riga a se' stante)</div>
            
              <textarea rows="20" cols="60" id="n_ingr" name="n_ingr"></textarea>
             

            <div class="form-txt">Procedimento </div>
             
              <textarea rows="20" cols="60" name="n_proc" id="n_proc"></textarea>
              
              

        <div class="buttons">
		<div class="button">
			<input type="submit" value="Submit"/>
		</div>
	<div class="button">
		<input type="reset" value="reset"/>
	</div>
        </div>
        </div>
        <p id="err_proponi"></p>
    </form>
  </div>
  </div>
  </div>

EOF

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
<a href=\"#header\"><span id=\"up\">TORNA SU</span></a>
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
          </div>
    </div>
  </div>
</body>
</html>";
}

#Last update by Luca 07/06/2016

