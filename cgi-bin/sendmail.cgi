#!/usr/bin/perl -w


use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;
use HTML::Parser;
use HTML::Entities;
use Mail::Sendmail;


my %mail = (
         from => 'sindicarlo@hotmail.it',
         to => 'sindicarlo@hotmail.it',
         subject => 'Test HTML mail',
         'content-type' => 'text/html; charset="iso-8859-1"',
);



sendmail(%mail) || print "Error: $Mail::Sendmail::error\n";

