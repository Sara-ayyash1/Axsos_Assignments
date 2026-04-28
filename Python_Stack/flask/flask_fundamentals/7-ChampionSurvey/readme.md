# Dojo Survey

A Flask web application that accepts a form submission and displays the submitted data on a results page.

## Project Structure

```
7-ChampionSurvey/
├── templates/
│   ├── index.html
│   └── info.html
├── server.py
└── README.md
```

## How It Works

1. User visits `http://localhost:5000` and fills out the survey form
2. Form data is submitted via POST to `/result`
3. Data is stored in session and user is redirected to `/info`
4. Results page displays the submitted information

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Displays the survey form |
| `/result` | POST | Processes form data and redirects |
| `/info` | GET | Displays submitted information |

## Technologies Used

- Python
- Flask
- Tailwind CSS
- HTML

## How To Run

```
python server.py
```

Then visit `http://localhost:5000` in your browser.