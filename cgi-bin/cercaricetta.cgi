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


print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Contattaci</title>
  <meta name=\"title\" content=\"2forchette - Cerca ricetta\"/>
    <meta name=\"description\" content=\"Sezione Cerca ricetta del sito 2forchette\"/>
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
     <div id=\"banner\"><h1><a href=\"index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>          
          <a class=\"active\">CERCA RICETTA</a>
          <a href=\"contatti.cgi\">CONTATTACI</a>
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
  <div class=\"main\">
    <h2>Cerca ricetta</h2>
    <div class=\"info\">
    <span>ATTENZIONE WORK IN PROGRESS.Il modulo potrebbe non funzionare. ci dispiace per l'inconveniente.</span>
    <p>Il modulo puo' essere utilizzato per cercare una ricetta che vi interessa o vi piacerebbe consultare.</p></div>
    <div class=\"box-contact\">
     <form id=\"contact-form\" action=\"\" method=\"post\">
      <div id=\"fieldset\"> <!-- <fieldset> non è accettato da html5 -->

            <div class=\"form-txt\">Cerca</div>
            <label>
              <input type=\"text\" name=\"n_search\" id=\"n_search\"title=\"Inserisci la keyworld per il tuo piatto\"/>
             </label>
             
            <div class=\"form-txt\">Tempo di preparazione</div>
            <label>
              <input type=\"text\" name=\"n_tempo\" id=\"n_tempo\" title=\"Inserisci il tempo di preparazione\"/>
           </label>

            <div class=\"form-txt\">Difficolta'</div>
            <label>
              <select  name=\"n_difficolta\">	
                <option value=\"1\">1</option> 
                  <option value=\"2\">2</option>
                  <option value=\"3\">3</option>
              </select>
            </label>

      
            <div class=\"form-txt\">Categoria </div>
            <label>
              <select  name=\"n_categoria\">
                <option value=\"Primo\">Primi</option>
                  <option value=\"Secondo\">Secondi</option>
                  <option value=\"Antipasti\">Antipasti</option>
                  <option value=\"Dessert\">Dessert</option>
              </select>
            </label>

        <div class=\"buttons\">
		<div class=\"button\">
			<input type=\"submit\" value=\"Cerca\"/>
		</div>
	<div class=\"button\">
		<input type=\"reset\"/>
	</div>
        </div>
        </div>
    </form>
    </div>
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
