from django.urls import path
from .views import MovieView, MovieDetailView,AuthorDetailView,AuthorView

urlpatterns = [
    path('movies', MovieView.as_view(), name='movie-list'),
    path('movie/<int:id>', MovieDetailView.as_view(), name='movie-id'),
    path('authors', AuthorView.as_view(), name='author-list'),
    path('author/<int:id>', AuthorDetailView.as_view(), name='author-id'),
    
]
