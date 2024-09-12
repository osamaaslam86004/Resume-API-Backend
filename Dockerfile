# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install netcat
# Ensuring that the Django API server waits for the PostgreSQL
#  container to be fully up and ready before trying to run 
#  database-dependent operations (like migrations or starting the server).
RUN apt-get update && apt-get install -y netcat-openbsd


# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the wait-for-it.sh script into the container and give it executable permissions
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Copy the entire Django project into the container
COPY . .

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run migrations and start Django server, ensuring the database is ready using wait-for-it.sh
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
