#!usr/bin/env bash
# install nginx and configure a custom header response

exec { 'http header':
	command  => 'sudo apt-get update -y';
	sudo apt-get install nginx -y;
	sudo sed -i "/server_name _/a add_header X-Served-By HOSTNAME;" /etc/nginx/sites-available/default
	sudo service nginx restart',
	provider => shell,
}

