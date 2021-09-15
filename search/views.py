from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from favorites.models import Favorite
from products.models import Product


# @login_required
def search_results(request):
    favorites = Favorite.objects.filter(user=request.user)
    searched = request.POST.get('searched')
    if not searched or searched == "":
        messages.error(request, "Veuillez écrire un produit")
        return redirect('home')
    else:
        searched_product = Product.objects.filter(
            name__icontains=searched,
            nutriscore__in=['d', 'e']
        ).first()
        if searched_product is None:
            messages.error(
                request,
                "Désolé nous n'avons pas trouvé ce produit"
            )
            return redirect('home')
        else:
            categories_list = searched_product.categories.all()[:2]
            substitutes_products = Product.objects.filter(
                categories__in=categories_list,
                nutriscore__in=['a', 'b', 'c'],
            )
            context = {'searched_product': searched_product,
                       'substitutes_products': substitutes_products,
                       'favorites': [
                           prod.substitute_product for prod in favorites
                       ]}
            return render(request, 'products/results.html', context)
