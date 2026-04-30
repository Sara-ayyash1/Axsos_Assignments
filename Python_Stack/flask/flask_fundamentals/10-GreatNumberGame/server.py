from flask import Flask, render_template, session, redirect, request
import random     

app = Flask(__name__)
app.secret_key = 'keep_it_secret_keep_it_safe' 

@app.route('/')
def index():
    # Only set the target number if it doesn't exist yet
    if 'answer' not in session:
        session['answer'] = random.randint(1, 100)
        session['attempts'] = 0
        session['message'] = None
        session['game_over'] = False
    return render_template('index.html')

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
        session['message'] = f"{session['answer']} was the number!"
        session['game_over'] = True
        return redirect('/')

    if session['attempts'] >= 5:
        session['message'] = 'You Lose! Game Over'
        session['game_over'] = True
        return redirect('/')


    return redirect('/')

@app.route('/reset')
def reset():
    session.clear() 
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)