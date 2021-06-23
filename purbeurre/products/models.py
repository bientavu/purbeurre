from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, help_text='Select a category for this product', related_name='products')
    url = models.CharField(max_length=300)
    nutriscore = models.CharField(max_length=1)
    fat_100g = models.FloatField()
    satured_fat_100g = models.FloatField()
    salt_100g = models.FloatField()
    suger_100g = models.FloatField()
    
    def __str__(self):
        return self.name