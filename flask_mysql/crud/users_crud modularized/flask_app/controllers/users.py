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

@app.route("/create_user_process", methods=['post'])
def create_user_process():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "eml": request.form["eml"]
    }
    User.save(data)
    return redirect('/')

# ========================
# DISPLAY ONE USER
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
    return redirect('/')

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