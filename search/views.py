from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchResultsView(ListView):
    model = Product
    template_name = 'products/results.html'

    def get_queryset(self):
        return Product.objects.filter(
            Q(name__icontains='Nutella')
        )