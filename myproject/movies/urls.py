from django.urls import path
from .views import MovieListView, MovieDetailAPIView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('<int:id>', MovieDetailAPIView.as_view(), name='movie-id'),

]
