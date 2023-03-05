from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes.views import my_home, my_sobre, my_contato




urlpatterns = [
    path("", my_home),
    path("sobre/", my_sobre),
    path("contato/", my_contato)
    
]