from django.urls import path
from .views import MovieView, MovieDetailView

urlpatterns = [
    path('movies', MovieView.as_view(), name='movie-list'),
    path('movie/<int:id>', MovieDetailView.as_view(), name='movie-id'),
    
]
