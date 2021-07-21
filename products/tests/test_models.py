from django.test import TestCase
from products.models import Category, Product


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Pates à tartiner')

    def test_name_label(self):
        category = Category.objects.first()
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'category_name')

    def test_name_max_length(self):
        category = Category.objects.get(name='Pates à tartiner')
        field_label = category._meta.get_field('name').max_length
        self.assertEquals(field_label, 100)


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product_insertion = Product.objects.create(name='Nutella', url='http://helloworld.com',
                                                   image_url='http://helloworld.com/image', nutriscore='b',
                                                   fat_100g=0.2,
                                                   satured_fat_100g=0.5, salt_100g=0.1, sugar_100g=0.8)
        product_insertion.categories.add(Category.objects.create(name='Pates à tartiner'))

    def test_name_max_length(self):
        product = Product.objects.first()
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_categories_help_text_name(self):
        product = Product.objects.first()
        help_text = product._meta.get_field('categories').help_text
        self.assertEquals(help_text, 'Select a category for this product')

    def test_categories_related_name(self):
        product = Product.objects.first()
        related_name = product._meta.get_field('categories').related_name
        self.assertEquals(related_name, 'products')

    def test_url_max_length(self):
        product = Product.objects.first()
        max_length = product._meta.get_field('url').max_length
        self.assertEquals(max_length, 300)

    def test_image_url_blank_is_true(self):
        product = Product.objects.first()
        blank_is_true = product._meta.get_field('image_url').blank
        self.assertTrue(blank_is_true)

    def test_nutriscore_max_length(self):
        product = Product.objects.first()
        max_length = product._meta.get_field('nutriscore').max_length
        self.assertEquals(max_length, 1)
