import pytest

from django.urls import reverse
from products.models import Product, Category
from favorites.models import Favorite


@pytest.mark.django_db
def test_favorites_view(connected_client, user):
    """
    Test the favorite view where we create products, categories
    and a favorite. Then we check if we have the proper information
    in the response.content
    """
    product_insertion, _ = Product.objects.get_or_create(
        name='Nutella',
        url='http://helloworld.com',
        image_url='http://helloworld.com/image',
        nutriscore='b',
        fat_100g=0.2,
        satured_fat_100g=0.5,
        salt_100g=0.1,
        sugar_100g=0.8
    )
    cat, _ = Category.objects.get_or_create(name='Pates à tartiner')
    product_insertion.categories.add(cat)

    product_insertion_2, _ = Product.objects.get_or_create(
        name='Compote de pomme',
        url='http://helloworld2.com',
        image_url='http://helloworld.com/image2',
        nutriscore='a',
        fat_100g=0.1,
        satured_fat_100g=0.4,
        salt_100g=0.1,
        sugar_100g=0.3
    )
    cat1, _ = Category.objects.get_or_create(name='Compote')
    product_insertion_2.categories.add(cat1)

    p1 = Product.objects.get(id=product_insertion.id)
    p2 = Product.objects.get(id=product_insertion_2.id)

    Favorite.objects.get_or_create(product_to_substitute=p2,
                                   substitute_product=p1,
                                   user=user)
    url = reverse('favorites')
    response = connected_client.get(url)

    assert response.status_code == 200
    assert p1.name in str(response.content)
    assert p1.nutriscore == 'b' in str(response.content)
