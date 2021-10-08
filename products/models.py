from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField("category_name", max_length=300, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, help_text='Select a '
                                                            'category for '
                                                            'this product',
                                        related_name='products')
    url = models.CharField(max_length=300)
    image_url = models.CharField(max_length=300, blank=True, null=True)
    nutriscore = models.CharField(max_length=1)
    fat_100g = models.FloatField()
    satured_fat_100g = models.FloatField()
    salt_100g = models.FloatField()
    sugar_100g = models.FloatField()

    def __str__(self):
        return self.name


class DataTableInfos(models.Model):
    date = models.DateTimeField()
