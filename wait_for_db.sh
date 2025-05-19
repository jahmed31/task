#!/bin/sh

echo "Waiting for postgres database to initiate..."

while ! nc -z $DJANGO_DB_HOST $DJANGO_DB_PORT; do
  sleep 1
done

echo "PostgreSQL Container started"

exec "$@"
