#  we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password

file { '/etc/ssh/sshd_config':
  ensure => file,
}

file { '/etc/ssh/config':
  ensure => file,
}

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/etc/ssh/config',
  line => 'IdentityFile ~/.ssh/school',
}
