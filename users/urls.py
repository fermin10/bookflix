"""Defines URL patterns for users"""
from django.urls import path, include
from . import views
from django.contrib import admin


app_name = 'users'
urlpatterns = [

    path('admin/', admin.site.urls, name='admin'),
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('configurar/', views.configurar, name='configurar'),
    path('register/', views.register, name='register'),
]