from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
@app.route("/play")
@app.route("/play/<nums_of_boxes>")
@app.route("/play/<nums_of_boxes>/<color>")
def play(nums_of_boxes = 3 , color = "#9FC5F8"):
    return render_template("index.html",no_of_boxes = int(nums_of_boxes) , clr= color)


if __name__ == "__main__":
    app.run(debug=True)