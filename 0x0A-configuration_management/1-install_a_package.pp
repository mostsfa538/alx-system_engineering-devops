# Install flask
exec { 'flask':
  ensure   => '2.1.0',
  path     => '/usr/local/bin:/usr/bin:/bin',
  provider => 'pip3',
}
