#!/usr/bin/perl -w

use HTML::Parser;
use HTML::Entities;
use utf8;
sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };
sub traduci() {
	my $string = shift;
  	$string = encode_entities($string, '<>&"');
	$string = encode_entities($string);
	return $string;
}
sub leggi_post()
{	
	my($buffer, $nome, $valore, @coppia, %DATI);
	
	read (STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    # Suddivide la richiesta in un array di coppie nome valore.
    @coppia = split ('&', $buffer);
    # Elabora ogni coppia contenuta nell'array.
    foreach my $elemento (@coppia)
      {
        # Scompone la coppia.
        ($nome, $valore) = split ('=', $elemento);
        $valore =~ tr/+/ /;
        # Trasforma nel carattere corrispondente.
        $nome   =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        $valore =~ s/%([A-Fa-f0-9][A-Fa-f0-9])/pack('c',hex($1))/ge;
        # Aggiunge la coppia decodificata in un hash.
        $DATI{$nome} = $valore;
      }
      # Restituisce l'hash delle coppie
      return (%DATI);
}
# creo una pagina di avvertimento per errore di permessi
sub errore_permessi()
{
	print "Content-type:text/html\n\n";

print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	<title>Errore-Judo Club Castelfranco Veneto</title>
        <link rel="icon" type="image/png" href="../img/TaoIco.png"></link>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <base href=""/>
        <link href="../css/Main.css" rel="stylesheet" type="text/css" media="screen"/>
        <link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>
                <link href='http://fonts.googleapis.com/css?family=Shojumaru' rel='stylesheet' type='text/css'/>

    </head>
    <body>
<div><a href="Home.cgi"><img class="tao" alt="tao" src="../img/TaoLogo.png"/></a><div class="titolo"><a href="Home.cgi"><span lang="en">Judo Club</span></a></div><div class="sottotitolo"><a href="Home.cgi">Castelfranco Veneto</a></div></div>
                               		 <div class="menu">
            <ul class="lista-menu">
                <li><a href="../cgi-bin/Home.cgi"><span lang="en">HOME</span></a></li>
            <li><a href="../storia.html">STORIA CLUB</a></li>
            <li><a href="../ilJudo.html">IL <span lang="ja">JUDO</span></a></li>
            <li><a href="../ilBJJ.html">IL <span lang="ja">JIU JITSU</span> BRASILIANO</a></li> <!--verificare col screen reader la lettura giusta della parola-->
            <li><a href="../maestri.html">MAESTRI</a></li>
            <li><a href="../orari.html">ORARI</a></li>
            <li><a href="info_contatti.cgi">INFO &amp; CONTATTI</a></li>
            </ul>		
        </div>
		
		<div class="navigazione">Sei qui: errore</div>
		
        <div class="corpo">Errore, non hai i permessi per vedere questa pagina, torna alla <a href="./Home.cgi">Home</a></div>
        
        <div class="footer"> <img class="valido" alt="css valido" src="../img/cssvalido.png"/><div class="indirizzo"> Via Boito, Castelfranco Veneto</div><img class="valido" alt="xhtml valido" src="../img/xhtmlvalido.png"/></div> <!-- mettere simboli w3c e html css valido-->
        
        
    </body>
</html>
EOF
}

# creo una pagina di avvertimento personalizzabile
sub errore()
{
my $msg = shift;
	print "Content-type:text/html\n\n";

print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
	<title>Errore-Judo Club Castelfranco Veneto</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <base href=""/>
		<link rel="icon" type="image/png" href="../img/TaoIco.png"></link>
        <link href="../css/Main.css" rel="stylesheet" type="text/css" media="screen"/>
        <link href="../css/print.css" rel="stylesheet" type="text/css" media="print"/>
         <link href='http://fonts.googleapis.com/css?family=Shojumaru' rel='stylesheet' type='text/css'/>

    </head>
    <body>
		 		<div><a href="Home.cgi"><img class="tao" alt="tao" src="../img/TaoLogo.png"/></a><div class="titolo"><a href="Home.cgi"><span lang="en">Judo Club</span></a></div><div class="sottotitolo"><a href="Home.cgi">Castelfranco Veneto</a></div></div>                           		 <div class="menu">
            <ul class="lista-menu">
                <li><a href="Home.cgi"><span lang="en">HOME</span></a></li>
            <li><a href="../storia.html">STORIA CLUB</a></li>
            <li><a href="../ilJudo.html">IL <span lang="ja">JUDO</span></a></li>
            <li><a href="../ilBJJ.html">IL <span lang="ja">JIU JITSU</span> BRASILIANO</a></li> <!--verificare col screen reader la lettura giusta della parola-->
            <li><a href="../maestri.html">MAESTRI</a></li>
            <li><a href="../orari.html">ORARI</a></li>
            <li><a href="info_contatti.cgi">INFO &amp; CONTATTI</a></li>
            </ul>		
        </div>
		
		<div class="navigazione">Sei qui: errore</div>
		
        <div class="corpo">
$msg, torna alla torna alla <a href=\"$ENV{HTTP_REFERER}\">pagina precedente</a></div>
        
        <div class="footer"> <img class="valido" alt="css valido" src="../img/cssvalido.png"/><div class="indirizzo"> Via Boito, Castelfranco Veneto</div><img class="valido" alt="xhtml valido" src="../img/xhtmlvalido.png"/></div> <!-- mettere simboli w3c e html css valido-->
    </body>
</html>
EOF
}
1;
