from django.test import TestCase
from products.models import Category, Product


class CategoryModelTest(TestCase):
    """Multiple tests for Category models"""
    @classmethod
    def setUpTestData(cls):
        """Data setup by creating a category"""
        Category.objects.create(name='Pates à tartiner')

    def test_name_label(self):
        """Check if verbose_name is category_name"""
        category = Category.objects.first()
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'category_name')

    def test_name_max_length(self):
        """Check if max_length is 300"""
        category = Category.objects.get(name='Pates à tartiner')
        field_label = category._meta.get_field('name').max_length
        self.assertEqual(field_label, 300)


class ProductModelTest(TestCase):
    """Multiple tests for Product models"""
    @classmethod
    def setUpTestData(cls):
        """Data setup by creating a product and his category"""
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

    def test_name_max_length(self):
        """Check if max_length is 200"""
        product = Product.objects.first()
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_categories_help_text_name(self):
        """
        Check if categories help_text is 'Select a category for this product'
        """
        product = Product.objects.first()
        help_text = product._meta.get_field('categories').help_text
        self.assertEqual(help_text, 'Select a category for this product')

    def test_categories_related_name(self):
        """Check if the categories related_name is 'products'"""
        product = Product.objects.first()
        related_name = product._meta.get_field(
            'categories'
        ).remote_field.get_accessor_name()
        self.assertEqual(related_name, 'products')

    def test_url_max_length(self):
        """Check if url max_length is 300"""
        product = Product.objects.first()
        max_length = product._meta.get_field('url').max_length
        self.assertEqual(max_length, 300)

    def test_image_url_blank_is_true(self):
        """Check if image_url can be blank"""
        product = Product.objects.first()
        blank_is_true = product._meta.get_field('image_url').blank
        self.assertTrue(blank_is_true)

    def test_nutriscore_max_length(self):
        """Check if nutriscore max_length is 1"""
        product = Product.objects.first()
        max_length = product._meta.get_field('nutriscore').max_length
        self.assertEqual(max_length, 1)
