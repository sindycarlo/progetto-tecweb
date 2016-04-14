#!/usr/bin/perl -w

# librerie: servono tutte?
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;

# salto la parte delle sessioni/cookie/ecc per ora


# stampo la prima parte della pagina
print "Content-Type: text/html\n\n";


print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
    <title>Dessert</title>
    <meta name=\"title\" content=\"4forchette - Progetto di Tecnlogie web\"/>
    <meta name=\"description\" content=\"Sezione dessert del sito 4forchette\"/>
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
      <div id=\"banner\"><h1><a href=\"index.html\"><span>2FORCHETTE</span></a></h1></div>
      <div class=\"header-menu\">
        <div id=\"nav\">
          <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
          <a href=\"../proponiricetta.html\">PROPONI UNA RICETTA</a>
          <a href=\"../ricettagiorno.html\">RICETTA DEL GIORNO</a>
          <a href=\"../contatti.html\">CONTATTACI</a>
        </div>
      </div>
            <div class=\"allinea\"></div>
                <div id='breadcrumb'>
        <p>Ti trovi in:
      <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
      Dessert
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
    <div class=\"main\">
    <h2>Dolci e dessert</h2>
    
    <div class=\"box-img\"><img src=\"../images/dolce.jpg\" alt=\"immagine che descrive la crostata con crema\"/></div>
    <div>
        <p>
L’Italia è famosa nel mondo per i numerosi dolci e dessert tipici della tradizione. Basta citare il tiramisù, golosità in grado di soddisfare il palato di tutti, il panettone o il pandoro, tipici nel periodo natalizio, o i tradizionali dolci del sud come la pastiera napoletana o la cassata siciliale. Impossibile dimenticare il carnevale, periodo perfetto per preparare ogni tipologia di dolce fritto come frappe o chiacchiere né i dolci al cucchiaio come il biancomangiare o il budino al cioccolato.
 E se i biscotti meritano un capitolo a parte, la bella stagione è subito sinonimo di gelati artigianali al pistacchio, alla crema o ai gusti più insoliti.

</p>
    </div>    
    <div class=\"allinea\"></div>    
        
    </div>
      <div class=\"contenitore\">";


my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @cose = $doc->findnodes("/ricetteDB/ricetta[categoria='Dessert']");

foreach my $thing (@cose)
{
      my $bla = $thing->findvalue('nomePiatto');
  my $id = $thing->findvalue('imgPiatto');
  print "
  <div class=\"blocco2\">
      <ul class=\"lista-menu\">
      <li>
        <a href=\"page_template.cgi?id=$id\">$bla</a> 
        <div class=\"box-img\"><img src=\"../images/$id\" alt=\"immagine che descrive $bla\"/></div>
      </li>
      </ul>
  </div>
    <div class=\"allinea\"></div>
</div>"
}
print "
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






