import pytest

from django.urls import reverse
from products.models import Product
from favorites.models import Favorite


@pytest.mark.django_db
def test_search_view(auto_login_user):
    product_1 = Product.objects.create(
        name='Test products',
        url='testurl.test',
        image_url='test.testimage.com',
        nutriscore='d',
        fat_100g='0.2',
        satured_fat_100g='0.85',
        sugar_100g='0.4',
        salt_100g='1.2'
    )
    product_2 = Product.objects.create(
        name='Test_products_2',
        url='testurl2.test2',
        image_url='test2.testimage2.com',
        nutriscore='d',
        fat_100g='0.4',
        satured_fat_100g='0.9',
        sugar_100g='1.4',
        salt_100g='1.5'
    )
    client, user = auto_login_user()
    favorites = Favorite.objects.create(
        product_to_substitute_id='1',
        substitute_product_id='2',
        user_id='1'
    )
    data = {'searched': 'products_2'}
    url = reverse('search_results')
    response = client.post(url, data)
    assert response.status_code == 200
    assert product_2.name in str(response.content)
    assert favorites.product_to_substitute_id in str(response.content)
    assert product_2.name in str(response.content)
    assert product_2.image_url in str(response.content)
