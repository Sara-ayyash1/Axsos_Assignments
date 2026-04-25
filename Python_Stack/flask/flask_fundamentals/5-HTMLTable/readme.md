# HTML Table 📋

A Flask app that passes a list of dictionaries from Python to an HTML template and displays them as a styled table using Jinja2 and the Foundation CSS framework.

---

## Project Structure

```
html_table/
│
├── app.py
└── templates/
    └── index.html
```

> No `static/` folder needed — Foundation is loaded via CDN!

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
   http://127.0.0.1:5000
   ```

---

## How It Works — Step by Step

### Step 1: The Data (app.py)

```python
users = [
    {'first_name': 'Michael', 'last_name': 'Choi'},
    {'first_name': 'John',    'last_name': 'Supsupin'},
    {'first_name': 'Mark',    'last_name': 'Guillen'},
    {'first_name': 'KB',      'last_name': 'Tonel'}
]
```

A **list of dictionaries** — each dictionary is one user with two keys: `first_name` and `last_name`. This is the standard format for database records in web development.

---

### Step 2: Passing Data to the Template (app.py)

```python
return render_template('index.html', users=users)
```

`render_template()` finds `index.html` inside the `templates/` folder and sends the `users` list to it so Jinja2 can use it.

---

### Step 3: Looping in the Template (index.html)

```html
{% for user in users %}
<tr>
    <td>{{ user['first_name'] }}</td>
    <td>{{ user['last_name'] }}</td>
    <td>{{ user['first_name'] }} {{ user['last_name'] }}</td>
</tr>
{% endfor %}
```

- `{% for user in users %}` — loops through every dictionary in the list
- `{{ user['first_name'] }}` — accesses the value of the key
- The **Full Name** column combines both keys with a space
- `{% endfor %}` — ends the loop

---

### Step 4: Jinja2 Syntax Summary

| Syntax | Purpose |
|--------|---------|
| `{{ variable }}` | Display a value |
| `{% for x in list %}` | Start a loop |
| `{% endfor %}` | End a loop |
| `{# comment #}` | Write a comment (not shown in browser) |

---

## Foundation CSS Framework

Foundation is loaded via **CDN** — no files to download:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/foundation-sites@6.8.1/dist/css/foundation.min.css">
```

### Foundation Classes Used

| Class | What it does |
|-------|-------------|
| `bg-light-gray` | Light gray background on the page |
| `padding-vertical-3` | Adds padding to top and bottom of the page |
| `grid-container` | Centers the content and sets a max-width |
| `text-center` | Centers the heading text |
| `margin-bottom-2` | Adds spacing below the heading |
| `hover` | Highlights a row when you hover over it |
| `striped` | Alternates row background colors (zebra style) |

### Why Foundation?

- No CSS file needed — just add the CDN link and start using classes
- Mobile-first — looks good on all screen sizes automatically
- Clean and professional default styles with minimal effort