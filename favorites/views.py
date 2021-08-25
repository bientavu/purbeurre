from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from favorites.models import Favorite
from django.http import HttpResponse


def import_favorites(request):
    favorites = Favorite.objects.all()
    return render(request, 'favorites/favorites.html', {'favorites': favorites})


@csrf_exempt
def add_favorites(request):
    print('YES')
    print(request.user)
    print(request.POST.get('substitute_product', None))
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"
    return HttpResponse(message)
    # Favorite.objects.get_or_create(
    #     product_to_substitute=product_to_substitute,
    #     substitute_product=substitute_product,
    #     user=user
    # )
