# Playground 🎨

A simple Flask app that generates colored boxes dynamically based on URL parameters.

---

## Project Structure

```
Playground/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── css/
        └── style.css
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
   http://127.0.0.1:5000
   ```

---

## Usage

Customize the boxes via the URL:

| URL | Description |
|-----|-------------|
| `/` or `/play` | Default 3 boxes with default color |
| `/play/<num>` | Custom number of boxes |
| `/play/<num>/<color>` | Custom number of boxes and color |

### Examples

```
/play/5
/play/6/red
/play/4/tomato
/play/3/FFA500
---

## URL Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `nums_of_boxes` | `3` | Number of boxes to display |
| `color` | `9FC5F8` (light blue) | Background color of the boxes |

---

## How It Works

- Flask receives the URL parameters and passes them to the HTML template
- Jinja2 loops through the number of boxes using a `{% for %}` loop
- Each box gets its background color set via inline `style` attribute
- The boxes are laid out using Flexbox with wrapping for responsive display