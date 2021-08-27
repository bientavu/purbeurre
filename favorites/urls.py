from django.urls import path
from favorites import views


urlpatterns = [
    path('favorites/', views.import_favorites, name='favorites'),
    path('add_favorites_test/', views.add_favorites_test)
]
