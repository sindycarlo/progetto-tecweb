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


my $thing = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $id]")->get_node(1);

my $stuff=$thing->findvalue('nomePiatto');
my $contenuto=$thing->findvalue('descrizione');        

# stampo la pagina
print "Content-Type: text/html\n\n";

print "<html> <head>\n";
print "<title>template - $id</title>";
print "</head>\n";
print "<body>\n";
print "<h1>$stuff</h1>\n";
print "<p>$contenuto</p>\n";
print "</body> </html>\n";
