from django.urls import path
from search import views


urlpatterns = [
    path('results/', views.search_results, name='search_results'),
    path('', views.home, name='home'),
]
