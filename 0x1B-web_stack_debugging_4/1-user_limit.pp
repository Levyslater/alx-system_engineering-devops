exec { 'set file limits for holberton user':
  command => 'echo -e "holberton soft nofile 4096\nholberton hard nofile 8192" >> /etc/security/limits.conf',
  path    => '/usr/bin/env:/bin:/usr/bin:/usr/sbin',
  unless  => 'grep -q "^holberton.*nofile" /etc/security/limits.conf',
}

