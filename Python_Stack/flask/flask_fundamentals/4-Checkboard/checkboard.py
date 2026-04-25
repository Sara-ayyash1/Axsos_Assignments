from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<x>")
@app.route("/<x>/<y>")
@app.route("/<x>/<y>/<color1>/<color2>")
def checkboard(x =8 , y =8 , color1 = "#556B2F" , color2 = "#FFFFE0"):
    return render_template("index.html" , x = int(x) , y = int(y) , color1=color1 ,color2=color2)

if __name__ == "__main__":
    app.run(debug=True)