from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.composer import Composer

# from flask_app.models.song import Song


# =======================================
# Render New Song Page
# =======================================


@app.route('/new_song')
def new_song():
    if "user_id" not in session:
        flash("You have to login or register before entering =( sorry bout that...")
        return redirect("/")

    data = {
        "user_id" : session["user_id"]
    }

    all_composers = Composer.get_all_composers(data)

    return render_template("new_song.html", user_id=session['user_id'], all_composers=all_composers)