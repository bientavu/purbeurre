import pytest

from django.urls import reverse
from products.models import Product


@pytest.mark.django_db
def test_product_view(client):
    product = Product.objects.create(
        name='Test products',
        url='testurl.test',
        image_url='test.testimage.com',
        nutriscore='c',
        fat_100g='0.2',
        satured_fat_100g='0.85',
        sugar_100g='0.4',
        salt_100g='1.2'
    )
    url = reverse('product_detail', kwargs={'product_id': product.id})
    response = client.get(url)
    assert response.status_code == 200
    assert product.name in str(response.content)
    assert product.nutriscore == 'c' in str(response.content)
