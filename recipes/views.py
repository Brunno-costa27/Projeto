from django.shortcuts import render
from django.http import HttpResponse


def my_home(request):
    return render(request, 'recipes/home.html')

def my_sobre(request):
    return render(request, 'recipes/contato.html')
    

def my_contato(request):
    return HttpResponse("contato")