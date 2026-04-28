# Dojo Fruit Store 🍓

A Flask web application where students can order fruits from the Dojo store.

## Project Structure

```
dojo_fruit_store/
├── static/
│   ├── css/
│   │   └── bootstrap.css
│   └── img/
│       ├── apple.png
│       ├── blackberry.png
│       ├── raspberry.png
│       └── strawberry.png
├── templates/
│   ├── index.html
│   ├── checkout.html
│   └── fruits.html
├── server.py
└── README.md
```

## How It Works

1. User visits `http://localhost:5000` and selects fruit quantities
2. User fills in their name and student ID then clicks Checkout
3. Form data is stored in session and user is redirected to `/show_checkout`
4. Checkout page displays the order summary

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Displays the fruit order form |
| `/checkout` | POST | Processes order and redirects |
| `/show_checkout` | GET | Displays order summary |
| `/fruits` | GET | Displays available fruits with images |

## Technologies Used

- Python
- Flask
- Bootstrap

## How To Run

```bash
git clone https://github.com/mchoidojo/dojo_fruit_store
cd dojo_fruit_store
python server.py
```

Then visit `http://localhost:5000` in your browser.