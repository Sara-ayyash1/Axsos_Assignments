# Flask Routing Demo 🗺️

A simple Flask app that demonstrates how routing works — connecting URLs to Python functions.

---

## Project Structure

```
Hello_Flask/
│
└── app.py
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

## Routes

| URL | Description |
|-----|-------------|
| `/` | Returns "Hello World!" |
| `/success` | Returns "success" |
| `/hello/<name>` | Returns a greeting with the given name |
| `/users/<username>/<id>` | Returns the username and ID |
| `/<name>` | Returns the name with an exclamation mark |
| `/say/<name>` | Returns "Hi name!" |
| `/repeat/<count>/<str>` | Repeats the string the given number of times |

### Examples

```
/hello/Ahmad         → Hello, Ahmad
/users/Ahmad/42      → username: Ahmad, id: 42
/say/Ahmad           → Hi Ahmad!
/repeat/3/hello      → hello
                       hello
                       hello
```

---

## How It Works

- `@app.route('/path')` connects a URL to a Python function
- `<variable>` in the route captures dynamic values from the URL and passes them to the function
- Multiple variables can be captured in the same route: `/<username>/<id>`
- `@app.errorhandler(404)` handles any undefined routes and returns a custom error message instead of the default Flask 404 page

---

## Notes

- The `localhost:5000` part of the URL determines which server receives the request
- The rest of the route tells the server which function should run
- Routes are matched in order — more specific routes should be defined before general ones like `/<name>`