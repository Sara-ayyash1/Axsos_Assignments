# Books & Authors

A full-stack Django web application that demonstrates a **many-to-many relationship** between Books and Authors.

---

## Features

- Add, view Books
- Add, view Authors
- Associate authors with books and books with authors
- Dropdown menus only show unassociated records (Sensei Bonus)

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS

---

## Project Structure

```
books_authors_proj/
│
├── books_authors_app/
│   ├── templates/
│   │   ├── book.html
│   │   ├── book_detail.html
│   │   ├── author.html
│   │   └── author_detail.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
└── db.sqlite3
```

---

## Models

### Book
| Field | Type |
|-------|------|
| title | CharField |
| desc | CharField |
| created_at | DateTimeField |
| updated_at | DateTimeField |

### Author
| Field | Type |
|-------|------|
| first_name | CharField |
| last_name | CharField |
| notes | TextField |
| books | ManyToManyField → Book |
| created_at | DateTimeField |
| updated_at | DateTimeField |

---

## Routes

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | List all books + add book form |
| `/add_book` | POST | Add a new book |
| `/book_detail/<id>` | GET | View book details and associated authors |
| `/book_detail/<id>` | POST | Add an author to the book |
| `/edit_book/<id>` | GET/POST | Edit a book |
| `/delete_book/<id>` | GET | Delete a book |
| `/authors` | GET | List all authors + add author form |
| `/add_author` | POST | Add a new author |
| `/author_detail/<id>` | GET | View author details and associated books |
| `/author_detail/<id>` | POST | Add a book to the author |
| `/edit_author/<id>` | GET/POST | Edit an author |
| `/delete_author/<id>` | GET | Delete an author |

---

## Getting Started

### 1. Clone the repository
```bash
git clone <repo-url>
cd books_authors_proj
```

### 2. Create and activate virtual environment
```bash
python -m venv django_env
source django_env/bin/activate  # Mac/Linux
django_env\Scripts\activate     # Windows
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

### 6. Open in browser
```
http://127.0.0.1:8000/
```

---