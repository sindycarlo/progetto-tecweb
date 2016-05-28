#!/usr/bin/perl -w

use HTML::Parser;
use HTML::Entities;
use utf8;
sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

sub traduci() {
	my $string = shift;
  	$string = encode_entities($string, '<>&"');
	$string = encode_entities($string);
	return $string;
}

1;
