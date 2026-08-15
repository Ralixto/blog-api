This is a Blog API that uses Django and more specifically, the Django Rest Framework(DRF).
Tech Stack: Python, Django
To run it locally, clone, install the appropriate dependencies, including: 

asgiref==3.11.1
attrs==26.1.0
colorama==0.4.6
Django==6.0.6
django-filter==26.1
djangorestframework==3.17.1
djangorestframework_simplejwt==5.5.1
drf-spectacular==0.30.0
inflection==0.5.1
iniconfig==2.3.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
packaging==26.3
pluggy==1.6.0
Pygments==2.20.0
PyJWT==2.13.0
pytest==9.1.1
pytest-django==4.14.0
PyYAML==6.0.3
referencing==0.37.0
rpds-py==2026.6.3
sqlparse==0.5.5
tzdata==2026.2
uritemplate==4.2.0

Migrate, and then run the server.
All API Endpoints:

POST
/api/register/

POST
/api/token/

POST
/api/token/refresh/

category

GET
/category/

POST
/category/

GET
/category/{id}/

PUT
/category/{id}/

PATCH
/category/{id}/

DELETE
/category/{id}/

comments

GET
/comments/

POST
/comments/

GET
/comments/{id}/

PUT
/comments/{id}/

PATCH
/comments/{id}/

DELETE
/comments/{id}/

posts
GET
/posts/

POST
/posts/

GET
/posts/{id}/

PUT
/posts/{id}/

PATCH
/posts/{id}/

DELETE
/posts/{id}/

Swagger Docs Link : /api/docs/
