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

my $file = "../data/cose.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my @cose = $doc->findnodes("/cose/thing");
@cose=reverse(@cose);

foreach my $thing (@cose)
{
     	my $bla = $thing->findvalue('blabla');
	my $id = $thing->getAttribute('IDcode');
	print "<a href=\"page_template.cgi?id=$id\">link che parla di $bla</a>"; 
}


# stampo la fine della pagina
print "</body> </html>\n";
