# Dojo Survey — Dojango Project

A Django web application that collects bootcamp survey responses and displays the submitted information on a results page.

##  Overview

Built as part of the **Coding Dojo — Python Stack** curriculum. The app accepts a form submission via POST request and renders the submitted data on a new page.

---

##  Features

- Submit a survey form with name, location, language, experience level, and optional comment
- Results page displays all submitted data
- Styled with **Tailwind CSS**
- Radio buttons for experience level selection
- Handles optional fields gracefully

---

##  Tech Stack

- **Python** 3.14
- **Django** 6.0
- **Tailwind CSS** (via CDN)
- **Google Fonts** — Playfair Display & Inter

---

##  Project Structure

```
Dojo_survey_project/
├── dojo_survey_app/
│   ├── templates/
│   │   ├── index.html      # Survey form
│   │   └── info.html       # Results page
│   ├── views.py
│   └── urls.py
├── Dojo_survey_project/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---

##  Setup & Installation

**1. Clone the repository**
```bash
git clone <repo-url>
cd Dojo_survey_project
```

**2. Create and activate a virtual environment**
```bash
python -m venv django_env
# Windows
django_env\Scripts\activate
# Mac/Linux
source django_env/bin/activate
```

**3. Install Django**
```bash
pip install django
```

**4. Run the server**
```bash
python manage.py runserver
```

**5. Open in browser**
```
http://localhost:8000/
```

---

##  Routes

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Displays the survey form |
| `/result` | POST | Processes form and displays results |

---

##  Views

```python
def index(request):
    return render(request, 'index.html')

def process_form(request):
    context = {
        'name':     request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'level':    request.POST['level'],
        'comment':  request.POST.get('comment') or 'No Comment',
    }
    return render(request, 'info.html', context)
```

---
