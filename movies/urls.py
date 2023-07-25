from django.urls import path
from .views import MovieView, MovieDatailsView, MovieOrdenView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDatailsView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrdenView.as_view())
]
