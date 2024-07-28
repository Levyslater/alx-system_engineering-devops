#!usr/bin/env bash
# install nginx and configure a custom header response

exec { 'update':
	command => 'sudo apt-get update''
	provider => shell,
}

package { 'nginx':
	ensure => installed,
	require => Exec['update'],
}

file_line { 'headercustom':
	ensure => present,
	path => 'etc/nginx/sites-available/default',
	after => ':80 default_server;',
	line => "add_header X-Served-By ${hostname};",
	require => Package['nginx'],
}

service { 'nginx':
	ensure => running,
	require => file_line['headercustom'],
}
