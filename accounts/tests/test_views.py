import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_auth_view(connected_client, user):
    """Test to check if user is logged by checking a 200 status code"""
    url = reverse('signup')
    response = connected_client.get(url)
    assert response.status_code == 200
