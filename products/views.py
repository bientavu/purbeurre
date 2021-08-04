from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/details.html', {'product': product})
