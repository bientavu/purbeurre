import pytest

from django.urls import reverse
from products.models import Product, Category
from favorites.models import Favorite

@pytest.mark.django_db
def test_favorites_view(auto_login_user):
    client, user = auto_login_user()
    product_insertion = Product.objects.create(name='Nutella', url='http://helloworld.com',
                                               image_url='http://helloworld.com/image', nutriscore='b',
                                               fat_100g=0.2,
                                               satured_fat_100g=0.5, salt_100g=0.1, sugar_100g=0.8)
    product_insertion.categories.add(Category.objects.create(name='Pates à tartiner'))
    product_insertion_2 = Product.objects.create(name='Compote de pomme', url='http://helloworld2.com',
                                                 image_url='http://helloworld.com/image2', nutriscore='a',
                                                 fat_100g=0.1,
                                                 satured_fat_100g=0.4, salt_100g=0.1, sugar_100g=0.3)
    product_insertion_2.categories.add(Category.objects.create(name='Compote'))

    p1 = Product.objects.get(id=1)
    p2 = Product.objects.get(id=2)

    Favorite.objects.create(product_to_substitute=p1,
                            substitute_product=p2,
                            user=user)
    url = reverse('favorites')
    response = client.get(url)
    assert response.status_code == 200
    assert p1.name in str(response.content)
    assert p1.nutriscore == 'c' in str(response.content)
    assert p1.sugar_100g in str(response.content)
