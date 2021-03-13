#!/usr/bin/perl -w

# use strict;
# use warnings;
use Template;
use DBI;
use CGI::Simple;
use Data::Dumper;

# set up MySQL connection
# get posts data from mySQL
# feed it to template (index.tt)

# get CGI params
my $q         = CGI::Simple->new;
my $thread_id = $q->param('thread_id');

# setup for MySQL
my $data_source     = 'DBI:mysql:5chan:localhost';
open(my $fh, '<', '/var/www/private/creds/creds.txt');
chomp(my $username  = <$fh>);
chomp(my $auth      = <$fh>);
close $fh;
my $db = DBI->connect($data_source, $username, $auth);

my $statement = <<"END_STRING";
	SELECT
		p.id as id,
		p.title as title,
		p.content as content,
		p.created_datetime as created_datetime,
		u.username as username
	FROM
		post as p
	JOIN
		user as u
	ON
		p.user_id = u.id
	WHERE
		p.id = ?
	LIMIT
		1
END_STRING

my $sth = $db->prepare($statement);
$sth->execute($thread_id);

my $post_hash_ref = $sth->fetchall_hashref('id');
# print Dumper $post_hash_ref;

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
my $html_filepath = 'view_thread.tt';
my $passed_vars = {
	thread_id     => $thread_id,
        post_hash_ref => $post_hash_ref,
};
# print Dumper $post_hash_ref;
print "Content-Type: text/html\n\n";
$template->process($html_filepath, $passed_vars)
    || die $template->error();

