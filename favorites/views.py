from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from favorites.models import Favorite
from django.http import HttpResponse

from products.models import Product


def import_favorites(request):
    favorites = Favorite.objects.all()
    return render(request, 'favorites/favorites.html', {'favorites': favorites})


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
