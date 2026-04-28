from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got POST info")
    print(request.form)
    
    # name_from_form = request.form['name']
    # email_from_form = request.form['email']
    
    # return render_template(
    #     "show.html",
    #     name_on_template=name_from_form,
    #     email_on_template=email_from_form
    # ) 

    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")  # ← غيرنا هون


@app.route('/show')
def show_user():
    return render_template('show.html')  # ← بس هيك!

if __name__ == "__main__":
    app.run(debug=True) 

