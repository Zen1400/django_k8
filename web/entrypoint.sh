#!/bin/bash
APP_PORT=${APP_PORT:-8000}
cd /app/
gunicorn --worker-tmp-dir /dev/shm django_k8.wsgi:application --bind "0.0.0.0:${APP_PORT}"
