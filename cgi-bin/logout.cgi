#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;


	#controllo se la sessione esiste già:
	my $session = CGI::Session->load() or die $!;
	
	#elimino la sessione:
	  $session->delete();
	  
	  print "Location: menu.cgi\n\n";
