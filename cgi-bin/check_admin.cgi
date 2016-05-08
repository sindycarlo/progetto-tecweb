#!/usr/bin/perl -w

# servono tutte ste librerie?
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

my $input_login = $cgi->param('login');
my $input_pw = $cgi->param('pw');

my $file = "../data/amministratore.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my $credenziali = $doc->findnodes("/amministratore/[first()]")->get_node(1);

#questo if è scritto in pseudo codice, troverò la sintassi corretta prossimamente
if($input_login->text()==$credenziali->findvalue('login') && $input_pw->text()==$credenziali->findvalue('password'))
{
	#login con successo, passo alla pagina console admin...
	print "Location:...\n\n";
}
else
{
	#login errato, do un messaggio d'errore che lo notifica (javascript probabilmente)	
	print "Location:...\n\n";
}

# Last Update by Luca 26/04/2016
