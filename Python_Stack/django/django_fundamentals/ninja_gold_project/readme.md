#  Ninja Gold

A Django web app where your ninja starts with 0 gold and earns (or loses!) gold by visiting different locations. Each visit is logged with a timestamp and displayed as an activity feed.

---

##  Features

- ✅ Ninja starts with 0 gold stored in session
- ✅ Four locations to visit: Farm, Cave, House, Quest
- ✅ Each location awards a random gold amount within its range
- ✅ Quest can result in gaining **or losing** gold (–50 to +50)
- ✅ Activity log stored in session, newest entries shown first
- ✅ Each activity shows message, color (green/red), and timestamp
- ✅ Reset button clears session and starts over

---

##  Gold Ranges per Location

| Location | Min Gold | Max Gold |
|----------|----------|----------|
|  Farm  | +10      | +20      |
|  Cave  | +10      | +20      |
|  House | +10      | +20      |
|  Quest | –50      | +50      |

---

##  Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Session Storage:** Django built-in session framework
- **Database:** SQLite (default Django)

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/Sara-ayyash1/ninja_gold_project.git
cd ninja_gold_project

# 2. Create and activate a virtual environment
python -m venv django_env
source django_env/bin/activate        # Mac/Linux
django_env\Scripts\activate           # Windows

# 3. Install dependencies
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Start the development server
python manage.py runserver
```

Then open your browser at **http://localhost:8000**

---

##  Project Structure

```
ninja_gold_project/
├── ninja_gold_app/
│   ├── templates/
│   │   └── index.html          # Main game page
│   ├── views.py                # Game logic (index, process_money, reset)
│   ├── urls.py                 # App URL routes
│   ├── models.py
│   └── apps.py
├── ninja_gold_project/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── readme.md
```

---

##  How to Play

1. Visit the home page — your ninja starts with **0 gold**
2. Click one of the four location buttons (Farm, Cave, House, Quest)
3. The server calculates a random gold amount for that location
4. Your gold total updates and the activity is logged with a timestamp
5. Green entries = gold gained ✅ | Red entries = gold lost ❌
6. Click **Reset** to clear everything and start a new game

---

##  Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page — shows gold total, location forms, activity log |
| `/process_money` | POST | Handles location visit, updates gold and activity log |
| `/reset` | GET | Flushes session and redirects to home |

---

##  Session Variables

| Key | Type | Description |
|-----|------|-------------|
| `gold` | int | Current gold total for the ninja |
| `activities` | list | List of `{msg, color}` dicts, newest first |

---

##  Bonus Features Implemented

-  **Ninja:** Location passed via URL rather than hidden form input