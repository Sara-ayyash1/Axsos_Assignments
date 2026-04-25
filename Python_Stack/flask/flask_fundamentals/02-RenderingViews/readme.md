# Flask Template Engine Demo 🧩

A simple Flask app that demonstrates how to pass data from the server to HTML templates using Jinja2.

---

## Project Structure

```
RenderingView/
│
├── app.py
└── templates/
    └── index.html
```

---

## Installation

1. **Install Flask**
   ```bash
   pip install flask
   ```

2. **Run the app**
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5001
   ```

---

## How It Works

Flask passes data from `app.py` to the HTML template using `render_template()`:

```python
return render_template("index.html", phrase="hello", times=5)
```

Inside the template, Jinja2 syntax is used to display and work with that data:

| Syntax | Purpose |
|--------|---------|
| `{{ variable }}` | Display a variable |
| `{% for %}` | Loop |
| `{% if %}` | Conditional |

---

## Jinja2 Features Demonstrated

- **Variables** — displaying `phrase` and `times` directly in the HTML
- **For Loop** — repeating the phrase based on the `times` value
- **If Statement** — conditionally rendering content based on the phrase value

---

## Notes

- The app runs on port `5001` instead of the default `5000`
- Templates must be placed inside the `templates/` folder for Flask to locate them
- Jinja2 comments use `{# ... #}` syntax and are not rendered in the browser