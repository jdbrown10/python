from flask import Flask, render_template
app = Flask (__name__)

@app.route("/play")
def index():
    return render_template("playground.html", x=3)

@app.route("/play/<int:x>")
def number_of_boxes(x):
    return render_template("playground.html", x = x)

@app.route("/play/<int:x>/<string:color>")
def colored_boxes(x, color):
    return render_template("playground.html", x = x, color=color)







if __name__=="__main__":
    app.run(debug=True, port=5001)