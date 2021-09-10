from django.test import TestCase
from products.models import Category, Product
from favorites.models import Favorite
from accounts.models import CustomUser


class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(
            birth_date='1992-05-15',
            email='helloworld@hello.world',
            username='axel'
        )
        product_insertion = Product.objects.create(
            name='Nutella',
            url='http://helloworld.com',
            image_url='http://helloworld.com/image',
            nutriscore='b',
            fat_100g=0.2,
            satured_fat_100g=0.5,
            salt_100g=0.1,
            sugar_100g=0.8
        )
        product_insertion.categories.add(
            Category.objects.create(name='Pates à tartiner')
        )
        product_insertion_2 = Product.objects.create(
            name='Compote de pomme',
            url='http://helloworld2.com',
            image_url='http://helloworld.com/image2',
            nutriscore='a',
            fat_100g=0.1,
            satured_fat_100g=0.4,
            salt_100g=0.1,
            sugar_100g=0.3
        )
        product_insertion_2.categories.add(
            Category.objects.create(name='Compote')
        )

        p1 = Product.objects.get(id=1)
        p2 = Product.objects.get(id=2)

        Favorite.objects.create(product_to_substitute=p1,
                                substitute_product=p2,
                                user=user)

    def test_product_to_substitute_null_is_true(self):
        favorite = Favorite.objects.get(id=1)
        null = favorite._meta.get_field('product_to_substitute').null
        self.assertTrue(null)

    def test_substitute_product_null_is_true(self):
        favorite = Favorite.objects.get(id=1)
        null = favorite._meta.get_field('substitute_product').null
        self.assertTrue(null)

    def test_product_to_substitute_related_name(self):
        favorite = Favorite.objects.get(id=1)
        related_name = favorite._meta.get_field(
            'product_to_substitute'
        ).remote_field.get_accessor_name()
        self.assertEquals(related_name, 'favorites_as_product')

    def test_substitute_product_related_name(self):
        favorite = Favorite.objects.get(id=1)
        related_name = favorite._meta.get_field(
            'substitute_product'
        ).remote_field.get_accessor_name()
        self.assertEquals(related_name, 'favorites_as_substitute')
