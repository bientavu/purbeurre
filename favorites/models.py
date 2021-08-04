from django.db import models
from django.conf import settings


class Favorite(models.Model):
    product_to_substitute = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True,
                                              related_name='favorites_as_product')
    substitute_product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True,
                                           related_name='favorites_as_substitute')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='favorites')

    def __str__(self):
        return f'{self.product_to_substitute}, {self.substitute_product}'
