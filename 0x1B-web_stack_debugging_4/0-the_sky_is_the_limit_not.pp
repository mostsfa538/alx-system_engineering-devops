# chagne the unlimit of nginx

exec { 'fix-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/bin/', '/bin/']
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
}
