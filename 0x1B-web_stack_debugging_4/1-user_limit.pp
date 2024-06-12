# change the unlimit of a user

exec { 'modify-holberton-hard':
  command => 'sed -i "/^holberton hard/s/5/100000/" /etc/security/limits.conf',
  path    => ['/usr/bin/', '/bin/']
}

exec { 'modify-holberton-soft':
  command => 'sed -i "/^holberton soft/s/4/100000/" /etc/security/limits.conf',
  path    => ['/usr/bin/', '/bin/']
}
