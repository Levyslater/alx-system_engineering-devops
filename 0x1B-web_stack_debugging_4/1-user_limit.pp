# Change the OS configuration so that it is possible to login
# with the holberton user and open a file without any error message
exec { 'set file limits for holberton user':
  command => 'echo -e "holberton soft nofile 4096\nholberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => '/usr/bin/env:/bin:/usr/bin:/usr/sbin',
  unless  => 'grep -q "^holberton.*nofile" /etc/security/limits.conf',
}

