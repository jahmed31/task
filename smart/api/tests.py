from datetime import datetime

import pytest

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from app.models import Task

User = get_user_model()


@pytest.mark.django_db
def test_authenticated_user_can_update_task():
    user = User.objects.create_user(email='test@example.com', password='123')
    client = APIClient()
    client.login(email='test@example.com', password='123')
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    task = Task.objects.create(
        title='Updated', description='Updated', status='PENDING',
        user=user, due_date=datetime.now()
    )

    data = {
        'title': 'Updated 123',
        'description': 'Updated 123',
        'status': 'PROGRESS',
        'due_date': datetime.now().strftime('%Y-%m-%d')
    }

    url = f'/api/tasks/{task.id}/'
    response = client.put(url, data=data, format='json')

    assert response.status_code == 202
    assert response.data['title'] == 'Updated 123'


@pytest.mark.django_db
def test_unauthenticated_user_cannot_update_task():
    client = APIClient()

    url = '/api/tasks/1/'
    updated_data = {
        'title': 'Something',
        'description': 'Something',
        'status': 'PROGRESS',
        'due_date': datetime.now().strftime('%Y-%m-%d')
    }

    response = client.put(url, data=updated_data, format='json')

    assert response.status_code == 401


@pytest.mark.django_db
def test_authenticated_user_update_nonexistent_task():
    user = User.objects.create_user(email='test2@example.com', password='123')
    client = APIClient()
    client.login(email='test2@example.com', password='123')
    token = Token.objects.create(user=user)
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    url = '/api/tasks/999/'
    data = {
        'title': 'Something',
        'description': 'Something',
        'status': 'PENDING',
        'due_date': datetime.now().strftime('%Y-%m-%d')
    }

    response = client.put(url, data=data, format='json')

    assert response.status_code == 404
