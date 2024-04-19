# create a manifest that kills a process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}
