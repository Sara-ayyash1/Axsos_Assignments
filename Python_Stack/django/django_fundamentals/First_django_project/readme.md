# First Django Project 🐍

A Django routing practice project that demonstrates URL patterns, views, redirects, route parameters, and multiple apps.

## Project Overview

This project was built to practice:
- Setting up a new Django project with multiple apps
- Configuring URL routing using `include()`
- Writing views that return HTTP responses and redirects
- Using route parameters
- Organizing routes across multiple apps

## Setup & Installation

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

## Project Structure

```
First_django_project/
├── First_django_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── first_app/
│   ├── views.py
│   └── urls.py
├── surveys_app/
│   ├── views.py
│   └── urls.py
├── user_app/
│   ├── views.py
│   └── urls.py
└── manage.py
```

## Routes

###  Blogs (`first_app`)

| URL | Method | Description |
|-----|--------|-------------|
| `/` | `index` | Same as `/blogs` — Ninja Bonus ⭐ |
| `/blogs` | `index` | Displays list placeholder |
| `/blogs/new` | `new` | Displays new blog form placeholder |
| `/blogs/create` | `create` | Redirects to `/blogs` |
| `/blogs/<number>` | `show` | Displays blog number |
| `/blogs/<number>/edit` | `edit` | Displays edit placeholder |
| `/blogs/<number>/delete` | `destroy` | Redirects to `/blogs` |
| `/blogs/json` | `blog_json` | Returns JSON response |

### Surveys (`surveys_app`)

| URL | Method | Description |
|-----|--------|-------------|
| `/surveys` | `index` | Displays all surveys placeholder |
| `/surveys/new` | `new` | Displays new survey form placeholder |

###  Users (`user_app`)

| URL | Method | Description |
|-----|--------|-------------|
| `/users` | `index` | Displays all users placeholder |
| `/users/new` | `register` | Same method as `/register` |
| `/register` | `register` | Displays register placeholder |
| `/login` | `login` | Displays login placeholder |

## Code

### Project `urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blogs/', include('first_app.urls')),
    path('surveys/', include('surveys_app.urls')),
    path('', include('user_app.urls')),
]
```

### `first_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('json', views.blog_json),
    path('<int:number>', views.show),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
]
```

### `first_app/views.py`

```python
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/blogs')

def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder to edit blog {number}')

def destroy(request, number):
    return redirect('/blogs')

def blog_json(request):
    return JsonResponse({'title': 'My First Blog', 'content': 'Hello Django!'})
```

### `surveys_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
]
```

### `surveys_app/views.py`

```python
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('placeholder to display all the surveys created.')

def new(request):
    return HttpResponse('placeholder for users to add a new survey.')
```

### `user_app/urls.py`

```python
from django.urls import path
from . import views
from first_app import views as blog_views

urlpatterns = [
    path('users/new', views.register),
    path('users', views.index),
    path('register', views.register),
    path('login', views.login),
    path('', blog_views.index),   # Ninja Bonus ⭐
]
```

### `user_app/views.py`

```python
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('placeholder to display all the list of users later.')

def register(request):
    return HttpResponse('placeholder for users to create a new user record.')

def login(request):
    return HttpResponse('placeholder for users to log in.')
```