from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Product
from django.db.models import Q


def search_results(request):
    searched = request.POST['searched']
    if not searched or searched == "":
        messages.error(request, "Veuillez écrire un produit")
        return redirect('home')
    else:
        searched_product = Product.objects.filter(
            name__icontains=searched,
            nutriscore__in=['c', 'd', 'e']
        ).first()
        if searched_product is None:
            messages.error(request, "Désolé nous n'avons pas trouvé ce produit")
            return redirect('home')
        else:
            substitutes_products = Product.objects.filter(
                Q(categories__name__contains=searched_product.categories.all()[0]) |
                Q(categories__name__contains=searched_product.categories.all()[1]),
                nutriscore__in=['a', 'b', 'c'],
            )
            context = {'searched_product': searched_product, 'substitutes_products': substitutes_products}
            return render(request, 'products/results.html', context)
