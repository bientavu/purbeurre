from django.test import TestCase
from products.models import Category, Product
from favorites.models import Favorite


class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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

        Favorite.objects.create(product_to_substitute=Product.objects.get(id=1).id,
                                product_to_substitute_id=Product.objects.get(id=2).id)

    def test_product_to_substitute_related_name(self):
        favorite = Favorite.objects.get(id=1)
        related_name = favorite._meta.get_field('product_to_substitute').related_name
        self.assertEquals(related_name, 'favorites_as_product')
