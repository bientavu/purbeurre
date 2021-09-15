import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_auth_view(auto_login_user):
    """Test to check if user is logged by checking a 200 status code"""
    client, user = auto_login_user()
    url = reverse('signup')
    response = client.get(url)
    assert response.status_code == 200
