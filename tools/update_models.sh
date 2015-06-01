#! /bin/bash

python manage.py schemamigration wiki --auto
python manage.py migrate wiki
