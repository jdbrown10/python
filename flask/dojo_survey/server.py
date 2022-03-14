from flask import Flask, render_template, redirect, session, request
app = Flask (__name__)
app.secret_key = "sf67596ds8af56s7a8fd86sa"

#==========================
#ROOT ROUTE - Renders Form
#==========================
@app.route('/')
def index():
    return render_template("index.html")

#==========================
#POST ROUTE - Processes Results
#==========================
@app.route('/process', methods=["POST"])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['optional'] = request.form['optional']
    return redirect('/result')

#==========================
#RESULT ROUTE - Renders Results
#==========================
@app.route('/result')
def result():
    return render_template("result.html", name=session['name'], location=session['location'], language=session['language'], optional=session['optional'])


if __name__=="__main__":
    app.run(debug=True, port=5001)