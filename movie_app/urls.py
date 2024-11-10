from django.urls import path
from .views import MovieView, MovieDetailView,MovieDeleteView,MovieUpdateView,MovieCreateView

urlpatterns = [
    path('movies', MovieView.as_view(), name='movie-list'),
    path('<movie/int:id>', MovieDetailView.as_view(), name='movie-id'),
    path('movies', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:id>', MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/<int:id>', MovieUpdateView.as_view(), name='movie-update'),


]
