from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<int:x>')
def box_size(x):
    return render_template("index.html", x = x)


@app.route('/<int:x>/<int:y>')
def box_size_2(x, y):
    return render_template("index.html", x = x, y = y)

@app.route('/<int:x>/<int:y>/<string:custom1>/<string:custom2>')
def box_size_custom_colors(x, y, custom1, custom2):
    return render_template("index.html", x = x, y = y, custom1 = custom1, custom2 = custom2)

if __name__=="__main__":
    app.run(debug=True, port=5001)