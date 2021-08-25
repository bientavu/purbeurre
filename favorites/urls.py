from django.urls import path
from favorites import views


urlpatterns = [
    path('favorites/', views.import_favorites, name='favorites'),
    path('add_favorites/', views.add_favorites)
]
