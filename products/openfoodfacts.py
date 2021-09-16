import requests


class ProductDownloader:
    """Download all the information for the products"""
    def get_products_info(self):
        """
        Gets all the products information from the
        openfoodfacts API and put them in a list
        """
        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        number_of_pages = 8
        page_size = 1000

        products = []

        for page_number in range(1, number_of_pages + 1):
            params = {
                "action": "process",
                "sort_by": "unique_scans_n",
                "page_size": page_size,
                "page": page_number,
                "fields": "product_name,url,nutriscore_grade,categories,fat_100g,saturated-fat_100g,salt_100g,sugars_100g,image_url",
                "json": True,
            }

            response = requests.get(url, params=params)
            products.extend(response.json()["products"])

        return products


class ProductCleaner:
    """
    Cleans the list that has been downloaded by
    the method get_products_info
    """
    def remove_empty_values(self, product):
        """Removes all the empty values from the list"""
        res = {key: val for key, val in product.items() if val}
        return res

    def clean(self, products):
        """
        Add all the cleaned products to a new list only if
        length is 9, name length under 100
        """
        cleaned_products = []

        for product in products:
            product = self.remove_empty_values(product)
            if (
                    len(product) == 9
                    and len(product['product_name']) < 100
            ):
                cleaned_products.append(product)

        return cleaned_products
