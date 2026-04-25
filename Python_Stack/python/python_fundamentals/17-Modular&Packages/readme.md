# Modular & Packages 📦

A Python demo that explains how modules work — specifically the difference between running a file directly vs importing it from another file.

---

## Project Structure

```
17-Modular&Packages/
│
└── app.py
```

---

## How It Works

### `__name__` — The Key Concept

Every Python file has a built-in variable called `__name__`.

| How the file runs | Value of `__name__` |
|---|---|
| Run directly (`python app.py`) | `"__main__"` |
| Imported by another file | The file's name (e.g. `"app"`) |

This lets you control what code runs and when:

```python
if __name__ == "__main__":
    # This only runs when the file is executed directly
    print("Running directly!")
else:
    # This runs when the file is imported by another file
    print("I was imported by:", __name__)
```

---

## What's Inside

### Variable
```python
local_val = "magical unicorns"
```
A module-level variable — accessible anywhere inside this file or when imported.

---

### Function
```python
def square(x):
    return x * x
```
Takes a number and returns its square. When imported, other files can use `app.square(5)`.

---

### Class
```python
class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"
```
A simple class with a constructor and a method. When imported, other files can create `User` objects using `app.User("Anna")`.

---

## Why This Matters

When you build a large project, you split your code into multiple files (modules). The `if __name__ == "__main__"` check makes sure your testing/demo code doesn't accidentally run when another file imports your module.

### Example

```
project/
├── app.py       ← defines square(), User, etc.
└── main.py      ← imports from app.py
```

```python
# main.py
import app  # This triggers the else block in app.py, not the if block
result = app.square(4)
print(result)  # 16
```