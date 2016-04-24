#!/usr/bin/perl -w

# file che controlla l'inserimento commenti
# carico le librerie
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use File::Basename; # serve per uploadare i file
use Time::localtime; # per conoscere la data corrente
use POSIX;
use URI;
use utf8;



my $cgi = CGI->new(); # create new CGI object

my $data_stuff = $cgi->param('new_stuff');
my $data_bla = $cgi->param('new_bla');
my $data_contenuto = $cgi->param('new_contenuto');
#ho preso i dati che ha inserito l'utente (ATTENZIONE CHE NON SONO PARSATI MA PER ORA TENIAMO COSI)


	my $file = "../data/cose.xml";
	
	# creazione oggetto parser
	my $parser = XML::LibXML->new();
	
	# apertura file e lettura input
	my $doc = $parser->parse_file($file);
	
	# estrazione radice
	my $root = $doc->getDocumentElement;
	
	# creo nuovo oggetto in cui salvo i dati dopo avergli dato un' id
	my $thing = XML::LibXML::Element->new('thing');
	
#	my $stuff = XML::LibXML::Element->new('stuff');
#	$stuff->appendText($data_stuff); non dovrebbe servire
#	$thing->appendChild($stuff);
 
        #calcolo l'id
        my $id;
	my $path = $doc->findnodes("/cose/thing[last()]")->get_node(1);
	if ($path){
		$id = $path->getAttribute('IDcode');
	}
	else{
		$id=0;
	}
	$thing->setAttribute("IDcode", $id+1); 


	my $stuff = XML::LibXML::Element->new('stuff');
	$stuff->appendText($data_stuff);
	$thing->appendChild($stuff);
	
	my $bla = XML::LibXML::Element->new('blabla');
	$bla->appendText($data_bla);
	$thing->appendChild($bla);
	
	my $contenuto = XML::LibXML::Element->new('contenuto');
	$contenuto->appendText($data_contenuto);
	$thing->appendChild($contenuto);

#	ho finito di creare il nodo
#	lo inserisco nel mio alberello natalizio xml
	
	my $cose = $doc->findnodes("/cose")->get_node(1);
	
	$cose->appendChild($thing);
	
	open(OUT,">$file") or die $!;
	print OUT $doc->toString;
	close(OUT);

        print "Location:proponiricetta.cgi\n\n";
