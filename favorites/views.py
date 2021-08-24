from django.shortcuts import render
from favorites.models import Favorite
from django.http import HttpResponse


def import_favorites(request):
    favorites = Favorite.objects.all()
    return render(request, 'favorites/favorites.html', {'favorites': favorites})


def add_favorites(request, product_to_substitute, substitute_product, user):
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)
    # adding_favorites = Favorite.objects.create(
    #     product_to_substitute=product_to_substitute,
    #     substitute_product=substitute_product,
    #     user=user
    # )
