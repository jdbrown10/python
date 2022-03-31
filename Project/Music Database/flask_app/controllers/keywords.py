from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.keyword import Keyword

# =======================================
# Process Create New Keyword
# =======================================

@app.route('/new_keyword/process', methods=['POST'])
def create_keyword():
    
    # validate the form data
    data = {
        "type": request.form["type"],
        "user_id": request.form["user_id"]
    }

    if not Keyword.validate_keyword(data):
        return redirect("/new_song")

    # save the new keyword to the db
    Keyword.create_keyword(data)

    # redirect
    return redirect('/new_song')