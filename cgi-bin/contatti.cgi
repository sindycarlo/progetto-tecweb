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
  <meta name=\"title\" content=\"2forchette - Contatti\"/>
    <meta name=\"description\" content=\"Sezione contatti del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"4forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
    <script type=\"text/javascript\" src=\"../js/check_mail.js\"></script>
</head>
<body>
<div><a class=\"salta-main\" href=\"#contact-form\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
     <div id=\"banner\"><h1><a href=\"index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>          
          <a href=\"ricettagiorno.cgi\">RICETTA DEL GIORNO</a>
          <a class=\"active\">CONTATTACI</a>
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
    <h1>Modulo contatti</h1>
    <div class=\"info\">
    <p>Inviaci un'email e noi ti risponderemo il prima possibile, (descrivi in maniera precisa il problema).</p></div>
    <div class=\"box-contact\">
    <form id=\"contact-form\" action=\"sendmail.cgi\" method=\"post\" enctype=\"multipart/form-data\" onsubmit=\"return valida_campi()\">
    <span><p id=\"err_email\"></p></span>
      <div id=\"fieldset\">

            <div class=\"form-txt\">Il tuo nome </div>
            <label>
              <input type=\"text\" name=\"nome\" id=\"nome\" title=\"inserisci il tuo nome qui\"/>
             </label>

            <div class=\"form-txt\"><span xml:lang=\"en\">Email </span></div>
            <label class=\"email\">
              <input type=\"text\" name=\"email\" id=\"email\" title=\"inserisci il tuo indirizzo email\"/>
              </label>

            <div class=\"form-txt\">Inserire un messaggio </div>
            <label class=\"message\">
              <textarea name=\"question\" id=\"question\" rows=\"20\" cols=\"60\"></textarea>
              </label>
            <div class=\"allinea\"></div>
          
        
        <div class=\"buttons\"><div class=\"button\"><input type=\"submit\" value=\"Send mail\"/></div><div class=\"button\"><input type=\"reset\"/></div></div>
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