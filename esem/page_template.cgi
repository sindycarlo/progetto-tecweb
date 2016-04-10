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


my $file = "../data/cose.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);


my $thing = $doc->findnodes("/cose/thing[\@\IDcode = $id]")->get_node(1);

my $stuff=$thing->findvalue('stuff');
my $contenuto=$thing->findvalue('contenuto');        

# stampo la pagina
print "Content-Type: text/html\n\n";

print "<html> <head>\n";
print "<title>template - $id</title>";
print "</head>\n";
print "<body>\n";
print "<h1>$stuff</h1>\n";
print "<p>$contenuto</p>\n";
print "</body> </html>\n";