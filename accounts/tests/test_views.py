import pytest
from accounts.models import CustomUser
from django.urls import reverse


@pytest.mark.django_db
def test_auth_view(client):
    user = CustomUser.objects.create(
        birth_date='1992-05-15',
        email='helloworld@hello.world',
        username='axel',
        password='test')
    url = reverse('signup')
    client.login(
        username=user.username, password=user.password
    )
    response = client.get(url)
    assert response.status_code == 200
