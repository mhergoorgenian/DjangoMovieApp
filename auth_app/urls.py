from django.urls import path
from .views import MeView,LoginView,RegisterView

urlpatterns = [
    path('me', MeView.as_view(),name="get-mydata"),
    path('login', LoginView.as_view(),name='auth-login'),
    path('register', RegisterView.as_view(),name='auth-register')
]
