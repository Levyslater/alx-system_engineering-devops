# modify the 'wp-settings.php file to remove the typo error
exec { 'fix-wordpress':
  command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',

  path    => ['/usr/local/bin', '/bin', '/usr/bin'],
  onlyif  => 'grep -q "phpp" /var/www/html/wp-settings.php',
}

