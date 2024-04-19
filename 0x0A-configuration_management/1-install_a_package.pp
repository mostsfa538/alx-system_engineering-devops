# Install flask
exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
}
