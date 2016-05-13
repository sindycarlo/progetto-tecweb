#!/usr/bin/perl -w

# questo file è finito, resta solo da togliere le librerie inutili
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use XML::LibXSLT;
use File::Copy;
use POSIX;
use URI;

my $cgi = new CGI;
my $file = "../data/commenti_ricetta.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my $id = $cgi->param('id');
my $ric = $doc->findnodes("/commenti/commento[\@\id = $id]")->get_node(1);
my $parent = $ric->parentNode;
$parent->removeChild($ric);
open(OUT,">$file") or die $!;
print OUT $doc->toString;
close(OUT);			
print "Location:console_admin.cgi\n\n";
#Last update 13/05/2016 by Carlo
