# Counter App 

A Django web app that tracks how many times a user visits a page, with session-based counters and custom increment controls.

---

## Features

- Tracks visit count per session
- Displays a counter that persists across page refreshes
- Reset button to clear the session
- +2 quick increment button
- Custom increment form (enter any number)

---

## Setup

```bash
# Create and activate virtual environment
python -m venv django_env
source django_env/bin/activate  # Windows: django_env\Scripts\activate

# Install Django
pip install django

# Create project & app
django-admin startproject counter_project
cd counter_project
python manage.py startapp counter_app
```

Register the app in `counter_project/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'counter_app',
]
```

---

## Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `index` | Displays visit count and counter |
| `/destroy_session` | `destroy_session` | Clears session and redirects to `/` |
| `/increment_count_2` | `increment_count_2` | Adds 2 to counter |
| `/increment_by` | `increment_by` | Adds custom amount to counter (POST) |

---

## Code

### `counter_app/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    path('increment_count_2', views.increment_count_2),
    path('increment_by', views.increment_by),
]
```

### `counter_app/views.py`

```python
from django.shortcuts import render, redirect

def index(request):
    if 'visit' not in request.session:
        request.session['visit'] = 0
    if 'counter' not in request.session:
        request.session['counter'] = 0

    request.session['visit'] += 1
    return render(request, 'index.html')

def destroy_session(request):
    request.session.flush()
    return redirect('/')

def increment_count_2(request):
    if 'counter' in request.session:
        request.session['counter'] += 2
    return redirect('/')

def increment_by(request):
    if request.method == 'POST':
        if 'counter' in request.session:
            amount = int(request.POST.get('amount', 0))
            request.session['counter'] += amount
    return redirect('/')
```

### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counter</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="min-h-screen bg-gray-100 flex items-center justify-center p-8">

  <div class="bg-white rounded-2xl p-10 w-full max-w-sm shadow-sm border border-gray-100">

    <p class="text-xs uppercase tracking-widest text-gray-600 mb-2">Counter</p>
    <p class="text-8xl font-bold text-gray-900 leading-none mb-3">{{request.session.counter}}</p>
    <span class="inline-flex items-center gap-2 bg-gray-100 rounded-full px-3 py-1 text-sm text-gray-500">
      <span class="w-2 h-2 rounded-full bg-green-600 inline-block"></span>
      {{request.session.visit}} visits
    </span>

    <hr class="my-7 border-gray-100">

    <p class="text-xs uppercase tracking-widest text-gray-600 mb-3">Actions</p>
    <div class="flex gap-3">
      <a href="/increment_count_2" class="flex-1 text-center py-3 bg-gray-900 text-white rounded-xl text-base font-bold hover:bg-gray-700 transition">+2</a>
      <a href="/destroy_session" class="flex-1 text-center py-3 bg-red-50 text-red-500 border border-red-200 rounded-xl text-base font-medium hover:bg-red-100 transition">Reset</a>
    </div>

    <hr class="my-7 border-gray-100">

    <p class="text-xs uppercase tracking-widest text-gray-600 mb-3">Custom increment</p>
    <form action="/increment_by" method="post" class="flex gap-3">
      {% csrf_token %}
      <input name="amount" type="number" placeholder="Amount" min="1" required
        class="flex-1 px-4 py-3 border border-gray-200 rounded-xl text-base text-gray-900 bg-gray-50 focus:outline-none focus:border-gray-600">
      <button type="submit" class="px-5 py-3 bg-indigo-500 text-white rounded-xl text-base font-bold hover:bg-indigo-600 transition">Add</button>
    </form>

  </div>

</body>
</html>
```

---

## Run the App

```bash
python manage.py migrate
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---
