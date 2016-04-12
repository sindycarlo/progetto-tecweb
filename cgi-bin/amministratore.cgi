#!/usr/bin/perl -w

# librerie: non so quali servono e quali no
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;

# da completare!!!


# stampo la prima parte della pagina
print "Content-Type: text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Admin Login</title>
  <meta name=\"title\" content=\"4forchette - Progetto di Tecnlogie web\"/>
    <meta name=\"description\" content=\"Login Area amministrativa del sito 4forchette\"/>
    <meta name=\"keywords\" content=\"4forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
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
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
      Login
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
  <div class=\"main\">
    <h2>Login</h2>
    <div class=\"info\">
    <p>Tutti i campi contrassegnati da asterisco (*) sono obbligatori.</p></div>
    <div class=\"box-contact\">
    <form id=\"contact-form\" action=\"\" method=\"post\"><!--da sistemare-->
      <div id=\"fieldset\">
        <div class=\"colonna1\">
          <div>
            <div class=\"form-txt\"><span xml:lang=\"en\">Username *</span></div>
            <label class=\"name\">
              <input type=\"text\" name=\"nr_author\" title=\"inserisci il tuo nome qui\"/>
             </label>
            <div class=\"allinea\"></div>
          </div>
          <div>
            <div class=\"allinea\"></div>
          </div>
          <div>
            <div class=\"form-txt\"><span xml:lang=\"en\">Password *</span></div>
            <label class=\"email\">
              <input type=\"text\" name=\"nr_email\"  title=\"inserisci il tuo indirizzo email\"/>
              </label>
            <div class=\"allinea\"></div>
          </div>
            <div class=\"allinea\"></div>
         </div>
         <div class=\"buttons\"><div class=\"button\"><input type=\"submit\" value=\"accedi\"/></div><div class=\"button\"><input type=\"reset\" value=\"reset\"/></div></div>
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
            <span>4Forchette</span> - Via Molinari 63, 33170, Milano- p. iva 02768250152
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
</body>
</html>";








