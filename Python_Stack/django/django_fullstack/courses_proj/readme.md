# Courses App 

A full-stack Django web application for managing bootcamp courses, built as part of the AXSOS Academy Python Stack curriculum.

---

## Features

- Add new courses with name and description
- View all courses in a table
- Delete a course with a confirmation page
- Add comments to each course and view all comments
- Model validations (name > 5 characters, description > 15 characters)
- One-to-One relationship between `Course` and `Description`
- One-to-Many relationship between `Course` and `Comment`

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default Django DB)
- **Frontend:** HTML, CSS
- **Icons:** Tabler Icons

---

## Project Structure

```
courses_app/
├── courses_app/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   ├── delete_confirm.html
│   │   └── comment.html
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── manage.py
```

---

## Models

### Course
| Field | Type |
|---|---|
| name | CharField (max 255) |
| created_at | DateTimeField |
| updated_at | DateTimeField |

### Description (One-to-One with Course)
| Field | Type |
|---|---|
| content | TextField |
| course | OneToOneField → Course |
| created_at | DateTimeField |
| updated_at | DateTimeField |

### Comment (Many-to-One with Course)
| Field | Type |
|---|---|
| content | TextField |
| course | ForeignKey → Course |
| created_at | DateTimeField |
| updated_at | DateTimeField |

---

## Routes

| URL | Method | Description |
|---|---|---|
| `/` | GET | Display all courses + add form |
| `/courses/add_course/` | POST | Create a new course |
| `/courses/destroy/<id>/` | GET | Show delete confirmation |
| `/courses/destroy/<id>/` | POST | Delete the course |
| `/courses/add_comment/<id>/` | GET | Show comments page |
| `/courses/create_comment/<id>/` | POST | Add a new comment |

---

## Getting Started

### 1. Clone the repository
```bash
git clone <https://github.com/Sara-ayyash1/Axsos_Assignments/tree/master/Python_Stack/django/django_fullstack/courses_proj>
cd courses_app
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
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

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Validations

- Course name must be **more than 5 characters**
- Course description must be **more than 15 characters**
- Comment content **cannot be empty**

---

## Author

Sara — AXSOS Academy, Python Stack