from django.test import TestCase
from products.models import Category, Product


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Pates à tartiner')

    def test_name_label(self):
        category = Category.objects.get(id=1)
