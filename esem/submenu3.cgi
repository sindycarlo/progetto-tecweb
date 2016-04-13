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

print "<html> <head>\n";
print "<title>SUBMENU</title>";
print "</head>\n";
print "<body>\n";
print "<h1>elenco</h1>\n";

# a questo punto per sapere quanti link ci sono devo leggere il file xml

my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @ricetteDB = $doc->findnodes("/ricetteDB/ricetta");

foreach my $ricetta (@ricetteDB)
{
     	my $nomePiatto = $ricetta->findvalue('nomePiatto');
	my $id = $ricetta->getAttribute('IDCode');
	print "<p><a href=\"page_template3.cgi?id=$id\">link che parla di $nomePiatto</a></p>"; 
}


# stampo la fine della pagina
print "</body> </html>\n";
