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

# stampo la pagina
print "Content-type:text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it"> 
<head>
    <title>Proponi una ricetta</title>
    <meta name="title" content="2forchette - Proponi una ricetta"/>
    <meta name="description" content="Sezione proponi una ricetta del sito 2forchette"/>
    <meta name="keywords" content="2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo"/>
    <meta name="language" content="italian it"/>
    <meta name="author" content="Carlo Sindico ,Luca Alessio"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link rel="stylesheet" href="../css/style.css" type="text/css" media="screen"/>
    <link rel="stylesheet" href="../css/print.css" type="text/css" media="print"/>
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
          <a href="../ricettagiorno.html">RICETTA DEL GIORNO</a>
          <a href="../contatti.html">CONTATTACI</a>
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
         <!--da qualche parte precisare che gli ingredienti vanno inseriti uno a uno e poi si deve andare caporiga-->
         </div>
     <div class="allinea"></div>
  <div class="box-contact">
    <h1>Inviaci la tua ricetta</h1>
    <form id="contact-form" action="handle_proposta.cgi" method="post">
      <div id="fieldset"> <!-- <fieldset> non è accettato da html5 -->

            <div class="form-txt">Nome piatto </div>
            <label>
              <input type="text" name="n_piatto" title="Inserisci il nome del tuo piatto"/>
             </label>

          
            <div class="form-txt">Autore </div>
            <label>
              <input type="text" name="n_author" title="Inserisci il nome dell'autore"/>
              </label>
          
          
            <div class="form-txt">Breve descrizione </div>
            <label class="message">
              <textarea rows="20" cols="60" name="n_desc" placeholder="Descrivi brevemente la tua prelibatezza..."></textarea>
              </label>

          <div class="Td"> <!-- sarebbe meglio un nome diverso e si mette al posto di form-txt -->
            <div class="form-txt">Tempo di preparazione e Difficolta</div>
            <label>
              <input type="text" name="n_tempo" title="Inserisci il tempo di preparazione"/>
           </label>
     
            <label>
              <select  name="n_difficolta">	
                <option value="1">1</option> 
                  <option value="2">2</option>
                  <option value="3">3</option>
              </select>
            </label>
          </div>


    <div class="form-txt">Numero persone </div> <!-- classe speciale per renderlo più piccolo anche questo -->
            <label>
              <input type="text" name="n_persone" title="Inserisci il numero di persone"/>
             </label>



            <div class="form-txt">Carica un'immagine </div>
            <label>
              <input type="file" name="n_immagine" title="Carica un'immagine di presentazione"/>
             </label>
          
             
            <div class="form-txt">Categoria </div>
            <label>
              <select  name="n_categoria">
                <option value="Primo">Primi</option>
                  <option value="Secondo">Secondi</option>
                  <option value="Antipasti">Antipasti</option>
                  <option value="Dessert">Dessert</option>
              </select>
            </label>

            <div class="form-txt">Ingredienti </div>
            <label>
              <input type="text" name="n_ingredienti" title="quanti ingredienti"/>
             </label>

            <div class="form-txt">Procedimento </div>
            <label class="message">
              <textarea rows="20" cols="60" name="n_proc" placeholder="Spiega come prepare il tuo manicaretto..."></textarea>
              </label>

        <div class="buttons">
		<div class="button">
			<input type="submit"/>
		</div>
	<div class="button">
		<input type="reset"/>
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
            <span>2Forchette</span> -copyright 2016 CARLO&LUCA produzione riservata - P.IVA 0838456799
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
	  </div>
	</div>
</body>
</html>

<!-- Last Update by Luca & Carlo 28/04/2016 -->

EOF
