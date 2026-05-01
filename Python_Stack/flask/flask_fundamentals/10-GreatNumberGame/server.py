from flask import Flask, render_template, session, redirect, request
import random     

app = Flask(__name__)
app.secret_key = 'keep_it_secret_keep_it_safe' 

def get_message_style(message):
    if 'high' in message:
        return {'bg': 'bg-red-50 border-red-100', 'text': 'text-red-600'}
    elif 'low' in message:
        return {'bg': 'bg-blue-50 border-blue-100', 'text': 'text-blue-600'}
    elif 'Correct' in message :
        return {'bg': 'bg-green-50 border-green-100', 'text': 'text-green-700'}
    else:
        return {'bg': 'bg-gray-50 border-gray-100', 'text': 'text-gray-600'}
    
@app.route('/')
def index():
    # Only set the target number if it doesn't exist yet
    if 'answer' not in session:
        session['answer'] = random.randint(1, 100)
        session['attempts'] = 0
        session['message'] = None
        session['game_over'] = False

    style = get_message_style(session['message']) if session.get('message') else None
    return render_template('index.html', style=style)

#Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
@app.route('/process', methods=['POST'])
def process():
    if session['game_over']:
        return redirect('/')
    
    user_ans = int(request.form['guessing_num'])
    session['attempts'] += 1
    if user_ans > session['answer']:
        session['message'] = "Too high!"
        
    elif user_ans < session['answer']:
        session['message'] = "Too low!"

    else:
        session['message'] = f"Correct, {session['answer']} was the number!"
        session['game_over'] = True
        return redirect('/')

    if session['attempts'] >= 5:
        session['message'] = 'You Lose! Game Over'
        session['game_over'] = True

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear() 
    return redirect('/')


winners = []

@app.route('/submit_winner', methods=['POST'])
def submit_winner():
    name = request.form['name']
    attempts = session['attempts']
    winners.append({'name': name, 'attempts': attempts})
    session.clear()
    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    sorted_winners = sorted(winners, key=lambda x: x['attempts'])
    return render_template('leaderboard.html', winners=sorted_winners)

if __name__ == "__main__":
    app.run(debug=True)