from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# ================================
# RENDER ALL DOJOS
# ================================

@app.route("/dojos")
def index():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template("dojos.html", dojos=dojos)

# ================================
# PROCESS CREATE DOJO
# ================================

@app.route("/create_dojo", methods=['POST'])
def create_user_process(): #I know if I'm redirecting to '/read_one/<int:user_id>' I need to pass the user_id into this function, but where to I get it from in the html?

    data = {
        "name": request.form["name"],
    }

    Dojo.create_dojo(data) #the method still runs when saved to a variable, so this is fine

    return redirect('/dojos')

# ================================
# RENDER DOJO SHOW
# ================================
@app.route("/dojos/<int:dojo_id>")
def dojo_show(dojo_id):

    data = {
        "dojo_id" : dojo_id
    }

    ninjas = Ninja.get_certain_ninjas(data)

    dojo_name = Dojo.get_certain_dojo_name(data)

    return render_template("dojo_show.html", ninjas = ninjas, dojo_id = dojo_id, dojo_name=dojo_name)