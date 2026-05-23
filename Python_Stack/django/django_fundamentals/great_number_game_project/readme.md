#  Great Number Game

A Django web app where the server picks a random number between 1 and 100, and the user tries to guess it. The app gives feedback after each guess (too high / too low / correct), tracks attempts, limits guesses to 5, and includes a leaderboard for winners.

---

##  Features

- ✅ Server picks a random number (1–100) and stores it in session
- ✅ User submits guesses via a form
- ✅ Feedback: **Too High** (red), **Too Low** (blue), or **Correct!** (green)
- ✅ Tracks number of attempts per game
- ✅ Progress bar showing attempts out of 5
- ✅ Max 5 guesses — "You Lose" message if not guessed in time
- ✅ Winner can submit their name to the leaderboard
- ✅ Leaderboard page showing winners and their attempt counts
- ✅ "Play Again" resets the session and starts a new game

---

##  Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, Tailwind CSS
- **Session Storage:** Django built-in session framework
- **Database:** SQLite (default Django)

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/Sara-ayyash1/great_number_game_project.git
cd great_number_game

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
great_number_game_project/
├── great_number_game_app/
│   ├── templates/
│   │   ├── index.html          # Main game page
│   │   └── leaderboard.html    # Winners leaderboard
│   ├── views.py                # Game logic (index, process, submit_winner)
│   ├── urls.py                 # App URL routes
│   ├── models.py
│   └── apps.py
├── great_number_game_project/
│   ├── settings.py
│   └── urls.py                 # Project URL config
├── manage.py
└── readme.md
```

---

##  How to Play

1. Visit the home page — the server secretly picks a number between 1 and 100
2. Enter your guess and submit
3. The app tells you if your guess is **too high**, **too low**, or **correct**
4. You have **5 attempts** — guess correctly before running out!
5. If you win, enter your name to appear on the **leaderboard**
6. Click **Play Again** to start a new round

---

##  Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page — starts game, shows guess form |
| `/process/` | POST | Handles guess submission, returns feedback |
| `/submit_winner/` | POST | Saves winner's name to session leaderboard |
| `/leaderboard/` | GET | Displays all winners and attempt counts |

---

##  Session Variables

| Key | Type | Description |
|-----|------|-------------|
| `answer` | int | The secret random number |
| `attempts` | int | Number of guesses made |
| `message` | str | Feedback message (too high / too low / correct) |
| `game_over` | bool | Whether the game has ended |
| `winners` | list | List of `{name, attempts}` dicts for leaderboard |

---

##  Bonus Features Implemented

-  **Ninja:** Color-coded feedback with Tailwind CSS
-  **Ninja:** Continuous guessing until correct or game over
-  **Ninja:** Attempt counter displayed to the user
-  **Sensei:** 5-guess limit with "You Lose" message
-  **Sensei:** Winner name submission + leaderboard page