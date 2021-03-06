#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use File::Basename;
use CGI::Pretty qw(:html3);
use POSIX;
use URI;
use utf8;

my $session = CGI::Session->load() or die $!;

my $auth = $session->param('auth');

require ('funzioni.pl');

$CGI::POST_MAX = 1024 * 5000;

my $file_er = \"a-zA-Z0-9_.-";
my $upload_dir = "../images";

my $cgi = CGI->new();

my $filename = $cgi->param('immagine');
my $data_piatto = $cgi->param('n_piatto');
my $data_author = $cgi->param('n_author');
my $data_desc = $cgi->param('n_desc');
my $data_tempo = $cgi->param('n_tempo');
my $data_ingr = $cgi->param('n_ingr');
my $data_difficolta = $cgi->param('n_difficolta');
my $data_Persone = $cgi->param('n_persone');
my $data_categoria = $cgi->param('n_categoria');
my $data_proc = $cgi->param('n_proc');

$data_piatto = removewhitespace(convertstring($data_piatto));
$data_desc = removewhitespace(convertstring($data_desc));
$data_author = removewhitespace(convertstring($data_author));
$data_tempo = removewhitespace(convertstring($data_tempo));
$data_Persone = removewhitespace(convertstring($data_Persone));
$data_proc = removewhitespace(convertstring($data_proc));

chomp $filename;

my ($nome, $path, $estensione) = fileparse($filename, '..*');

