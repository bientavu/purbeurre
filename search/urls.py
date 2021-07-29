from django.urls import path
# from .views import SearchResultsView
from search import views


urlpatterns = [
    path('results/', views.search_results, name='search_results'),
]
