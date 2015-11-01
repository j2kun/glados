#!/usr/bin/perl

use File::Copy;
use File::Path qw(mkpath);

my $python = "/usr/bin/python";
my $grader = "glados";
my $graderUID = 1003;

$ENV{"PATH"} = "/usr/bin"; # appease the perl-suid security for shell calls

my $baseDir = "/home/$grader";
my $username = getlogin() or die "Couldn't access user login: $!\n"; 

print "Real user $<, effective user $>\n";

my $assignment = shift or die "No arguments given!\n";
$assignment =~ /([A-Za-z0-9-]+)/g;
$assignment = $1;
my $dir = "$baseDir/submissions/$assignment/$username/";

# check if the project is open
open(PROJECTS, "< $baseDir/open-assignments.txt") or die "Couldn't open assignments file: $!\n";
my %validAssignments = {};
while(<PROJECTS>) {
   chomp;
   $validAssignments{$_} = 1;
}
die "Project name $assignment is invalid or submission is closed.\n" unless $validAssignments{$assignment};
system("clear");
print "Submitting $assignment...\n";

# make the directory for the submission
mkpath($dir, {mode => 0700, owner => $grader, group => $grader, error => my $err});
if (@$err){
  die "Couldn't make submission directory: $err\n"; 
}

foreach (@ARGV) {
   $_ =~ /(.*)/;
   $filename = $1;

   print "Submitting $filename... ";
   copy($filename, $dir) or die "Copy failed for filename $filename: $!\n";
   chmod(0600, "$dir/$filename") or die "Submission failed: unable to change permissions: $!\n"; 
   chown $graderUID, $graderUID, "$dir/$filename";
   print "OK!\n";
}

print "Files Submitted.\n\n";

system("touch $dir/__init__.py");
system("touch $baseDir/log/$username-$assignment.txt");
# system("$python $baseDir/grade.py $username $assignment | tee $baseDir/log/$username-$assignment.txt");
