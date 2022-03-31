from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.source import Source

# =======================================
# Process Create New Composer
# =======================================

@app.route('/new_source/process', methods=['POST'])
def create_source():
    
    # validate the form data
    data = {
        "title": request.form["title"],
        "user_id": request.form["user_id"],
        "medium_id": request.form["medium"]
    }

    if not Source.validate_source(data):
        return redirect("/new_song")

    # save the new composer to the db
    Source.create_source(data)

    # redirect
    return redirect('/new_song')