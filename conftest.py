import pytest
from django.test import Client as DjangoClient
from accounts.models import CustomUser


# @pytest.fixture
# def auto_login_user(db):
#     user, _ = CustomUser.objects.get_or_create(
#         birth_date='1992-05-15',
#         email='helloworld@hello.world',
#         username='axel',
#         password='test'
#     )
#     Client.login(username=user.username, password=user.password)
#     return Client, user


@pytest.fixture
def connected_client(user):
    connected_client = DjangoClient()
    connected_client.login(
        username=user.username, password='test'
    )
    return connected_client


@pytest.fixture
def user(db):
    user = CustomUser.objects.create_superuser(
        # birth_date='1992-05-15',
        email='helloworld@hello.world',
        username='axel',
        password='test'
    )
    return user
