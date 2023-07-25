from django.urls import path
from .views import UserView, UserDatailsView, LoginView

urlpatterns = [path("users/", UserView.as_view()),
               path("users/<int:user_id>/", UserDatailsView.as_view()),
               path("users/login/", LoginView.as_view())]