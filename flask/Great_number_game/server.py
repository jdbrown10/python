from flask import Flask, render_template, redirect, request, session
app = Flask (__name__)
app.secret_key = "sdfjkla54233sdjfkahsdjsf53djkah33djk4hflkl"

import random
random.randint(1, 100)

#==========================
#ROOT ROUTE - Renders Form
#==========================
@app.route("/")
def index():
    if "comp_guess" in session:
        print("Computer's guess = " + str(session["comp_guess"]))
    else:
        session["comp_guess"] = random.randint(1, 100)


    if "comparison" not in session:
        session["comparison"] = "none"


    return render_template("index.html", comparison = session["comparison"])



#==========================
#ROOT ROUTE - Processes Form
#==========================
@app.route("/process_guess", methods=["POST"])
def process_guess():
    print(request.form)

    if request.form["guess"] != "":
        user_guess = int(request.form["guess"])
    else:
        return redirect("/")
    comp_guess = session["comp_guess"]

    if comp_guess == user_guess:
        print("You got it right!")
    else:
        print("You got it wrong...")
    
    if comp_guess > user_guess:
        session["comparison"] = "low"
    elif comp_guess < user_guess:
        session["comparison"] = "high"
    else:
        session["comparison"] = "perfect"

    print(session["comparison"])

    return redirect("/")

#==========================
#RESET ROUTE - Processes Form
#==========================
@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")




if __name__=="__main__":
    app.run(debug=True, port=5001)