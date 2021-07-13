from django.test import TestCase
from products.openfoodfacts import ProductDownloader, ProductCleaner

result = [{'categories': '',
           'fat_100g': 0,
           'image_url': '',
           'nutriscore_grade': 'a',
           'product_name': '',
           'salt_100g': 0,
           'saturated-fat_100g': 0,
           'sugars_100g': 0,
           'url': 'https://fr.openfoodfacts.org/produit/3274080005003/cristaline-eau-de-source'},
          {'categories': 'Produits à tartiner, Petit-déjeuners, Aides culinaires, '
                         'Produits à tartiner sucrés, Aides à la pâtisserie, Pâtes à '
                         'tartiner, Pâtes à tartiner aux noisettes, Pâtes à tartiner au '
                         'chocolat, Pâtes à tartiner aux noisettes et au cacao, Aide '
                         'culinaire sucrée',
           'fat_100g': 30.9,
           'image_url': 'https://static.openfoodfacts.org/images/products/301/762/042/2003/front_fr.270.400.jpg',
           'nutriscore_grade': 'e',
           'product_name': 'Nutella pate a tartiner noisettes-cacao t.400 pot de 400 gr',
           'salt_100g': 0.107,
           'saturated-fat_100g': 10.6,
           'sugars_100g': 56.3,
           'url': 'https://fr.openfoodfacts.org/produit/3017620422003/nutella-pate-a-tartiner-noisettes-cacao-t-400'
                  '-pot-de-400-gr-ferrero '
           }]

correct_removed_result = [{'categories': 'Produits à tartiner, Petit-déjeuners, Aides culinaires, '
                                         'Produits à tartiner sucrés, Aides à la pâtisserie, Pâtes à '
                                         'tartiner, Pâtes à tartiner aux noisettes, Pâtes à tartiner au '
                                         'chocolat, Pâtes à tartiner aux noisettes et au cacao, Aide '
                                         'culinaire sucrée',
                           'fat_100g': 30.9,
                           'image_url': 'https://static.openfoodfacts.org/images/products/301/762/042/2003/front_fr'
                                        '.270.400.jpg',
                           'nutriscore_grade': 'e',
                           'product_name': 'Nutella pate a tartiner noisettes-cacao t.400 pot de 400 gr',
                           'salt_100g': 0.107,
                           'saturated-fat_100g': 10.6,
                           'sugars_100g': 56.3,
                           'url': 'https://fr.openfoodfacts.org/produit/3017620422003/nutella-pate-a-tartiner'
                                  '-noisettes-cacao-t-400-pot-de-400-gr-ferrero '
                           }]


class TestProducts(TestCase):

    def test_products_info_are_valid(self):
        productdownloader = ProductDownloader()
        pass

    def test_empty_values_are_removed(self):
        productcleaner = ProductCleaner()
        test_result = productcleaner.clean(result)
        self.assertContains(correct_removed_result)

    def test_products_info_values_are_cleaned(self):
        productcleaner = ProductCleaner()
        pass