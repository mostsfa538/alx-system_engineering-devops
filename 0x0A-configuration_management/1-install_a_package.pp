# Install flask
package { 'flask':
ensure   => '2.1.1',
name     => 'flask',
provider => 'pip3',
}
