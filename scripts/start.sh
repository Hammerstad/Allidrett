#! /usr/bin/env sh

IPADDRESS=$(ifconfig eth0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' | awk '{print $1}')

if [ -z $IPADDRESS ]; then
	exec gunicorn allidrett.wsgi -b 0.0.0.0:80
else	
	exec gunicorn allidrett.wsgi -b $(IPADDRESS):80
fi