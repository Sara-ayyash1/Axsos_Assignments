# Counter App 

A simple Flask web app that demonstrates how to use sessions and cookies to store and manage client-side state across HTTP requests.

---

## Overview

Flask's `session` object stores user data in a signed cookie sent to the browser. Because HTTP is stateless, without sessions the server has no memory of previous requests. This app tracks two values per user: the number of page visits and a manually controlled counter.

---

## Features

- Tracks the number of times the root route has been visited
- Displays a counter that can be incremented by 2, reset, or incremented by a custom amount
- Allows the session to be fully cleared via `/destroy_session`
- Styled with Tailwind CSS for a clean, minimal UI

---

## Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Renders the main page, initialises session, increments visit counter |
| GET | `/increment_count_2` | Adds 2 to the counter |
| POST | `/custom_increment` | Adds a custom amount to the counter |
| GET | `/reset` | Resets the counter to 0 |
| GET | `/destroy_session` | Clears all session data |

---

## How Sessions Work

Flask serialises the session dictionary into JSON, encodes it with Base64, and signs it using the app's `secret_key`. The result is stored as a browser cookie named `session`.

On every subsequent request the browser sends the cookie back automatically. Flask verifies the signature and deserialises the data, making it available via the `session` object.

> **Note:** The cookie data is Base64-encoded, not encrypted. Anyone can decode and read it. Flask only prevents tampering — if the cookie is modified, the signature will not match and Flask will reject it. Never store sensitive information such as passwords or permissions in the session.

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
counter/
├── server.py
└── templates/
    └── index.html
```