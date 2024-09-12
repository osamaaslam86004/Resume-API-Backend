# # Build Stage
# FROM python:3.9-slim AS build

# # Set the working directory in the container
# WORKDIR /app

# # Install netcat (required for waiting for PostgreSQL to be ready)
# RUN apt-get update && apt-get install -y netcat-openbsd

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install dependencies with verbose output and fail on error
# RUN pip install --no-cache-dir -r requirements.txt && \
#     pip show django || { echo 'Django not installed!' ; exit 1; }

# # Copy the entire Django project into the container
# COPY . .

# # Final Stage
# FROM python:3.9-slim

# # Copy only the necessary files from the build stage
# COPY --from=build /app/. .
# COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
# COPY --from=build /usr/local/bin/ /usr/local/bin/

# # Install netcat and pip
# RUN apt-get update && apt-get install -y netcat-openbsd

# # Copy the wait-for-it.sh script into the container and give it executable permissions
# COPY wait-for-it.sh wait-for-it.sh
# RUN chmod +x wait-for-it.sh

# # Set environment variables for Django
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Run migrations and start Django server, ensuring the database is ready using wait-for-it.sh
# CMD ["./wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]

# Build Stage
FROM python:3.9-slim AS build

# Set the working directory in the container
WORKDIR /app

# Install netcat (required for waiting for PostgreSQL to be ready)
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies with verbose output and fail on error
RUN pip install --no-cache-dir -r requirements.txt && \
    pip show django || { echo 'Django not installed!' ; exit 1; }

# Copy the entire Django project into the container
COPY . .

# Final Stage
FROM python:3.9-slim

# Set working directory for final stage
WORKDIR /resume_api_build

# Copy necessary files from the build stage to the resume_api_build folder
COPY --from=build /app/. /resume_api_build/
COPY --from=build /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

# Install netcat and pip (if needed)
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the wait-for-it.sh script into the container and give it executable permissions
COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run migrations and start Django server, ensuring the database is ready using wait-for-it.sh
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
