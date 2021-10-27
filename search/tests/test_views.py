import pytest

from django.urls import reverse
from products.models import Product
from favorites.models import Favorite


@pytest.mark.django_db
def test_search_view(connected_client, user, products_creation):
    """
    Test the search view by creating products and favorites
    Then we test the response.content to check if we have
    the informations we need (product name, status code, etc)
    """
    product_1, product_2 = products_creation
    favorites, _ = Favorite.objects.get_or_create(
        product_to_substitute_id=product_1.id,
        substitute_product_id=product_2.id,
        user_id=user.id
    )
    data = {'searched': product_2}
    url = reverse('search_results')
    response = connected_client.get(url, data)
    assert response.status_code == 200
    assert product_2.name in str(response.content)
    assert str(favorites.product_to_substitute_id) in str(response.content)
    assert product_2.name in str(response.content)
    assert product_2.image_url in str(response.content)
