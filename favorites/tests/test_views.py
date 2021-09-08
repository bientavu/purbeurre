import pytest

from favorites.models import Favorite

@pytest.mark.django_db
def test_favorites_view(auto_login_user):
    pass