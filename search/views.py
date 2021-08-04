from django.contrib import messages
from django.shortcuts import render, redirect
from products.models import Product, Category


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
                name__icontains=searched,
                nutriscore__in=['a', 'b'],
                categories__name__contains=searched_product.categories.first()
            )
            context = {'searched_product': searched_product, 'substitutes_products': substitutes_products}
            return render(request, 'products/results.html', context)
