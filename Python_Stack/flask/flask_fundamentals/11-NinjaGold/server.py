from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ninja_secret_key_123"


BUILDINGS = {
    "farm":   {"min": 10,  "max": 20,  "label": "farm"},
    "cave":   {"min": 5,   "max": 10,  "label": "cave"},
    "house":  {"min": 2,   "max": 5,   "label": "house"},
    "casino": {"min": -50, "max": 50,  "label": "casino"},
}

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = []
    return render_template("index.html")


#"/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route.
@app.route("/process_money", methods=["POST"])
def process_money():
    building = request.form.get("building")
  
    b = BUILDINGS[building]
    amount = random.randint(b["min"], b["max"])  

    session["gold"] = session.get("gold", 0) + amount

    now = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if amount >= 0:
        msg = f"Earned {amount} golds from the {building}!  ({now})"
        color = "green"
    else:
        msg = f"Entered a {building} and lost {abs(amount)} golds... Ouch.  ({now})"
        color = "red"
    activities = session.get("activities", [])
    activities.insert(0, {"msg": msg, "color": color})
    session["activities"] = activities

    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5000)