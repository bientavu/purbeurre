from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product, Category


# class SearchResultsView(ListView):
#     model = Product
#     template_name = 'products/results.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         searched_product = Product.objects.filter(Q(name__icontains=query))
#         return searched_product


# def search_results(request):
#     product_name = request.GET.get('q')
#     searched_product = Product.objects.filter(Q(name__icontains=product_name))
#     return render(request, 'products/results.html', {'searched_product': searched_product})

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched_product = Product.objects.filter(
            name__icontains=searched,
            nutriscore__in=['c', 'd', 'e']
        ).first()
        substitutes_products = Product.objects.filter(
            name__icontains=searched,
            nutriscore__in=['a', 'b'],
            categories__name__contains=searched_product.categories.first()
        )
        context = {'searched_product': searched_product, 'substitutes_products': substitutes_products}
        return render(request, 'products/results.html', context)


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'products/results.html', {'categories': categories})
