from flask import Flask, render_template, redirect, session
app = Flask (__name__)
app.secret_key = "sasadffsadsa4677d5fasdf78sa6f"


#==========================
#ROOT ROUTE - Renders Form
#==========================
@app.route("/")
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template("index.html")

#==========================
#ADD ROUTE - Adds to Count
#==========================

@app.route("/add")
def add():
    session['counter'] += 1
    return redirect("/")

#==========================
#RESET ROUTE - Resets Count
#==========================
@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True, port=5001)