#!/usr/bin/env bash

# Host and port to check
host="$1"
shift

# Wait for PostgreSQL to be ready
until nc -z "$host" 5432; do
  echo "Waiting for PostgreSQL at $host..."
  sleep 1
done

# Apply Django migrations
echo "Applying Django migrations..."
python manage.py migrate

# Create the cache table
echo "Creating cache table..."
python manage.py createcachetable

# Execute the provided command (start the server)
exec "$@"
