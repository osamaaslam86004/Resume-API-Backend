#!/usr/bin/env bash
host="$1"
shift
until nc -z "$host" 5432; do
  echo "Waiting for PostgreSQL at $host..."
  sleep 1
done
exec "$@"
