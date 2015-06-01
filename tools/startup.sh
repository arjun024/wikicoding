#! /bin/bash

sudo systemctl enable uwsgi.service
sudo systemctl enable nginx.service
sudo systemctl enable mysqld.service
