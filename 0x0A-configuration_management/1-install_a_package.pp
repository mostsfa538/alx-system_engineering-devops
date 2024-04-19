# install  Wereug
package { 'Weruge':
    ensure   => '2.1.1',
    provider => 'apt',
}

# Install flask
package { 'flask':
  ensure   => '2.1.1',
  provider => 'pip3',
}
