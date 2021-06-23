# Generated by Django 3.2.4 on 2021-06-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(help_text='Select a category for this product', related_name='products', to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='fat_100g',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='salt_100g',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='satured_fat_100g',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='suger_100g',
            field=models.FloatField(),
        ),
    ]