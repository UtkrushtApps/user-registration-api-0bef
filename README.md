# User Registration API

## Task Overview

A new user onboarding service for a growing SaaS platform is experiencing operational issues, as duplicate accounts are being created with the same email address. This has led to confusion in the user base and administrative overhead due to multiple accounts per person. Your task is to build a FastAPI backend that allows users to register and ensures each email address is unique, leveraging both API validation and PostgreSQL constraints to enforce this business rule. The application must provide clear feedback to users attempting to register with an email that already exists, and allow administrators to view a list of all registered users.

## Guidance

- The project should follow modular FastAPI architecture, separating routers, models, services, and database logic for maintainability.
- Use SQLAlchemy (async mode) for ORM-based PostgreSQL integration and Pydantic for input validation.
- Ensure proper database indexing and uniqueness enforcement on the email field using migrations.
- Implement error handling that returns clear, user-friendly messages for duplicate registration attempts.
- All database credentials and secrets should be provided via environment variables for portability and security.
- Provide OpenAPI documentation by leveraging FastAPI features.
- Containerize the application using Docker and orchestrate both the API and PostgreSQL services using Docker Compose.

## Objectives

- Implement an endpoint to register new users with name, email, and password, validating input with Pydantic models.
- Prevent duplicate registrations by enforcing email uniqueness at both the database and API layers.
- Provide an endpoint to list all registered users (excluding passwords from responses).
- Handle errors gracefully and return appropriate HTTP status codes for invalid operations.
- Use async database operations throughout.
- Organize the codebase into routers, services, models, and core configuration modules.
- Ensure the project is fully containerized and runs both API and database services together.

## How to Verify

- Registering a user with a unique email should succeed and return the user data (excluding password).
- Attempting to register a second user with the same email must return a clear error message and the appropriate HTTP status code without creating a duplicate record.
- Listing users should display all registered users without revealing password information.
- The OpenAPI documentation should accurately describe the endpoints and models.
- The application should function correctly when started via Docker Compose, with both services healthy.
