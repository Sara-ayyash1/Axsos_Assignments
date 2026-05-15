# First Django Project 🐍

A Django routing practice project that demonstrates URL patterns, views, redirects, and route parameters.

##  Project Overview

This project was built to practice:
- Setting up a new Django project and app
- Configuring URL routing
- Writing views that return HTTP responses and redirects
- Using route parameters

##  Setup & Installation

```bash
# Create and activate virtual environment
python -m venv django_env
django_env\Scripts\activate  # Windows
source django_env/bin/activate  # Mac/Linux

# Install Django
pip install django

# Run the development server
python manage.py runserver
```

##  Project Structure
```
First_django_project/
├── First_django_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── first_app/
│   ├── views.py
│   └── urls.py
└── manage.py
```

##  Routes

| URL | Method | Description |
|-----|--------|-------------|
| `/` | `root` | Redirects to `/blogs` |
| `/blogs` | `index` | Displays list placeholder |
| `/blogs/new` | `new` | Displays new blog form placeholder |
| `/blogs/create` | `create` | Redirects to `/` |
| `/blogs/<number>` | `show` | Displays blog number |
| `/blogs/<number>/edit` | `edit` | Displays edit placeholder |
| `/blogs/<number>/delete` | `destroy` | Redirects to `/blogs` |
| `/blogs/json`  | `blog_json` | Returns JSON response (Bonus) |

##  Code

### `urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/json', views.blog_json),
    path('blogs/<int:number>', views.show),
    path('blogs/<int:number>/edit', views.edit),
    path('blogs/<int:number>/delete', views.destroy),
]
```

### `views.py`

```python
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder to edit blog {number}')

def destroy(request, number):
    return redirect('/blogs')

# Bonus
def blog_json(request):
    return JsonResponse({'title': 'My First Blog', 'content': 'Hello Django!'})
```