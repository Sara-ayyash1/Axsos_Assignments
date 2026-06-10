# Login & Registration App 

A full-stack Django web application for user authentication, built as part of the AXSOS Academy Python Stack curriculum.

---

## Features

- User registration with full validations
- User login with bcrypt password verification
- Session management (login/logout)
- Success page protected from unauthenticated users
- Flash messages for errors and success
- COPPA compliance — users must be at least 13 years old

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default Django DB)
- **Password Encryption:** bcrypt
- **Frontend:** HTML, CSS
- **Icons:** Tabler Icons

---

## Project Structure

```
login_reg/
├── login_reg/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── login_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── index.html
│   │   └── success.html
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

### User
| Field | Type |
|---|---|
| first_name | CharField (max 255) |
| last_name | CharField (max 255) |
| email | EmailField (unique) |
| password | CharField (max 255) |
| birthday | DateField |
| created_at | DateTimeField |
| updated_at | DateTimeField |

---

## Routes

| URL | Method | Description |
|---|---|---|
| `/` | GET | Display login & registration page |
| `/register/` | POST | Register a new user |
| `/login/` | POST | Login an existing user |
| `/success/` | GET | Welcome page (protected) |
| `/logout/` | GET | Clear session and redirect to login |

---

## Validations

### Registration
- First name: required, at least 2 characters, letters only
- Last name: required, at least 2 characters, letters only
- Email: required, valid format, must be unique
- Birthday: must be in the past, user must be at least 13 years old (COPPA)
- Password: required, at least 8 characters
- Confirm password: must match password

### Login
- Email: required, valid format
- Password: must match the stored hashed password

---

## Getting Started

### 1. Clone the repository
```bash
git clone <https://github.com/Sara-ayyash1/Axsos_Assignments/tree/master/Python_Stack/django/django_fullstack/login_reg_proj>
cd login_reg
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install django bcrypt
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

## Security Notes

- Passwords are hashed using **bcrypt** before being stored in the database
- The `/success` route is protected — unauthenticated users are redirected to login
- Email uniqueness is enforced at both the validator and database level

---

## Author

Sara — AXSOS Academy, Python Stack