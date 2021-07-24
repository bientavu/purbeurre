from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category


def products_list(request):
    products = Product.objects.all()[:6]
    return render(request, 'results.html', {'products': products})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'results.html', {'categories': categories})


def product_detail(request, product_id):
    products = Product.objects.all()[:6]
    return render(request, 'results.html', {'products': products})
