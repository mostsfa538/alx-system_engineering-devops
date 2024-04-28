# configure web-02 to be identical to web-01 with puppet

package { 'nginx':
  ensure => installed,
}

firewall { 'Allow Nginx HTTP':
  port   => 80,
  proto  => 'tcp',
  action => 'accept',
}
nginx::resource::server { 'default':
  listen_port => '80',
  locations   => {
    '/' => {
      'add_header' => 'X-Served-By $hostname',
    },
    '= /custom_404.html' => {
      'root'      => '/usr/share/nginx/html',
      'add_header'=> 'X-Served-By $hostname',
      'internal'  => true,
    },
  },
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => "Hello World!\n",
}

file { '/usr/share/nginx/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",

