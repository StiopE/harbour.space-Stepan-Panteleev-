# Lecture 07 Exercise

Build and deploy a small REST API using FastAPI and SQL.

Note: if you don't want to use GCP, feel free to use whatever you think is suitable. The only requirement is that api is publicly available and data is stored persistently

## Task

Create an API for one entity of your choice (for example: books, notes, movies, products, pets, events).

Your API must support exactly these 3 operations:

1. Create a new entity record.
2. Get one entity record by ID.
3. List all entity records.

## Technical Requirements

- Framework: FastAPI
- Database: SQL database (store real data in DB, not in-memory)
- Deployment:
  - API deployed to Google Cloud Run
  - Database deployed to Google Cloud SQL
- Verification tool: Postman (better, but optional) or curl

## API Requirements

Use your own entity name, but keep this structure:

- `POST /<entities>`: create a new record
- `GET /<entities>/{id}`: return one record by ID
- `GET /<entities>`: return a list of records

Each record must have at least:

- unique ID
- 2-3 meaningful fields specific to your entity

## What to Submit

- Cloud Run URL of your deployed API
- A short description of your entity and fields
- Postman proof (collection export or screenshots) showing:
  - successful create request
  - successful get-by-id request
  - successful list request

## Definition of Done

- All 3 endpoints work on deployed Cloud Run service.
- Data is saved and read from Cloud SQL.
- Postman checks confirm the full flow end-to-end.

## Don't forget to pause your cloud SQL instance when you are not working on it