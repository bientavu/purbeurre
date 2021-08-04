from django.shortcuts import render
from favorites.models import Favorite


def import_favorites(request):
    favorites = Favorite.objects.all()
    return render(request, 'favorites/favorites.html', {'favorites': favorites})


def add_favorites(request):
    pass
