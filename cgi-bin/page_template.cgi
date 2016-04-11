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

# leggo l'id da get
my $cgi = new CGI;
my $id = $cgi->param('id');


my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);


my $thing = $doc->findnodes("/ricetteDB/ricetta")->get_node(1);#problema relativo a quale ricetta estrarre!!!

my $categoria=$thing->findvalue('categoria');
my $autore=$thing->findvalue('autore');
my $descrizione=$thing->findvalue('descrizione');




#bisogna stampare la pagina corretta relativa a quella ricetta!!
# stampo la pagina
print "Content-Type: text/html\n\n";

print "<html> <head>\n";
print "</head>\n";
print "<body>\n";
print "<h1>$categoria</h1>\n";
print "<h2>$autore</h2>\n";
print "<p>$descrizione</p>\n";
print "</body> </html>\n";