if (($estensione =~ /.png/i) || ($estensione =~ /.jpg/i) || ($estensione =~ /.jpeg/i) || ($estensione =~ /.gif/i))
{
	$filename = $nome . $estensione;
	$filename =~ tr/ /_/;

	my $file_up = $cgi->upload("immagine");
	
	open (UPLOADFILE, ">../public_html/images/$filename") or die "$!";
	binmode UPLOADFILE;

	while( <$file_up> ){
		print UPLOADFILE;
	}
	close UPLOADFILE;

	my $file = "../data/4forchette.xml";
	
	my $parser = XML::LibXML->new();
	
	my $doc = $parser->parse_file($file);
	
	my $root = $doc->getDocumentElement;
	
	my $thing = XML::LibXML::Element->new('ricetta');
 
    my $id;
	my $path = $doc->findnodes("/ricetteDB/ricetta[last()]")->get_node(1);
	if ($path){
		$id = $path->getAttribute('IDCode');
	}
	else{
		$id=0;
	}
	$thing->setAttribute("IDCode", $id+1); 


	my $piatto = XML::LibXML::Element->new('nomePiatto');
	$piatto->appendText($data_piatto);
	$thing->appendChild($piatto);
	
	my $author = XML::LibXML::Element->new('autore');
	$author->appendText($data_author);
	$thing->appendChild($author);
	
	my $desc = XML::LibXML::Element->new('descrizione');
	$desc->appendText($data_desc);
	$thing->appendChild($desc);

	my $tempo = XML::LibXML::Element->new('tempoPreparazione');
	$tempo->appendText($data_tempo);
	$thing->appendChild($tempo);

	my $difficolta = XML::LibXML::Element->new('difficolta');
	$difficolta->appendText($data_difficolta);
	$thing->appendChild($difficolta);

	my $persone = XML::LibXML::Element->new('quantePersone');
	$persone->appendText($data_Persone);
	$thing->appendChild($persone);

	my $imm = XML::LibXML::Element->new('imgPiatto');
		$imm->appendText("$filename");
		$thing->appendChild($imm);

	my $categoria = XML::LibXML::Element->new('categoria');
	$categoria->appendText($data_categoria);
	$thing->appendChild($categoria);

	my $proc = XML::LibXML::Element->new('procedimento');
	$proc->appendText($data_proc);
	$thing->appendChild($proc);
 
	my $ingredienti = XML::LibXML::Element->new('ingredienti');

	my %arrayingr = split /[;]/, $data_ingr;

	foreach my $ing (%arrayingr)
	{
		my $newing = XML::LibXML::Element->new('ingr');
		$newing->appendText($ing);
		$ingredienti->appendChild($newing);
	}

	$thing->appendChild($ingredienti);
		
	my $ricette = $doc->findnodes("/ricetteDB")->get_node(1);
	
	$ricette->appendChild($thing);
	
	open(OUT,">$file") or die;
	print OUT $doc->toString;
	close(OUT);
		
	print "Content-type:text/html\n\n";

	print "
	<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
	<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
	<head>
		<title>Proponi una ricetta</title>
		<meta name=\"title\" content=\"2forchette - Proponi una ricetta\"/>
		<meta name=\"description\" content=\"Sezione proponi una ricetta del sito 2forchette\"/>
		<meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
		<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
		<link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
		<link rel=\"shortcut icon\" href=\"../images/favicon.ico\" type=\"image/x-icon\"/>	
		<link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
	</head>

	<body>
	<div><a class=\"salta-main\" href=\"#contact-form\"><span>Salta al contenuto</span></a></div>
	<!--==============================header=================================-->
	<div id=\"header\">
	  <div class=\"main\">
		<div class=\"intestazione\">
		  <div id=\"banner\"><h1><a href=\"../index.html\">2FORCHETTE</a></h1></div>
		  <div class=\"header-menu\" id=\"nav\">
			<!-- spostato nav dentro-->
			  <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
			  <a class=\"active\">PROPONI UNA RICETTA</a>
			  <a href=\"contatti.cgi\">CONTATTACI</a>
			  <form id=\"tfsearch\" method=\"get\" action=\"cercaricetta.cgi\">
			  <div>
				<input type=\"text\" class=\"tftextinput\" name=\"search_parameter\" title=\"inserisci testo qui\" size=\"30\" maxlength=\"30\">
				<input type=\"submit\" value=\"Cerca\" title=\"cerca\" class=\"tfbutton\">
				</div>
			  </form>
		  </div>
		  <div class=\"allinea\"></div>
		<div id='breadcrumb'>
			<p>Ti trovi in: 
			<a href=\"index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
			  Proponi una ricetta
		  </p>
		</div> 
		</div>
	  </div>
	</div>

	<!--==============================content=================================-->
	<div id=\"content\">
	<div class=\"full\">
	  <div class=\"main\">
		<h1>Informazioni</h1>
			  <div class=\"box-contact\">
			  <p>Ricetta inviata con successo! In Attesa di approvazione da parte dell'amministratore</p><a href=\"proponiricetta.cgi\">Torna alla pagina precedente</a>
			  </div>
	  </div>
	  </div>
	  </div>
	";		
}
else 
{
	print "Content-type:text/html\n\n";

	print "
	<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">
	<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"it\" lang=\"it\"> 
	<head>
		<title>Proponi una ricetta</title>
		<meta name=\"title\" content=\"2forchette - Errore\"/>
		<meta name=\"description\" content=\"Sezione Errore proponi una ricetta del sito 2forchette\"/>
		<meta name=\"keywords\" content=\"2forchette, progetto, tecnologie web, cucina, ricette, piatti, cibo\"/>
		<meta name=\"language\" content=\"italian it\"/>
		<meta name=\"author\" content=\"Carlo Sindico ,Luca Alessio\"/>
		<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
		<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>
		<link rel=\"stylesheet\" href=\"../css/style.css\" type=\"text/css\" media=\"screen\"/>
		<link rel=\"shortcut icon\" href=\"../images/favicon.ico\" type=\"image/x-icon\"/>	
		<link rel=\"stylesheet\" href=\"../css/print.css\" type=\"text/css\" media=\"print\"/>
	</head>

	<body>
	<div><a class=\"salta-main\" href=\"#contact-form\"><span>Salta al contenuto</span></a></div>
	<!--==============================header=================================-->
	<div id=\"header\">
	  <div class=\"main\">
		<div class=\"intestazione\">
		  <div id=\"banner\"><h1><a href=\"../index.html\">2FORCHETTE</a></h1></div>
		    <div class=\"header-menu\" id=\"nav\">
			  <a href=\"../index.html\"><span xml:lang=\"en\">HOME</span></a>
			  <a class=\"active\">PROPONI UNA RICETTA</a>
			  <a href=\"contatti.cgi\">CONTATTACI</a>
			  <form id=\"tfsearch\" method=\"get\" action=\"cercaricetta.cgi\">
			  <div>
				<input type=\"text\" class=\"tftextinput\" name=\"search_parameter\" title=\"inserisci testo qui\" size=\"30\" maxlength=\"30\">
				<input type=\"submit\" value=\"Cerca\" title=\"cerca\" class=\"tfbutton\">
				</div>
			  </form>
		  </div>
		  <div class=\"allinea\"></div>
		<div id='breadcrumb'>
			<p>Ti trovi in: 
			<a href=\"../index.html\"><span xml:lang=\"en\">Home</span></a><span>&gt;</span>
		<a href=\"proponiricetta.cgi\">Proponi ricetta</a><span>&gt;</span>
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
			  <p> Immagine non presente o formato immagine non supportato!</p><a href=\"proponiricetta.cgi\">Torna alla pagina precedente</a>
		</div>
			
	  </div>
	  </div>
	";
}
if($auth eq "amministratoreautenticato")
{
	print"<!--==============================footer=================================-->
	<div id=\"footer\">
		  <div class=\"main\">
			  <div id=\"inline\">
				<p>             
				<span>2Forchette</span> -copyright 2016 CARLO E LUCA produzione riservata - P.IVA 0838456799
				   </p>
				<p>
		 <img src=\"http://www.w3.org/Icons/valid-xhtml10\" alt=\"Valid XHTML 1.0 Strict\"/>

       	 <img src=\"http://jigsaw.w3.org/css-validator/images/vcss\" alt=\"CSS Valido!\"/>

       	 <img src=\"../images/valid_wcag_aaa.gif\" alt=\"Totally Valid WCAG 2.0 AAA\" />

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
	print"<!--==============================footer=================================-->
	<div id=\"footer\">
		  <div class=\"main\">
			  <div id=\"inline\">
				<p>             
				<span>2Forchette</span> -copyright 2016 CARLO E LUCA produzione riservata - P.IVA 0838456799
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
	</html>";
}
#last update by Carlo 12/06/2016

