#  Time Display - Django Project

An elegant, clean Django web application that captures and displays the current live date and time. Built as part of the backend engineering curriculum at Axsos Academy to practice foundational Django concepts, template rendering, and static file integration.

##  Project Objectives
- **Framework Setup:** Practice initializing and structuring a clean Django project and application.
- **Context Passing:** Familiarity with passing dynamic backend data (`views.py`) into frontend templates (`index.html`).
- **Static Assets:** Practice configuring, routing, and structuring static assets (`CSS/Design layouts`) seamlessly within the Django ecosystem.

---

##  Tech Stack & Concepts Applied
- **Backend:** Python 3.x, Django Web Framework.
- **Frontend:** HTML5, CSS3 (Custom responsive architecture utilizing Flexbox layout metrics).
- **Time Parsing Engine:** Utilized native Python `time` module wrappers (`gmtime`, `strftime`) to render standard formatted strings.

---

##  Directory Structure

```text
time_display_project/
│
├── time_display_project/       # Project Configuration Directory
│   ├── __init__.py
│   ├── settings.py             # Configured with registered 'time_display' app & static mappings
│   ├── urls.py                 # Core routing connecting application namespaces
│   └── wsgi.py
│
├── time_display/               # Core Application Component
│   ├── migrations/
│   ├── static/                 # Static Asset Subsystem
│   │   └── css/
│   │       └── style.css       # Custom stylesheet managing exact layout alignment
│   ├── templates/              # Presentation Templates
│   │   └── index.html          # Django template integrating standard template language tags
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py                 # Application-specific isolated route mappings
│   └── views.py                # Controller defining time payload architecture
│
└── manage.py                   # Django Administrative CLI wrapper
```

---

##  Step-by-Step Implementation Details

### 1. View Engine Pipeline (`time_display/views.py`)
Processes incoming requests and compiles a payload dictionary containing the parsed server timestamp formatted clearly into a standard readable pattern (`%b %d, %Y %I:%M %p`):

```python
from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
```

### 2. URL Mappings (`time_display/urls.py`)
Handles dynamic routing for both root requests and direct path invocations ensuring compliance with strict project route design constraints:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('time_display', views.index),
]
```

### 3. Template Presentation Layer (`time_display/templates/index.html`)
Injects dynamic data securely utilizing Django Template Language execution contexts:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Time Display Dashboard</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="container">
        <h3>The current time and date:</h3>
        <div class="time-box">
            <h1>{{ time }}</h1>
        </div>
    </div>
</body>
</html>
```

---

##  Local Deployment Instructions

Follow these instructions to spin up the server environment locally on your desktop machine:

1. **Clone or Navigate to the Repository Root:**
   ```bash
   cd time_display_project
   ```

2. **Initialize Database Schemas (Optional/Best Practice):**
   ```bash
   python manage.py migrate
   ```

3. **Boot Up the Local Development Server Engine:**
   ```bash
   python manage.py runserver
   ```

4. **Access the Interface:**
   Open your preferred browser engine and test the deployment at either endpoint:
   - Root URL: `http://localhost:8000/`
   - Explicit URL: `http://localhost:8000/time_display`
