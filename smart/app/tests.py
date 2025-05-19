from datetime import datetime

from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model

import pytest

from app.models import Task


User = get_user_model()


@pytest.mark.django_db
def test_task_create_view():
    user = User.objects.create_user(email='test@example.com', password='123')
    client = Client()
    client.login(email='test@example.com', password='123')

    url = reverse('task_create')
    data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'status': 'PENDING',
        'due_date': datetime.now().strftime('%Y-%m-%d'),
    }

    response = client.post(url, data)

    assert response.status_code == 302
    assert Task.objects.filter(title='Test Task', user=user).exists() is True
