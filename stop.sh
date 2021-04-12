#!/usr/bin/bash

host=192.168.2.2
port=8080
pids=$(ps aux|grep -v 'grep'|grep 'manage.py runserver 192.168.2.2:8080'|awk '{print $2}')
#echo $pids

if test -z "$pids";then
    echo 'No django server is runing.'
else
    echo 'Kill django servers pid ['$pids'].'
    echo $pids|xargs kill -9
fi

#nohup python manage.py runserver $host:$port >> django.log 2>&1 &
#echo 'Reruning django server on '$host':'$port
