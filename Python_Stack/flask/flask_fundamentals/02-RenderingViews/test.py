from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #render_template function tells Flask to locate the HTML file inside the templates directory and return it as the response.
    return render_template("index.html" ,phrase="hello", times=5)

if __name__ == "__main__":
    app.run(debug=True , port=5001)