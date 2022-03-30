from flask_app import app
from flask import render_template, redirect, request, session, flash

# from flask_app.models.song import Song


# =======================================
# Render New Song Page
# =======================================


@app.route('/new_song')
def new_recipe():
    if "user_id" not in session:
        flash("You have to login or register before entering =( sorry bout that...")
        return redirect("/")

    return render_template("new_song.html", user_id=session['user_id'])