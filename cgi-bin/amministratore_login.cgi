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


if ($auth eq "amministratoreautenticato")
{

   print "Location: console_admin.cgi\n\n";
}
if($auth ne "amministratoreautenticato")
{
	# stampo la pagina login:

print "Content-Type: text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Admin Login</title>
  <meta name=\"title\" content=\"2forchette - Login Area amministrativa\"/>
    <meta name=\"description\" content=\"Login Area amministrativa del sito 2forchette\"/>
    <meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
    <meta name=\"language\" content=\"italian it\"/>
    <meta http-equiv=\"Content-Script-Type\" content=\"text/javascript\"/>
    <meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
    <link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
    <link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
    <link rel=\"shortcut icon\" href=\"../images/favicon.ico\" type=\"image/x-icon\"/>	
     <script type=\"text/javascript\" src=\"../js/login_control.js\"></script>
</head>
<body>
<div><a class=\"salta-main\" href=\"#footer\"><span>Salta al contenuto</span></a></div>
<!--==============================header=================================-->
<div id=\"header\">
  <div class=\"main\">
    <div class=\"intestazione\">
     <div id=\"banner\"><h1><a href=\"../index.html\">2FORCHETTE</a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"proponiricetta.cgi\">PROPONI UNA RICETTA</a>          
          <a href=\"contatti.cgi\">CONTATTACI</a>
             <form id=\"tfsearch\" method=\"get\" action=\"cercaricetta.cgi\">
             <div>
            <input type=\"text\" class=\"tftextinput\" name=\"search_parameter\" title=\"inserisci testo qui\" size=\"30\" maxlength=\"30\"/>
            <input type=\"submit\" value=\"Cerca\" title=\"cerca\" class=\"tfbutton\"/>
            </div>
          </form>
        </div>
      </div>
      <div class=\"allinea\"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
      Admin Login
      </p>
    </div> 
    </div>
  </div>
</div>
<!--==============================content=================================-->
<div id=\"content\">
<div class=\"full\">
  <div class=\"main\">
    <h2>Login Area Amministrativa</h2>
    <div class=\"box-contact\">
    <form id=\"contact-form\" action=\"controllo_login.cgi\" method=\"post\" onsubmit=\"return valida_campi()\">
      <div id=\"fieldset\">
            <div class=\"form-txt\"><span xml:lang=\"en\">Username <span id=\"err_username\"></span></span></div>

              <input type=\"text\" name=\"username\" id=\"username\" title=\"inserisci qui il tuo username\"/>
             

            <div class=\"form-txt\"><span xml:lang=\"en\">Password <span id=\"err_password\"></span></span></div>

              <input type=\"password\" name=\"password\" id=\"password\" title=\"inserisci qui la tua password\"/>
              

         <div class=\"buttons\"><div class=\"button\"><input type=\"submit\" title=\"invia dati\" value=\"Submit\"/></div><div class=\"button\"><input type=\"reset\" title=\"resetta form\" value=\"Reset\"/></div></div>
      </div>
    </form>
    </div>
      </div>
      </div>
    
  </div>
<!--==============================footer=================================-->
<div id=\"footer\">
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
</html>

";
}
