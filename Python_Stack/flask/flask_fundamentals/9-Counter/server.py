from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'keep_it_secret_keep_it_safe' 

import base64

cookie = "eyJ2aXNpdHMiOjV9" 
decoded = base64.b64decode(cookie + "==")
print(decoded)# Output: b'{"visits": 5}'

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    #We can't increment something that doesn't exist! Here's how to check if a key exists in session yet:
    if 'count' not in session:
        session['count'] = 0
       
    session['visits'] += 1
    return render_template('index.html')


@app.route('/increment_count_2')
def increment_count_2():
    if 'count' in session:
        session['count'] += 2
        
    return redirect('/')


@app.route('/custom_increment', methods = ['POST'])
def custom_increment():
    increment_by = int(request.form['amount']) 
    session['count'] += increment_by
    return redirect('/')


@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    # If we want to get rid of what is currently stored in session:
    #session.pop('count')        # clears a specific keycopy
    session.clear() # clears all keys
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

   