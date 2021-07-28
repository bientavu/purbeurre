from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category


def products_list(request):
    products = Product.objects.all()[:6]
    return render(request, 'products/results.html', {'products': products})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'products/results.html', {'categories': categories})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/details.html', {'product': product})
