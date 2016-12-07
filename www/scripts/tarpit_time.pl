#!/usr/bin/perl
use strict;
use Tie::File;

my @sa_exim;
tie @sa_exim, 'Tie::File',"/etc/exim4/sa-exim.conf";
my $size_sa_exim = @sa_exim;
my $arg;

$arg = $ARGV[0];
do{
        for(my $i=0; $i <= $size_sa_exim; $i++){
                if($sa_exim[$i] =~ "SAteergrubetime:"){
                        $sa_exim[$i] = "SAteergrubetime: $arg";
                        print "Le temps a été modifié \n";
                }
        }
}
