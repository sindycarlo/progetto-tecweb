#!/usr/bin/perl -w
 
use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use File::Copy;
use utf8;
use URI;
use Email::Valid;


my $to = 'sindycarlo@gmail.com';
my $from = '';
my $subject = 'Test Email';
my $message = '<h1>This is test email sent by Perl Script</h1>';
 
open(MAIL, "|/usr/local/lib/sendmail -t");
 
# Email Header
print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n\n";
print MAIL "Content-type: text/html\n";
# Email Body
print MAIL $message;

close(MAIL);
print "Email Sent Successfully\n";
