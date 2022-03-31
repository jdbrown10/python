from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.album import Album

# =======================================
# Process Create New Album
# =======================================

@app.route('/new_album/process', methods=['POST'])
def create_album():
    
    # validate the form data
    data = {
        "title": request.form["title"],
        "user_id": request.form["user_id"]
    }

    if not Album.validate_album(data):
        return redirect("/new_song")

    # save the new album to the db
    Album.create_album(data)

    # redirect
    return redirect('/new_song')