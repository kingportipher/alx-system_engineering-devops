#This is a file that kills a process in puppet

exec { 'kill_killmenow':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
}
