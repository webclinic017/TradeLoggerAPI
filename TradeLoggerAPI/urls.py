from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, LoginView, UserView, UnregisterView

urlpatterns = [
    # accepts all endpoints of TradeLoggerAPI
    path('auth/register', RegisterView.as_view()),
    path('auth/login', LoginView.as_view()),
    path('auth/user', UserView.as_view()),
    path('auth/unregister', UnregisterView.as_view()),
]