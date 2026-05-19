# Great Number Game (Django Edition) 

An interactive and stylish web-based guessing game built using **Django** and styled with **Tailwind CSS**. The application challenges users to guess a randomly generated number between 1 and 100 within a limited number of attempts, featuring a dynamic progress bar and a persistent leaderboard system.

---

##  Features

### Core Functionality
* **Random Number Generation:** Automatically picks a secret number between 1 and 100 upon loading.
* **Session-Based State:** Tracks client history, game states, attempts, and messages securely using Django Sessions.

###  Ninja Bonuses Included
* **Dynamic Styling:** Colorful feedback boxes tailored to the user's guess (e.g., Light Red for "Too High", Light Blue for "Too Low", and Light Green for "Correct").
* **Attempt Tracking:** Visually informs the user how many attempts they have taken before finding the right number.

###  Sensei Bonuses Included
* **Attempt Limit (Max 5):** Users only have 5 chances to guess correctly. If they fail on the 5th attempt, a custom "You Lose" screen appears with an option to retry.
* **Save Winners Profile:** Winners can save their names after a successful guess.
* **Leaderboard Page:** A dedicated, clean leaderboard sorting and displaying all winners based on their efficiency (lowest number of attempts).

---

##  Tech Stack

* **Backend:** Python 3.14+ & Django 6.0+
* **Frontend:** HTML5, Django Template Language (DTL)
* **Styling:** Tailwind CSS (via CDN)

---

##  Project Structure

```text
great_number_game_project/
│
├── great_number_game_app/
│   ├── templates/
│   │   ├── index.html        # Main Game UI (Tailwind CSS)
│   │   └── leaderboard.html  # Scoreboard View
│   ├── urls.py               # App routing (process, reset, leaderboard, etc.)
│   └── views.py              # Main logic & session handling
│
├── great_number_game_project/
│   ├── settings.py           # Project configurations (INSTALLED_APPS updated)
│   └── urls.py               # Root routing config
│
└── manage.py                 # Django management script