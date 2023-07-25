Project Setup

Step 1: Start PostgreSQL with Docker

Before running the FastAPI application, set up a PostgreSQL database using Docker. Run the following command:

```bash
docker-compose -f docker-compose-local.yaml up -d


Step 2: Initialize Migrations with Alembic

Alembic is used for managing database migrations. To initialize Alembic for your FastAPI application, run:

```bash
alembic init migrations


Step 3: Create a New Migration

Open alembic.ini in the migrations directory. Configure the database connection URL under [alembic] by replacing sqlalchemy.url with your actual database connection URL.
Locate the versions folder inside the migrations directory. You'll find a new Python script named like some_random_string_comment.py. This script represents the base (initial migration
Open the Python script and add necessary database schema changes in the upgrade() function using SQLAlchemy ORM.
Generate an automatic migration with a comment using:

```bash
alembic revision --autogenerate -m 'your_comment_here'

Step 4: Apply the Migration
Apply the migration to the database with:

```bash
alembic upgrade head

Step 5: Running the FastAPI Application
uvicorn main:app --reload

Environment Configuration:
.env-local
settings.py