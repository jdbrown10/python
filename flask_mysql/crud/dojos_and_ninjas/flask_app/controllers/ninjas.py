from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# I think I'm supposed to use this controller for the ninja-related routes, but anything I put in here didn't work, so I just put it in dojos.py and it worked that way.... so uhhhhh.... 

# ================================
# RENDER CREATE NINJA
# ================================
@app.route("/ninja/new")
def new_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", all_dojos = all_dojos)

# ================================
# PROCESS CREATE NINJA
# ================================
@app.route("/ninja/new/process", methods=['POST'])
def process_new_ninja():
    
    data = {
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }

    new_ninja_id = Ninja.create_new_ninja(data)

    return redirect(f'/dojos/{request.form["dojo_id"]}')