import pytest

from accounts.models import CustomUser


@pytest.fixture
def auto_login_user(db, client):
    def make_auto_login(user=None):
        if user is None:
            user = CustomUser.objects.create(
                birth_date='1992-05-15',
                email='helloworld@hello.world',
                username='axel',
                password='test'
            )
        client.login(username=user.username, password=user.password)
        return client, user

    return make_auto_login
