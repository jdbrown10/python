from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User


# ========================
# ROOT ROUTE - DISPLAY ALL USERS
# ========================
@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users)


# ========================
# DISPLAY CREATE USER PAGE
# ========================

@app.route("/create_user")
def create_user_page():
    return render_template("create.html")


# ========================
# PROCESS CREATE USER
# ========================

@app.route("/create_user_process", methods=['POST'])
def create_user_process(): #I know if I'm redirecting to '/read_one/<int:user_id>' I need to pass the user_id into this function, but where to I get it from in the html?

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "eml": request.form["eml"]
    }


    user_id = User.save(data) #the method still runs when saved to a variable, so this is fine

    return redirect(f'/read_one/{user_id}')

# ========================
# SHOW ONE USER
# ========================

@app.route("/read_one/<int:user_id>")
def read_one(user_id):

    query_user_data = {
        "user_id" : user_id
    }

    one_user = User.get_one_user(query_user_data)

    return render_template('read_one.html', one_user = one_user )


# ========================
# DISPLAY EDIT USER
# ========================

@app.route("/edit_one/<int:user_id>")
def display_edit_one(user_id):

    query_user_data = {
        "user_id" : user_id,
    }

    one_user = User.get_one_user(query_user_data)

    return render_template('edit_one.html', one_user = one_user)


# ========================
# PROCESS EDIT USER
# ========================

@app.route("/edit_one/process", methods=['POST'])
def edit_one():
    
    User.edit_one_user(request.form)

    user_id = request.form["id"]

    return redirect(f'/read_one/{user_id}')

# ========================
# PROCESS DELETE USER
# ========================
@app.route("/delete_user/<int:id>")
def delete_one(id):
    
    query_user_data = {
        "id" : id,
    }

    User.delete_user(query_user_data)

    return redirect('/')