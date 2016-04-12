#!/usr/bin/perl -w

# file che controlla l'accesso utente
# carico le librerie
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
use XML::LibXML;
use File::Copy;
use URI;
#lascio a te luca il percorso della vita di questo file.