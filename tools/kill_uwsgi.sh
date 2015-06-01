#! /bin/bash

sudo kill -9 `ps aux | grep [u]wsgi | awk 'FNR == 2 {print $2}'`
