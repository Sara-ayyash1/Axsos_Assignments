from flask import Flask , render_template , redirect ,request,session

app = Flask(__name__)
app.secret_key = "my secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def submit_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['level'] = request.form['level']
    session['comment'] = request.form['comment']
    return redirect('/info')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == "__main__":
    app.run(debug=True)