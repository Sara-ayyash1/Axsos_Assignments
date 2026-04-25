# Modular & Packages 📦

A Python demo that explains how modules work — specifically the difference between running a file directly vs importing it from another file.

---

## Project Structure

```
Modular&Packages/
│
└── parent.py
└── child.py
```

---

## How It Works

### `__name__` — The Key Concept

Every Python file has a built-in variable called `__name__`.

| How the file runs | Value of `__name__` |
|---|---|
| Run directly (`python parent.py`) | `"__main__"` |
| Imported by another file | The file's name (e.g. `"parent"`) |

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

## Why This Matters

When you build a large project, you split your code into multiple files (modules). The `if __name__ == "__main__"` check makes sure your testing/demo code doesn't accidentally run when another file imports your module.
