from django.urls import path
from .views import MovieView, MovieDetailView,AuthorDetailView,AuthorView,CategoryDetailView,CategoryView

urlpatterns = [
    path('movies', MovieView.as_view(), name='movie-list'),
    path('movie/<int:id>', MovieDetailView.as_view(), name='movie-id'),
    path('authors', AuthorView.as_view(), name='author-list'),
    path('author/<int:id>', AuthorDetailView.as_view(), name='author-id'),
    path('categories', CategoryView.as_view(), name='category-list'),
    path('category/<int:id>', CategoryDetailView.as_view(), name='category-id'),
    
]
