#This file installs flask using puppet

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin:/bin',
  environment => ['PATH=/usr/local/bin:/usr/bin:/bin'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
