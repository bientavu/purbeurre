from django.shortcuts import render, get_object_or_404
from favorites.models import Favorite
from django.http import HttpResponse
from products.models import Product


def import_favorites(request):
    favorites = Favorite.objects.all()
    favorites_unique = list(set(favorites))
    products = Product.objects.all()
    context = {'favorites': favorites,
               'products': products}
    return render(request, 'favorites/favorites.html', context)


def add_favorites(request):
    product_to_substitute = Product.objects.get(id=request.POST.get('product_to_substitute'))
    substitute_product = Product.objects.get(id=request.POST.get('substitute_product'))
    user = request.user

    favorite_creation = Favorite.objects.get_or_create(
        product_to_substitute=product_to_substitute,
        substitute_product=substitute_product,
        user=user
    )

    return HttpResponse(favorite_creation)


def add_favorites_test(request):
    product_to_substitute2 = Product.objects.get(id=request.POST.get('product_to_substitute'))
    substitute_product2 = Product.objects.get(id=request.POST.get('substitute_product'))
    user = request.user

    try:
        favorite = Favorite.objects.get(
            product_to_substitute_id=request.POST.get('product_to_substitute'),
            substitute_product_id=request.POST.get('substitute_product')
        )
        if str(favorite.substitute_product_id) == request.POST.get('substitute_product'):
            favorite_deletion = favorite.delete()
            return HttpResponse(favorite_deletion)
    except Favorite.DoesNotExist:
        favorite_creation = Favorite.objects.get_or_create(
            product_to_substitute=product_to_substitute2,
            substitute_product=substitute_product2,
            user=user
        )
        return HttpResponse(favorite_creation)
