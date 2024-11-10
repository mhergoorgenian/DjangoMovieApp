from django.urls import path
from .views import MovieView, MovieDetailView,MovieDeleteView,MovieUpdateView,MovieCreateView

urlpatterns = [
    path('', MovieView.as_view(), name='movie-list'),
    path('<int:id>', MovieDetailView.as_view(), name='movie-id'),
    path('create', MovieCreateView.as_view(), name='movie-create'),
    path('delete/<int:id>', MovieDeleteView.as_view(), name='movie-delete'),
    path('update/<int:id>', MovieUpdateView.as_view(), name='movie-update'),


]
