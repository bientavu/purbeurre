from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from favorites.models import Favorite
from products.models import Product


@login_required
def search_results(request):
    """
    This is the search method that allows to display the product the user
    has searched for and then all the substitutes products that are attached
    to the searched product
    """
    favorites = Favorite.objects.filter(user=request.user)
    searched = request.GET.get('searched')
    if not searched or searched == "":
        messages.error(request, "Veuillez écrire un produit")
        return redirect('home')
    else:
        searched_product = Product.objects.filter(
            name__icontains=searched,
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

            new_substitutes_products = set()
            keywords_ingredients_comparaison(new_substitutes_products,
                                             searched_product,
                                             substitutes_products,
                                             True)

            if not new_substitutes_products:
                keywords_ingredients_comparaison(new_substitutes_products,
                                                 searched_product,
                                                 substitutes_products,
                                                 False)

            context = {'searched_product': searched_product,
                       'substitutes_products': new_substitutes_products,
                       'favorites': [
                           prod.substitute_product for prod in favorites
                       ]}
            return render(request, 'products/results.html', context)


def keywords_ingredients_comparaison(new_substitutes_products,
                                     searched_product,
                                     substitutes_products,
                                     associate=True):
    for substitute in substitutes_products:

        searched_product_keywords = searched_product.keywords.all()
        substitute_keywords = substitute.keywords.all()
        same_keywords = searched_product_keywords.intersection(
            substitute_keywords)

        searched_product_ingredients = searched_product.ingredients.all()
        substitute_ingredients = substitute.ingredients.all()
        same_ingredients = searched_product_ingredients.intersection(
            substitute_ingredients)

        if associate:
            if same_keywords.count() >= 5 and same_ingredients.count() >= 4:
                new_substitutes_products.add(substitute)

        else:
            if same_keywords.count() >= 5 or same_ingredients.count() >= 4:
                new_substitutes_products.add(substitute)


def home(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(name__icontains=request.GET.get('term'))
        names = list()
        for product in qs:
            names.append(product.name)
        return JsonResponse(names, safe=False)
    return render(request, 'home.html')
