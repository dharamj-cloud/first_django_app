from django.contrib import admin
from django.urls import path
from my_first_app import views

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
]
