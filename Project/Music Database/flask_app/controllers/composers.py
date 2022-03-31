from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.composer import Composer

# =======================================
# Process Create New Composer
# =======================================

@app.route('/new_composer/process', methods=['POST'])
def create_composer():
    
    # validate the form data
    data = {
        "name": request.form["name"],
        "user_id": request.form["user_id"]
    }

    if not Composer.validate_composer(data):
        return redirect("/new_song")

    # save the new composer to the db
    Composer.create_composer(data)

    # redirect
    return redirect('/new_song')