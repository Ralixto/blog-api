# Blog API

A REST API built with Django REST Framework supporting user authentication,
blog posts, comments, and categories.

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL (production)
- JWT Authentication (simplejwt)

## Live API
Base URL: https://blog-api-sjpc.onrender.com
API Docs: https://blog-api-sjpc.onrender.com/api/docs/

## Running Locally

1. Clone the repo
   git clone https://github.com/Ralixto/blog-api.git
   cd blog-api

2. Create and activate a virtual environment
   python -m venv .venv
   .venv\Scripts\activate  # Windows

3. Install dependencies
   pip install -r requirements.txt

4. Run migrations
   python manage.py migrate

5. Start the server
   python manage.py runserver

## API Endpoints

### Auth
- POST /api/register/
- POST /api/token/
- POST /api/token/refresh/

### Posts
- GET /posts/
- POST /posts/
- GET /posts/{id}/
- PUT /posts/{id}/
- PATCH /posts/{id}/
- DELETE /posts/{id}/

### Comments
- GET /comments/
- POST /comments/
- GET /comments/{id}/
- PUT /comments/{id}/
- PATCH /comments/{id}/
- DELETE /comments/{id}/

### Categories
- GET /category/
- POST /category/
- GET /category/{id}/
- PUT /category/{id}/
- PATCH /category/{id}/
- DELETE /category/{id}/

## API Documentation
Swagger UI available at /api/docs/ after running the server.

## Running Tests
pytest
