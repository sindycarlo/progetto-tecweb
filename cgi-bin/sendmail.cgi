




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




use CGI;
my $q = new CGI;

my $sendmailpath = "/usr/lib/sendmail";
my $myemail = "sindycarlo\@gmail.com";
my $name = $q->param("name");
my $email = $q->param("email");
my $message = $q->param("question");





open(MAIL, "| $sendmailpath -t");

print MAIL "To: $myemail\n";
print MAIL "Reply: $email\n";
print MAIL "Subject:Webmail $name\n\n";
print MAIL "$message";
close MAIL; 

