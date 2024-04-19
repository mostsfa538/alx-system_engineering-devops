# install  Wereug
package { 'Weruge':
    ensure   => '2.1.1',
    provider => 'apt',
}

# Install flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
