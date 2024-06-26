#Fixing nginx to serve more requests

exec {'modify ulimit setting':
	command => 'sed -i "s/15/4096/" /etc/default/nginx && sudo service nginx restart',
	path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
}
