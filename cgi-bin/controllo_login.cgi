#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;


my $q = new CGI;




      my $username = $q->param('username');
      my $password = $q->param('password');
      my $auth="amministratoreautenticato";
      my $file="../data/amministratore.xml";

  #creo oggetto parser:
	my $parser=XML::LibXML->new();  
      
  # apertura file e lettura input:
	my $doc = $parser->parse_file($file);
  #controllo password:    
	my $pwd = $doc->findvalue("/amministratore[username=\"$username\"]/password");

      if($pwd ne $password)#se la password non coincide
      	{
      				print "Content-Type: text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Admin Login</title>
  <meta name=\"title\" content=\"2forchette - Errore\"/>
    <meta name=\"description\" content=\"Errore login del sito 2forchette\"/>
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
      <div id=\"banner\"><h1><a href=\"../index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"allinea\"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in:
        <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
    <a href=\"amministratore_login.cgi\">Amministratore login</a><span>&gt;</span>
    Errore
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
  <div class=\"main\">
    <h1>Errore</h1>
    <div class=\"box-contact\">
    <p><span lang=\"en\">Password</span> sbagliata o vuota, riprova di nuovo!</p><a href=\"amministratore_login.cgi\"><span lang=\"en\">Torna alla pagina precedente</span></a>
    </div>
      </div>
    
  </div>
<!--==============================footer=================================-->
<div id=\"footer\">
    <div class=\"main\">
          <div id=\"inline\">

          <p>             
            <span>2Forchette</span> -copyright 2016 CARLO E LUCA produzione riservata - P.IVA 0838456799
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
</body>";

      	}
      	if($pwd eq $password)
      	{
			#controllo se la sessione esiste già:
			my $session = CGI::Session->load() or die $!;
			
			
			if($session->is_expired || $session->is_empty){
			# sessione non esiste quindi la creo
			my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
			# aggiungo i parametri amministratore alla sessione
			$session->param("username", $username);
			$session->param("auth", $auth);

			# creo il cookie
			my $cookie1 = CGI::Cookie->new(-name => $session->name, -value => $session->id);
			my $cookie2 = CGI::Cookie->new(-name => "JCC", -value => $username);
            my $cookie3 = CGI::Cookie->new(-name => "JCCA", -value => $auth);
			print header(-cookie => [$cookie1,$cookie2,$cookie3]);
		

      print "Location: console_admin.cgi\n\n";




		}else{
		
		
			# la sessione esiste
			# controllo l'esistenza del cookie
			my %cookie = CGI::Cookie->fetch;
			my $cook = $cookie{'JCCA'};
			my $cook2 = $cookie{'JCCA'};
			# se i 2 cookie fondamentali non sono presenti lo ricreo
			if(!defined $cook){
				# ricreo il cookie se mancante
				my $cookie3 = CGI::Cookie->new(-name => "JCCA", -value => $auth);
				print header(-cookie => $cookie3);				
			}
			if(!defined $cook2){
                        # ricreo il cookie se mancante
			my $cookie2 = CGI::Cookie->new(-name => "JCC", -value => $username);
				print header(-cookie => $cookie2);				
			}
					      				print "Content-Type: text/html\n\n";

print "
<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
<head>
  <title>Admin Login</title>
  <meta name=\"title\" content=\"2forchette - Login  effettutato\"/>
    <meta name=\"description\" content=\"Login del sito 2forchette\"/>
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
      <div id=\"banner\"><h1><a href=\"../index.html\"> <span>2FORCHETTE</span> </a></h1></div>
      <div class=\"allinea\"></div>
    <div id='breadcrumb'>
        <p>Ti trovi in:
        <a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
    <a href=\"amministratore_login.cgi\">Amministratore login</a><span>&gt;</span>
    Login effettuato
      </p>
    </div> 
    </div>
  </div>
</div>

<!--==============================content=================================-->
<div id=\"content\">
  <div class=\"main\">
    <h1>Login</h1>
    <div class=\"box-contact\">
    <p><span lang=\"en\">Login</span>effettuato con successo $username, si consiglia di tenere i cookie sempre attivi.</p><a href=\"console_admin.cgi\"><span lang=\"en\">Vai a Gestisci ricette</span></a>
    </div>
      </div>
    
  </div>
<!--==============================footer=================================-->
<div id=\"footer\">
    <div class=\"main\">
          <div id=\"inline\">

          <p>             
            <span>2Forchette</span> -copyright 2016 CARLO E LUCA produzione riservata - P.IVA 0838456799
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
          </p>          <p>
          ACCESSO EFFETTUTATO COME ADMIN:
          <a href=\"logout.cgi\"><button type=\"submit\" name=\"delete\"><span xml:lang=\"en\">logout</span></button></a>
          </p>
          </div>
    
    </div>
  </div>
</body>";
			
		} 
      
		}
	

