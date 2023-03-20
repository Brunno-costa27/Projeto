from django.shortcuts import render
from django.http import Http404
from utils.recipes.factory import make_recipe
from utils.recipes.pagination import make_pagination
from .models import Recipe
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
import os

PER_PAGE = os.environ.get('PER_PAGE')


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    # messages.success(request, 'Errou...')
    # messages.error(request, 'Errou...')
    # messages.info(request, 'Errou...')
    
    return render(request, 'recipes/pages/home.html', context={
        "recipes": page_obj,
        "pagination_range": pagination_range
    })
    
def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    
    
    if not recipes:
        raise Http404('Not found :)')
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    
    return render(request, 'recipes/pages/category.html', context={
        "recipes": page_obj,
        "pagination_range": pagination_range,
        "title": f'{recipes.first().category.name} - Category'
    })

def recipe(request, id):
    recipe = Recipe.objects.filter(pk=id, is_published=True).order_by('-id').first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        "recipe": recipe,
        'is_detail_page': True
    })
    
def search(request):
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    
    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}'
    })