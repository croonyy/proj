#!/usr/bin/bash

host=192.168.2.2
port=8080
pids=$(ps aux|grep -v 'grep'|grep 'manage.py runserver 192.168.2.2:8080'|awk '{print $2}')
#echo $pids

echo '********************************************************'
. /home/croonyy/django/webpy36/py36env/bin/activate
echo 'activate python env'
echo `python --version`

if test -z "$pids";then
    echo 'No django server is runing.'
else
    echo 'Kill django servers pid ['$pids'].'
    echo $pids|xargs kill -9
fi

nohup python /home/croonyy/django/webpy36/proj/manage.py runserver $host:$port > /home/croonyy/django/webpy36/proj/django.log 2>&1 &
echo 'Reruning django server on '$host':'$port

deactivate
echo '********************************************************'
