from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category
from products.openfoodfacts import ProductCleaner, ProductDownloader


class Command(BaseCommand):
    help = 'Add the products to the database'

    def handle(self, *args, **options):
        products = ProductDownloader()
        cleaner = ProductCleaner()
        products_dict = products.get_products_info()
        cleaned_products = cleaner.clean(products_dict)

        for product in cleaned_products:

            categories = [p.strip() for p in product['categories'].split(',')]

            if len(categories) > 1:
                product_insertion, _ = Product.objects.get_or_create(
                    name=product['product_name'],
                    url=product['url'],
                    image_url=product['image_url'],
                    nutriscore=product['nutriscore_grade'],
                    fat_100g=product['fat_100g'],
                    satured_fat_100g=product['saturated-fat_100g'],
                    salt_100g=product['salt_100g'],
                    sugar_100g=product['sugars_100g']
                )

                for category_name in categories[:2]:
                    categories_insertion, _ = Category.objects.get_or_create(name=category_name[:99])
                    product_insertion.categories.add(categories_insertion)

        Product.objects.filter(id=1).delete()
