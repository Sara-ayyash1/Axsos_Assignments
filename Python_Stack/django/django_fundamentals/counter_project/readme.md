# Counter App 

A Django web app that tracks page visits and manages a session-based counter.

---

## Features

- Session-based visit tracking
- Counter with reset functionality
- Quick +2 increment
- Custom increment via form

---

## Tech Stack

- Python 3.14
- Django 6.0
- Tailwind CSS

---

## Setup

```bash
git clone https://github.com/Sara-ayyash1/counter-project
cd counter-app
python manage.py migrate
python manage.py runserver
```

---

## Routes

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Home page |
| `/destroy_session` | GET | Reset session |
| `/increment_count_2` | GET | Add 2 to counter |
| `/increment_by` | POST | Add custom amount |

---

