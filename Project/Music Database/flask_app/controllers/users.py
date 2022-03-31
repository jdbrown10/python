from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#=======================================
#Render Register/Login
#=======================================

@app.route('/')
def index():
    return render_template("index.html")


#=======================================
#Register / Login Routes
#=======================================

@app.route('/register', methods=['POST'])
def register():
    #validate form info
    #for this part, don't use the bcrypted password so that you can validate it first...
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : request.form["password"],
        "conf_pass" : request.form["conf_pass"],
    }

    if not User.validate_register(data):
        return redirect("/")

    #bcrypt password
    data["password"] =  bcrypt.generate_password_hash(request.form['password'])

    #save new user to db
    new_user_id = User.create_user(data)

    #enter owner ID into Session (use same label for login!!!)
    session["user_id"] = new_user_id

    #redirect to dashboard
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    #validate login info
    data = {
        "email" : request.form["email"],
        "password" : request.form["password"]
    }
    if not User.validate_login(data):
        return redirect("/")

    #validation is good. 
    # Then query for user info based on email... and then...
    user = User.get_by_email(data)
    
    #put the user ID into session and redirect to dashboard
    session["user_id"] = user.id

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out!")
    return redirect ("/")

#=======================================
#Render Dashboard
#=======================================

@app.route('/dashboard')
def dashboard():

    if "user_id" not in session:
        flash("You have to login or register before entering =( sorry bout that...")
        return redirect("/")

    data = {
        "user_id" : session["user_id"]
    }

    user = User.get_by_id(data)

    return render_template("dashboard.html", user = user) #all_songs = all_songs.... gotta go here