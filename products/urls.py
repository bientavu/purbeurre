from django.urls import path
from products import views


urlpatterns = [
    # path('results/', views.products_list, name='products_list'),
    path('results/<int:product_id>/', views.product_detail, name='product_detail')
]
