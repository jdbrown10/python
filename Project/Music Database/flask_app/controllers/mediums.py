from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.medium import Medium

# =======================================
# Process Create New Medium
# =======================================

@app.route('/new_medium/process', methods=['POST'])
def create_medium():
    
    # validate the form data
    data = {
        "type": request.form["type"],
        "user_id": request.form["user_id"]
    }

    if not Medium.validate_medium(data):
        return redirect("/new_song")

    # save the new medium to the db
    Medium.create_medium(data)

    # redirect
    return redirect('/new_song')