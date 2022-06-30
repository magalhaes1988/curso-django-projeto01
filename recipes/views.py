from __localcode.factory import make_recipe
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe

# Create your views here.


# recipe = Recipe.objects.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        # 'recipes': [make_recipe() for _ in range(10)]
        'recipes': recipes
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_Detail_Page': True,
    })


def category(request, category_id):
    #    recipes = Recipe.objects.filter(
    #        category__id=category_id, is_published=True).order_by('-id')

    #    if not recipes:
    #        raise Http404('Not found 2')

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}  - Category | '
    })
