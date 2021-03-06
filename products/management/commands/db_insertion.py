from django.core.management.base import BaseCommand
from products.models import Product, Category, DataTableInfos, Keywords, \
    Ingredients
from products.openfoodfacts import ProductCleaner, ProductDownloader
from django.utils import timezone


class Command(BaseCommand):
    help = 'Add the products to the database'

    def handle(self, *args, **options):
        """
        Method to initialize the database. It calls the openfoodfacts API
        to get all the products informations then add them into the DB
        """
        products = ProductDownloader()
        cleaner = ProductCleaner()
        products_dict = products.get_products_info()
        cleaned_products = cleaner.clean(products_dict)

        for product in cleaned_products:

            categories = [p.strip() for p in product['categories'].split(',')]
            keywords = [p for p in product['_keywords']]
            ingredients = [p for p in product['ingredients_original_tags']]

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
                categories_insertion, _ = Category.objects.get_or_create(
                    name=category_name[:99]
                )
                product_insertion.categories.add(categories_insertion)

            for keyword_name in keywords:
                keywords_insertion, _ = Keywords.objects.get_or_create(
                    name=keyword_name[:99]
                )
                product_insertion.keywords.add(keywords_insertion)

            for ingredient_name in ingredients:
                ingredients_insertion, _ = Ingredients.objects.get_or_create(
                    name=ingredient_name[:99]
                )
                product_insertion.ingredients.add(ingredients_insertion)

        Product.objects.filter(id=1).delete()

        DataTableInfos.objects.create(date=timezone.now())
