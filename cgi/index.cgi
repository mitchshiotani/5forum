#!/usr/bin/perl -w

# use strict;
# use warnings;
use Template;
use DBI;
# use Data::Dumper;

# set up MySQL connection
# get posts data from mySQL
# feed it to template (index.tt)


# setup for MySQL
my $data_source = 'DBI:mysql:5chan:localhost';
open(my $fh, '<', '/var/www/private/creds/creds.txt');
chomp(my $username = <$fh>);
chomp(my $auth = <$fh>);
close $fh;
my $db = DBI->connect($data_source, $username, $auth);

my $statement = <<"END_STRING";
	SELECT
	p.id as id,
	p.title as title,
	p.created_datetime as created_datetime,
	u.username as username
	FROM
	post as p
	JOIN
	user as u
	ON
	p.user_id = u.id
END_STRING
my $post_arr_ref = $db->selectall_hashref($statement, ['id']);

# open the html template
# my $template = HTML::Template->new(filename => '/home/mush/my-website/html/hello.tt');
my $config = {
    INCLUDE_PATH => '/var/www/5chan.com/html',  # or list ref
    #     INCLUDE_PATH => '/home/mush/my-website/html',  # or list ref
    INTERPOLATE  => 1,               # expand "$var" in plain text
    POST_CHOMP   => 1,               # cleanup whitespace
    #     PRE_PROCESS  => 'header',        # prefix each template
    EVAL_PERL    => 1,               # evaluate Perl code blocks
};

# create Template object
my $template = Template->new($config);
my $html_filepath = 'index.tt';
my $passed_vars = {
        post_arr_ref => $post_arr_ref,
};
# print Dumper $post_arr_ref;
print "Content-Type: text/html\n\n";
$template->process($html_filepath, $passed_vars)
    || die $template->error();

# fill in some parameters
# $template->param(HOME => $ENV{HOME});
# $template->param(PATH => $ENV{PATH});

# send the obligatory Content-Type and print the template output
    # print "Content-Type: text/html\n\n", $template->output;
