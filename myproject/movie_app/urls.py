from django.urls import path
from .views import MovieView, MovieDetailView

urlpatterns = [
    path('', MovieView.as_view(), name='movie-list'),
    path('<int:id>', MovieDetailView.as_view(), name='movie-id'),

]
