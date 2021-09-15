import pytest
from django.test import Client as DjangoClient
from accounts.models import CustomUser


@pytest.fixture
def user(db):
    """Create a user"""
    user = CustomUser.objects.create_superuser(
        birth_date='1992-05-15',
        email='helloworld@hello.world',
        username='axel',
        password='test'
    )
    return user


@pytest.fixture
def connected_client(user):
    """Log in the user"""
    connected_client = DjangoClient()
    connected_client.force_login(user)
    return connected_client



