from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

#===================================
# Render Register/Login
# ==================================

@app.route("/")
def index():
    return render_template("index.html")

#===================================
# Process Register
# ==================================

@app.route("/register", methods=["POST"])
def register_user():
    
    if not User.validate_register(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    query_data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
        "password" : pw_hash
    }

    new_user_id = User.create_user(query_data)

    session['user_id'] = new_user_id

    return redirect("/dashboard")

#===================================
# Process Login
# ==================================

@app.route("/login", methods=["POST"])
def login_user():

    #1 gotta validate
    if not User.validate_login(request.form):
        return redirect("/")

    #2 query
    #we don't need the password anymore, it was just used for validation
    query_data = {
        "email" : request.form["email"]
    }

    #you could also just pass request.form directly in here - fwiw
    logged_in_user = User.get_by_email(query_data)

    #3 put user_id into Session
    session['user_id'] = logged_in_user.id

    #4 redirect to dashboard
    return redirect("/dashboard")

#===================================
# Render Dashboard
# ==================================

@app.route('/dashboard')
def dashboard():
    #this part is important!!! it's like a little validation to make sure the site doesn't error out if someone tries to manually go to the page without being logged in
    if "user_id" not in session:
        flash("You have to login or register before entering =( sorry bout that...")
        return redirect("/")
    user_id = session["user_id"]

    return render_template("dashboard.html", logged_user_id = user_id)

#===================================
# Process Logout
# ==================================

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")