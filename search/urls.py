from django.urls import path
from search import views


urlpatterns = [
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
