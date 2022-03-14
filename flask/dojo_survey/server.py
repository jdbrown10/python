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
    session['bagels'] = request.form['bagels']
    session['bike'] = request.form['bike']
    session['train'] = request.form['train']
    session['boat'] = request.form['boat']
    session['car'] = request.form['car']
    return redirect('/result')

#==========================
#RESULT ROUTE - Renders Results
#==========================
@app.route('/result')
def result():
    if 'bagels' not in session:
        session['bagels'] = "none"
    
    if 'bike' not in session:
        session['bike'] = "none"

    if 'train' not in session:
        session['train'] = "none"

    if 'boat' not in session:
        session['boat'] = "none"

    if 'car' not in session:
        session['car'] = "none"

    return render_template("result.html", name=session['name'], location=session['location'], language=session['language'], optional=session['optional'], bagels=session['bagels'])

#==========================
#RESET ROUTE - Clears Session
#==========================
@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True, port=5001)