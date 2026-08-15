import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Post, Category

# Create your tests here.

User = get_user_model()

@pytest.fixture
def category(db):
    return Category.objects.create(name="General", slug="general")

# @pytest.mark.django_db
# def test_unauthenticated_get_posts():
#     client = APIClient()
#     response = client.get("/posts/")
#     assert response.status_code == 200 

# @pytest.mark.django_db
# def test_unauthenticated_post_posts():
#     client = APIClient()
#     response = client.post("/posts/")
#     assert response.status_code == 401

# @pytest.mark.django_db
# def test_authenticated_post_posts(category):
#     user = User.objects.create_user(username='Habi', password='Habib')
#     payload = {
#         "title": "My Post",
#         "content": "Sample content",
#         "category": category.id
#     }  
#     client = APIClient()
#     client.force_authenticate(user=user)
#     response = client.post("/posts/", data=payload)
#     assert response.status_code == 201

# @pytest.mark.django_db
# def test_authenticated_delete_another_user_post(category):
#     user = User.objects.create_user(username='Habi', password='Habib')
#     attacker = User.objects.create_user(username='Habib', password='Habib22')

#     post = Post.objects.create(
#     title="Test", 
#     content="kajsldjlkwa",
#     category=category,
#     author=user,
#     published=True
# )

#     client = APIClient()
#     client.force_authenticate(user=attacker)
#     response = client.delete(f"/posts/{post.id}/")
#     assert response.status_code == 403


@pytest.mark.django_db
def test_authenticated_post_comment(category):
    user = User.objects.create_user(username='Habi', password='Habib')

    post = Post.objects.create(
        title="Test", 
        content="kajsldjlkwa",
        category=category,
        author=user,
        published=True
    )

    payload = {
        "post": post.id,
        "author": user.id,
        "content": "Wow interesting"
    }

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post("/comments/", data=payload, format="json")
    assert response.status_code == 201

@pytest.mark.django_db
def test_unauthenticated_post_comment(category):
    user = User.objects.create_user(username='Habi', password='Habib')

    post = Post.objects.create(
        title="Test", 
        content="kajsldjlkwa",
        category=category,
        author=user,
        published=True
    )

    payload = {
        "post": post.id,
        "author": user.id,
        "content": "Wow interesting"
    }

    client = APIClient()

    response = client.post(f"/comments/{post.id}/", data=payload, format="json")
    assert response.status_code == 401


@pytest.mark.django_db
def test_user_register_api():
    client = APIClient()

    payload = {
        "username": "NewRegisterAPI",
        "email": "newregisterapi@gmail.com",
        "password": "P2kjkssfjk.4d",
        "password2": "P2kjkssfjk.4d",
    }

    response = client.post("/api/register/", data=payload, format="json")
    assert response.status_code == 201

@pytest.mark.django_db
def test_user_register_api_password_mismatch():
    client = APIClient()

    payload = {
        "username": "NewRegisterAPI",
        "email": "newregisterapi@gmail.com",
        "password": "P2kjkssfjk.4d",
        "password2": "P2kjksjk.4d",
    }

    response = client.post("/api/register/", data=payload, format="json")
    assert response.status_code == 400

@pytest.mark.django_db
def test_api_token():
    User.objects.create_user(username='Habi', password='Habib')
    client = APIClient()
    payload = {"username": "Habi", "password": "Habib"}
    response = client.post("/api/token/", data=payload, format="json")
    assert response.status_code == 200
    assert "access" in response.data


@pytest.mark.django_db
def test_unauthenticated_comment_creation(category):
    user = User.objects.create_user(username='Habi', password='Habib')

    post = Post.objects.create(
        title="Test", 
        content="kajsldjlkwa",
        category=category,
        author=user,
        published=True
    )

    payload = {
        "post": post.id,
        "author": user.id,
        "content": "Wow interesting"
    }

    client = APIClient()

    response = client.post("/comments/", data=payload, format="json")
    assert response.status_code == 401

@pytest.mark.django_db
def test_api_token_wrong_password():
    User.objects.create_user(username='Habi', password='Habib')
    client = APIClient()
    payload = {"username": "Habi", "password": "Hab"}
    response = client.post("/api/token/", data=payload, format="json")
    assert response.status_code == 401

@pytest.mark.django_db
def test_auth_edit_own_post(category):
    user = User.objects.create_user(username='Habi', password='Habib')

    post = Post.objects.create(
        title="Test", 
        content="kajsldjlkwa",
        category=category,
        author=user,
        published=True
    )
    
    payload = {
        "title":"Testchango", 
        "content":"kaddjlkwa",
        "category":category.id,
        "published":True
    }

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.put(f"/posts/{post.id}/", data=payload, format="json")
    assert response.status_code == 200

@pytest.mark.django_db
def test_auth_edit_another_post(category):
    user = User.objects.create_user(username='Habi', password='Habi')
    user2 = User.objects.create_user(username='Habi2', password='Habi2')

    post = Post.objects.create(
        title="Test", 
        content="kajsldjlkwa",
        category=category,
        author=user2,
        published=True
    )
    
    payload = {
        "title": "Testcsfdhango", 
        "content": "kaddwewejlkwa",
        "category": category.id,
        "published": False
    }

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.put(f"/posts/{post.id}/", data=payload, format="json")
    print(response.data)
    assert response.status_code == 403