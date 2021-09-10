from django.shortcuts import render
from favorites.models import Favorite
from django.http import HttpResponse
from products.models import Product


def import_favorites(request):
    if request.user.is_active:
        product_substituted = Product.objects.filter(
            favorites_as_product__isnull=False,
            favorites_as_product__user=request.user
        ).distinct()
        context = {'product_substituted': product_substituted}
        return render(request, 'favorites/favorites.html', context)


def add_favorites_test(request):
    product_to_substitute = Product.objects.get(
        id=request.POST.get('product_to_substitute')
    )
    substitute_product = Product.objects.get(
        id=request.POST.get('substitute_product')
    )
    user = request.user
    is_deleted = True
    try:
        favorite = Favorite.objects.get(
            product_to_substitute_id=request.POST.get('product_to_substitute'),
            substitute_product_id=request.POST.get('substitute_product')
        )
        if str(favorite.substitute_product_id) ==\
                request.POST.get('substitute_product'):
            favorite.delete()
            return HttpResponse(is_deleted)
    except Favorite.DoesNotExist:
        Favorite.objects.get_or_create(
            product_to_substitute=product_to_substitute,
            substitute_product=substitute_product,
            user=user
        )
        is_deleted = False
        return HttpResponse(is_deleted)
