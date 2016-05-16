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
use POSIX;
use URI;
use utf8;

my $cgi = CGI->new();#creo nuovo oggetto cgi


my $user = $cgi->param('user');
my $comm = $cgi->param('commento');
my $email = $cgi->param('email');

	my $file = "../data/commenti_ricetta.xml";
	
	# creazione oggetto parser
	my $parser = XML::LibXML->new();
	
	# apertura file e lettura input
	my $doc = $parser->parse_file($file);
	
	# estrazione radice
	my $root = $doc->getDocumentElement;
	
	# creo nuovo commento
	my $commento = XML::LibXML::Element->new('commento');
	
	my $utente = XML::LibXML::Element->new('user');
	$utente->appendText($user);
	$commento->appendChild($utente);
        #calcolo l'id
        my $id;
		my $path = $doc->findnodes("/commenti/commento[last()]")->get_node(1);
if ($path){
		$id = $path->getAttribute('id');
}
else{
$id=0;
}
		$commento->setAttribute("id", $id+1); 


	my $data = XML::LibXML::Element->new('datacommento');
	# calcolo la data di adesso
	my $stime = localtime;
	my $Y = $stime->year+1900;
	my $M = $stime->mon+1;
	my $D = $stime->mday;
	my $dataoggi = "$Y-$M-$D";
	
	$data->appendText($dataoggi);
	$commento->appendChild($data);
	
	my $testo = XML::LibXML::Element->new('testo');
	$testo->appendText($comm);
	$commento->appendChild($testo);
	
	my $mail = XML::LibXML::Element->new('email');
	$mail->appendText($email);
	$commento->appendChild($mail);
	
	my $commenti = $doc->findnodes("/commenti")->get_node(1);
	
	$commenti->appendChild($commento);
	
	open(OUT,">$file") or die $!;
	print OUT $doc->toString;
	close(OUT);

        print "Location:contatti.cgi\n\n";
