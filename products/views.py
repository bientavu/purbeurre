from django.shortcuts import render
from products.models import Product, Category


def products_list(request):
    products = Product.objects.get(id=1)
    return render(request, 'results.html', {'products': products})

