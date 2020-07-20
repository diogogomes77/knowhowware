#!/bin/sh
docker-compose exec django python manage.py graph_models kww_app -o class_diagram_$(date +%d%m%Y).png
