# 🥷 Ninja Gold

A Flask mini-game where a ninja travels across different locations to earn (or lose) gold.

---

## Project Structure

```
ninja_gold/
├── server.py
└── templates/
    └── index.html
```

---

## Setup & Run

```bash
pip install flask
python server.py
```

Then open your browser at: `http://localhost:5000`

---

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Main page — shows gold, buildings, and activity log |
| `/process_money` | POST | Handles form submit, updates gold in session |
| `/reset` | GET | Clears session and restarts the game |

---

## Buildings & Gold Ranges

| Building | Min | Max | Notes |
|----------|-----|-----|-------|
| 🌾 Farm  | +10 | +20 | Always earns |
| ⛏️ Cave  | +5  | +10 | Always earns |
| 🏠 House | +2  | +5  | Always earns |
| 🎰 Casino| -50 | +50 | Can earn **or** lose! |

---

## Key Concepts Used

- **Flask Sessions** — stores gold amount and activity log across requests
- **Hidden Inputs** — each form sends `building` value to `/process_money`
- **Dictionary dispatch** — no if/elif chains, buildings stored in a dict
- **`random.randint(min, max)`** — picks a random amount within the range

---

## Features

- [x] 4 building forms with hidden inputs
- [x] Session-based gold tracking
- [x] Activity log (color-coded: 🟢 green = earned, 🔴 red = lost)
- [x] Activities in descending order (newest first)
- [x] Reset button
- [x] Only 2 routes (`/` and `/process_money`)
- [x] No 4 conditional statements — uses dictionary instead