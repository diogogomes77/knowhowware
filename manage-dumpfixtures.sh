#!/bin/sh
docker-compose exec django python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission -e admin.logentry --indent 4 > local_$(date +%d%m%Y).json