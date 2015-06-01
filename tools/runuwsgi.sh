#! /bin/bash

uwsgi --socket wikicoding.sock --chdir /wikicoding --module wikicoding.wsgi --uid nginx --gid nginx --chown-socket nginx:nginx --enable-threads --single-interpreter --logto /wikicoding/log/uwsgi.log
