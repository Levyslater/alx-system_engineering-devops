exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure   => 'installed',
  require  => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

exec { 'redirect_me':
  command  => 'sed -i "/server_name _;/a \\    rewrite ^/redirect_me$ https://www.google.com permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

exec { 'custom_404_page':
  command  => 'sed -i "/server_name _;/a \\    error_page 404 /404.html;\\n\\n    location /404.html {\\n        internal;\\n    }" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => [Exec['redirect_me'], Exec['custom_404_page']],
}

