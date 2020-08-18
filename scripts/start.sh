#! /usr/bin/env sh

IPADDRESS=$(shell ifconfig eth0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1' | awk '{print $1}')

ifndef IPADDRESS
	exec gunicorn allidrett.wsgi -b 0.0.0.0:8000
else	
	exec gunicorn allidrett.wsgi -b $(IPADDRESS):8000
endif