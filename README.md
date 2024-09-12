# Resume API

## Overview

The Resume API provides a platform for users to create and manage their resumes. It supports account creation, issues JWT tokens needed for resume management, and enforces a throttling limit of 200 requests per day for all user types. Users can create, update, and delete their resumes through this API.

**Note:** JWT tokens are not deleted or blacklisted by the API unless they expire, which may impact user sessions.

## Getting Started

Follow these instructions to set up and run the API:

### Prerequisites

- Python 3.11
- Django 4.2.8

### Installation

1. **Install Dependencies:**

   ```bash
   python -m pip install -r requirements.txt
   ```

optional: python manage.py flush
optional: python manage.py reset_db
optional: python manage.py clean_pyc
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable


### Running the API Using Docker

To build and start the API using Docker, follow these steps:

1. **Build and Start the Containers:**

   ```bash
   docker-compose up --build
   ```

Visit the API at http://localhost:8000/.