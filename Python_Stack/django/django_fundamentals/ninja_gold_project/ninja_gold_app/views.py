from django.shortcuts import render , redirect
import random 
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold' not in request.session  :
        request.session['gold'] = 0
    if "activities" not in request.session:
        request.session["activities"] = []
    return render(request , "index.html")

BUILDINGS = {
    "farm":   {"min": 10,  "max": 20},
    "cave":   {"min": 5,   "max": 10},
    "house":  {"min": 2,   "max": 5},
    "quest": {"min": -50, "max": 50},
}

def process_money(request):
    building = request.POST.get("building")
  
    b = BUILDINGS[building]
    amount = random.randint(b["min"], b["max"])  

    request.session['gold'] = request.session.get("gold", 0) + amount

    now = datetime.now().strftime("%b %d, %Y %I:%M %p")#"%Y/%M/%d %I:%M %p"  
    if amount >= 0:
        msg = f"You entered a {building} and earned {amount} golds.  ({now})"
        color = "green"
    else:
        msg = f"You failed a {building} and lost {abs(amount)} golds... Ouch.  ({now})"
        color = "red"
    activities = request.session.get("activities", [])
    activities.insert(0, {"msg": msg, "color": color})
    request.session[''] = activities
    request.session.modified = True
    return redirect("/")

def reset(request):
    request.session.flush()
    return redirect('/')