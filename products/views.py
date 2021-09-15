from django.shortcuts import render
from products.models import Product


def product_detail(request, product_id):
    """
    Method that gets the product in the DB via his id
    and then inject it into the product detail HTML page
    """
    product = Product.objects.get(id=product_id)
    return render(request, 'products/details.html', {'product': product})
