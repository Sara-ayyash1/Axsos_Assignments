# Great Number Game 
A number guessing game built with Flask that demonstrates session management, form handling, and server-side game logic.

---

## Overview

The server picks a random number between 1 and 100 and stores it in the session. The user has up to 5 attempts to guess it. After each guess, the server responds with "Too high", "Too low", or "Correct". If the user fails after 5 attempts, they lose and can start a new game.

---

## Features

- Random number generated once per game and stored in session
- Feedback after every guess: too high, too low, or correct
- Attempt counter with a visual progress bar (green → amber → red)
- Game ends after 5 wrong attempts with a "You Lose" message
- "Play again" button clears the session and starts fresh
- Styled with Tailwind CSS

---

## Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Loads the game, generates a number if session is empty |
| POST | `/process` | Validates the guess and updates session state |
| GET | `/reset` | Clears the session and redirects to `/` |

---

## Game Logic

```
User submits a guess
  ├── Too high  → store message, increment attempts
  ├── Too low   → store message, increment attempts
  └── Correct   → store win message, set game_over = True

After incrementing attempts:
  └── attempts >= 5 and not correct → store lose message, set game_over = True
```

---

## Setup

```bash
pip install flask
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## File Structure

```
great_number_game/
├── server.py
└── templates/
    └── index.html
```