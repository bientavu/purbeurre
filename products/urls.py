from django.urls import path
from products import views


urlpatterns = [
    path('results/', views.products_list, name='products_list')
]
