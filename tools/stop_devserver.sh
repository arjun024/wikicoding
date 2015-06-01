#! /bin/bash

sudo kill -9 `ps aux | grep '[p]ython manage.py' | awk '{print $2}'`
