from django.urls import path
from .views import *
from dj_rest_auth.views import LoginView,LogoutView

urlpatterns = [
    path('register/', userRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    
]

