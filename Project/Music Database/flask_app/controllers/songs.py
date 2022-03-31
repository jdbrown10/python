from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.composer import Composer
from flask_app.models.source import Source
from flask_app.models.medium import Medium
from flask_app.models.album import Album
from flask_app.models.keyword import Keyword

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

    all_sources = Source.get_all_sources(data)

    all_albums = Album.get_all_albums(data)

    all_keywords = Keyword.get_all_keywords(data)

    all_mediums = Medium.get_all_mediums()


    return render_template("new_song.html", user_id=session['user_id'], all_composers=all_composers, all_sources=all_sources, all_mediums=all_mediums, all_albums=all_albums, all_keywords=all_keywords)