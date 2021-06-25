from django.core.management.base import BaseCommand, CommandError
from purbeurre.products.models import Product
from purbeurre.products.openfoodfacts import ProductCleaner, ProductDownloader

class Command(BaseCommand):
    help = 'Add the products to the database'

    def handle(self, ):
        products = ProductDownloader()
        cleaner = ProductCleaner()
        products_dict = products.get_products_info()
        cleaned_products = cleaner.clean(products_dict)

        for product in cleaned_products:
            insertion = Product(
                name=product['product_name'],
                url=product['url'],
                image_url=product['image_url'],
                nutriscore=product['nutriscore'],
                fat_100g=product['fat_100g'],
                satured_fat_100g=product['saturated-fat_100g'],
                salt_100g=product['salt_100g'],
                sugar_100g=product['sugar_100g']
                )
            
            insertion.save()

        
