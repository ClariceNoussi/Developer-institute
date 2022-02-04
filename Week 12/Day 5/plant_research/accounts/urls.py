from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as django_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('About/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', django_views.LoginView.as_view(), name='login'),
    path('logout/', django_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.dashboard, name='dashboard'),
]