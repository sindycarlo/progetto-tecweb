#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;

my $session = CGI::Session->load() or die $!;
$session->delete();
print "Location: menu.cgi\n\n";
#Last Update by Luca e Carlo 07/06/2016
