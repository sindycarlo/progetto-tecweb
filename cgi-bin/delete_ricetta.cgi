#!/usr/bin/perl -w

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
my $file = "../data/4forchette.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my $id = $cgi->param('id');
my $ric = $doc->findnodes("/ricetteDB/ricetta[\@\IDCode = $id]")->get_node(1);
my $imgpath=$ric->findvalue('imgPiatto');
$imgpath = "../images/"+$imgpath; #non so se serve sta cosa ma penso di si cosi sa dove deve lavorare
my $parent = $ric->parentNode;
$parent->removeChild($ric);
unlink $imgpath;
open(OUT,">$file") or die $!;
print OUT $doc->toString;
close(OUT);			
print "Location:console_admin.cgi\n\n";
#Last update by Luca 01/06/2016
