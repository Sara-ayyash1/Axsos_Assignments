# Dojo & Ninjas — Django ORM Assignment

A full-stack Django application practicing one-to-many relationships using the Django ORM and Django Shell.

---

## Project Structure

```
dojo_ninjas_proj/
├── dojo_ninjas_proj/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dojo_ninjas_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── index.html
└── manage.py
```

---

## Models

### Dojo
| Field | Type |
|-------|------|
| name  | CharField(255) |
| city  | CharField(255) |
| state | CharField(255) |
| desc  | TextField (default: "old dojo") |

### Ninja
| Field | Type |
|-------|------|
| first_name | CharField(255) |
| last_name  | CharField(255) |
| dojo       | ForeignKey → Dojo (CASCADE) |

> One Dojo has many Ninjas. One Ninja belongs to one Dojo.

---

## Routes

| Method | URL | Description |
|--------|-----|-------------|
| GET  | `/` | Display all dojos and their ninjas |
| POST | `/add_dojo` | Create a new dojo |
| POST | `/add_ninja` | Create a new ninja |
| POST | `/delete_dojo/<int:dojo_id>` | Delete a dojo and all its ninjas |

---

## Features

- ✅ Create & display Dojos
- ✅ Create Ninjas and assign them to a Dojo via dropdown
- ✅ Delete a Dojo (cascades to all associated Ninjas)
- ✅ Show ninja count per dojo
- ✅ Empty state when no dojos exist

---

## Shell Queries

All ORM queries are saved in `queries.txt`:

```python
from dojo_ninjas_app.models import Dojo, Ninja

# Create 3 dojos
Dojo.objects.create(name="Dojo1", city="Gaza", state="PS")
Dojo.objects.create(name="Dojo2", city="Ramallah", state="PS")
Dojo.objects.create(name="Dojo3", city="Nablus", state="PS")

# Delete all dojos
Dojo.objects.all().delete()

# Create 3 new dojos
d1 = Dojo.objects.create(name="Dojo A", city="Gaza", state="PS")
d2 = Dojo.objects.create(name="Dojo B", city="Ramallah", state="PS")
d3 = Dojo.objects.create(name="Dojo C", city="Nablus", state="PS")

# Create 3 ninjas per dojo
Ninja.objects.create(first_name="Ali",   last_name="Hassan", dojo=d1)
Ninja.objects.create(first_name="Sara",  last_name="Ahmed",  dojo=d1)
Ninja.objects.create(first_name="Omar",  last_name="Nasser", dojo=d1)

Ninja.objects.create(first_name="Lina",  last_name="Khalil", dojo=d2)
Ninja.objects.create(first_name="Tariq", last_name="Yousef", dojo=d2)
Ninja.objects.create(first_name="Nour",  last_name="Salem",  dojo=d2)

Ninja.objects.create(first_name="Hana",  last_name="Mahmoud", dojo=d3)
Ninja.objects.create(first_name="Yasser",last_name="Issa",    dojo=d3)
Ninja.objects.create(first_name="Reem",  last_name="Barakat", dojo=d3)

# Retrieve ninjas from first dojo
d1.ninjas.all()

# Retrieve ninjas from last dojo
Dojo.objects.last().ninjas.all()

# Retrieve last ninja's dojo
Ninja.objects.last().dojo

# Create new dojo after adding desc field
Dojo.objects.create(name="Dojo D", city="Hebron", state="PS", desc="New dojo")
```

---

## Key Concepts Practiced

- **ForeignKey** with `related_name` and `on_delete=CASCADE`
- **Django Shell** ORM queries (create, delete, filter, reverse lookup)
- **Django Templates** with `{% for %}`, `{% empty %}`, `|length`, `|pluralize`
- **CSRF protection** on all POST forms
- **Migrations** including altering models after creation

---

## Setup

```bash
# 1. Create project & app
django-admin startproject dojo_ninjas_proj
cd dojo_ninjas_proj
python manage.py startapp dojo_ninjas_app

# 2. Add app to INSTALLED_APPS in settings.py

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Start server
python manage.py runserver

# 5. Open shell
python manage.py shell
```

---
