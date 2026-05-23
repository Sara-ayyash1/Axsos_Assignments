#  Single Model ORM — Django Users App

A Django web application that demonstrates how to use Django's ORM with a single model. Users can be viewed in a table and added through an HTML form — all connected to a SQLite database.

---

##  Project Structure

```
single_model_orm/
├── single_model_orm/        # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── users_app/               # App handling users
│   ├── migrations/
│   ├── templates/
│   │   └── index.html       # Main template (table + form)
│   ├── models.py            # User model
│   ├── views.py             # index + add_user views
│   ├── urls.py              # URL routes
│   └── admin.py
├── db.sqlite3               # SQLite database
└── manage.py
```

---

##  Features

- Display all users in a styled HTML table
- Add a new user through an HTML form (POST request)
- Django ORM for database interaction (no raw SQL)
- CSRF protection on all forms
- Redirects after form submission

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Sara-ayyash1/single_model_orm.git
cd single_model_orm
```

### 2. Create and activate a virtual environment

```bash
python -m venv django_env
# Windows
django_env\Scripts\activate
# Mac/Linux
source django_env/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

Then open your browser at: **http://localhost:8000**

---

## 🔗 URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `views.index` | Show all users + form |
| `/add_user` | `views.add_user` | Process form & save to DB |

---

## 🗃️ User Model

```python
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

---

##  Tech Stack

- **Python** 3.14
- **Django** (latest)
- **SQLite** (default DB)
- **HTML / Tailwind CSS**

---