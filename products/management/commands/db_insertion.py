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
            categorie_insertion = Category(
                name=product['categories']
                )

            categorie_insertion.save()

            product_insertion = Product(
                name=product['product_name'],
                url=product['url'],
                image_url=product['image_url'],
                nutriscore=product['nutriscore_grade'],
                fat_100g=product['fat_100g'],
                satured_fat_100g=product['saturated-fat_100g'],
                salt_100g=product['salt_100g'],
                sugar_100g=product['sugars_100g']
                )
            
            product_insertion.save()
            product_insertion.categories.add(categorie_insertion)






        

        
