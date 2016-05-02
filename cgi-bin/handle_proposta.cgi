#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use File::Basename; # serve per uploadare i file
use Time::localtime; # per conoscere la data corrente
use CGI::Pretty qw(:html3);
use POSIX;
use URI;
use utf8;

# definisco la dimensione massima del file uploadato (5Mb)
$CGI::POST_MAX = 1024 * 5000;

my $file_er = "a-zA-Z0-9_.-";
my $upload_dir = "../images";


my $cgi = CGI->new(); # create new CGI object

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

chomp $filename;
# faccio il parsing dell'immagine per estrarre il nome
my ($nome, $path, $estensione) = fileparse($filename, '\..*');



if (($estensione =~ /.png/i) || ($estensione =~ /.jpg/i) || ($estensione =~ /.jpeg/i) || ($estensione =~ /.gif/i)){
	# estensione valida
	$filename = $nome . $estensione;
	$filename =~ tr/ /_/;
	$filename =~ s/[^$file_er]//g;
	
	if($filename =~ /^([$file_er]+)$/){
		
		$filename = $1;
	}
	else{
		# stampo pagina di errore
		my $err_msg = "Il nome del file contiene caratteri che non sono ammessi.";
		&errore($err_msg);
exit;
	}
	my $file_up = $cgi->upload("immagine");

		# carico l'immagine nella cartella img
	open (UPLOADFILE, ">../public_html/images/$filename") or die "$!";
	binmode UPLOADFILE;

	while( <$file_up> ){
		print UPLOADFILE;
	}
	close UPLOADFILE;

	#ho preso i dati che ha inserito l'utente (ATTENZIONE CHE NON SONO PARSATI MA PER ORA TENIAMO COSI)
	my $file = "../data/4forchette.xml";
	
	# creazione oggetto parser
	my $parser = XML::LibXML->new();
	
	# apertura file e lettura input
	my $doc = $parser->parse_file($file);
	
	# estrazione radice
	my $root = $doc->getDocumentElement;
	
	# creo nuovo oggetto in cui salvo i dati dopo avergli dato un' id
	my $thing = XML::LibXML::Element->new('ricetta');
 
        #calcolo l'id
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

	foreach my $sticazzi (%arrayingr)
	{
		my $newing = XML::LibXML::Element->new('ingr');
		$newing->appendText($sticazzi);
		$ingredienti->appendChild($newing);
	}

	$thing->appendChild($ingredienti);
#	ho finito di creare il nodo
#	lo inserisco nel mio alberello natalizio xml
	
	my $ricette = $doc->findnodes("/ricetteDB")->get_node(1);
	
	$ricette->appendChild($thing);
	
	open(OUT,">$file") or die;
	print OUT $doc->toString;
	close(OUT);

        print "Location:proponiricetta.cgi\n\n";
	
}

#LAST UPDATE BY LUCA 02/05/2016
