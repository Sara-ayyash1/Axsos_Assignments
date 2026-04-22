#Imported the Flask class, which is required for every Flask application.
from flask import Flask

# Created an instance of the Flask class called app.
app = Flask(__name__)

# Defined a route using the decorator @app.route("/route"), which connects a URL to a Python function.
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/success')
def success():
    return "success"

#Anything placed after /hello/ in the URL will be passed to the function as the variable name.
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

#Practice to Understanding Routing
@app.route('/<name>')
def show_name(name):
    return f"{name}!"

@app.route('/say/<name>')
def say_flask(name):
    return f"Hi {name}!"

@app.route('/repeat/<count>/<str>')
def repeat(count , str):
    return f'{str}\n' * int(count)


# @app.route('/<path:path>')
# def catch_all(path):
#     return "Sorry! No response. Try again."

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."



if __name__ == "__main__":
    #Started the development server using app.run()
    app.run(debug=True)

# The localhost:5000 portion of the URL determines which server receives the request. 
# The rest of the route tells the server which function should run.

     
     