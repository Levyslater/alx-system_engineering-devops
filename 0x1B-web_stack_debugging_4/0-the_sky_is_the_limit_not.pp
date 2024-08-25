exec { 'modify nginx max open files limit':
  command => 'sed -i "s/^#worker_rlimit_nofile.*/worker_rlimit_nofile 10000;/" /etc/nginx/nginx.conf && systemctl restart nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'grep -q "^#worker_rlimit_nofile" /etc/nginx/nginx.conf',
}
