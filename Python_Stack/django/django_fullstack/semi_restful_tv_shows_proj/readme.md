#  Semi-Restful TV Shows

A Django CRUD web application for managing TV shows, built as part of the Full Stack Django module at AXSOS Academy.

---

##  Project Overview

This project implements a semi-RESTful architecture using Django, allowing users to **Create**, **Read**, **Update**, and **Delete** TV show records through a clean, browser-based interface.

---

##  Features

- View all TV shows in a table
- Add a new TV show via a form
- View a single show's details
- Edit an existing show
- Delete a show

---

##  Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/shows` | Display all shows in a table |
| GET | `/shows/new` | Display form to add a new show |
| POST | `/shows/create` | Save new show to database, redirect to `/shows` |
| GET | `/shows/<id>` | Display a single show's details |
| GET | `/shows/<id>/edit` | Display form to edit a show |
| POST | `/shows/<id>/update` | Update the show in the database, redirect to `/shows/<id>` |
| POST | `/shows/<id>/destroy` | Delete the show from the database, redirect to `/shows` |
| GET | `/` | Root route — redirects to `/shows` |

---

##  Model

**Show**

| Field | Type |
|-------|------|
| title | CharField |
| network | CharField |
| release_date | DateField |
| description | TextField |
| created_at | DateTimeField (auto) |
| updated_at | DateTimeField (auto) |

---

##  Setup & Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd semi-restful-tv-shows

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Then open your browser and go to: [http://localhost:8000](http://localhost:8000)

---

##  Project Structure

```
semi_restful_tv_shows/
│
├── shows_app/
│   ├── migrations/
│   ├── templates/
│   │   └── shows_app/
│   │       ├── index.html        # All shows
│   │       ├── add_show.html     # Create form
│   │       ├── show_detail.html  # Single show
│   │       └── edit_show.html    # Edit form
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── semi_restful_tv_shows/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```

---

##  Tech Stack

- **Python** 3.x
- **Django** 4.x
- **SQLite** (default Django database)
- **HTML / CSS**

---