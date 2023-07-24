from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import CategoryForm, RecipyForm
from .models import Recipy, Category

class CategoryList(ListView):
    model = Category
    ordering = 'title'
    template_name = 'categories.html'
    context_object_name = 'categories'

class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

class CategoryyCreate(CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'category_create.html'

class RecipiesList(ListView):
    model = Recipy
    ordering = 'title'
    template_name = 'recipies.html'
    context_object_name = 'recipies'

class RecipyDetail(DetailView):
    model = Recipy
    template_name = 'recipy.html'
    context_object_name = 'recipy'

class RecipyCreate(CreateView):
    form_class = RecipyForm
    model = Recipy
    template_name = 'recipy_create.html'

    