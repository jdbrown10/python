from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.composer import Composer
from flask_app.models.source import Source
from flask_app.models.medium import Medium
from flask_app.models.album import Album
from flask_app.models.keyword import Keyword
from flask_app.models.song import Song
from flask_app.models.user import User

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

@app.route('/new_song/process', methods=['POST'])
def new_song_process():
        
    num_of_keywords = int(request.form["keyword_counter"])

    keyword_ids = []

    data = {
        "title": request.form["title"],
        "user_id": request.form["user_id"],
        "audio": request.form.get("audio"),
        "composer": request.form["composer"],
        "source": request.form["source"],
        "album": request.form["album"]
    }

    keyword_ids.append(request.form["keyword"])


    #if we get 5 keywords from the form, the first one is appended to the list on line 61. this loop needs to append the remaining 4 (whose names should have consecutively increasing numbers attached via the javascript function). this will count from one up to (but not including) the number of keywords, so if there were 5 total, it will add 4 more. but the name in the request.form needs to start at 2 and increase until it gets to 5, so we need to add one to it to get to the proper name for each keyword input. (i hope)
    if num_of_keywords > 1:
        for i in range (1, num_of_keywords):
            keyword_ids.append(request.form["keyword" + f"{i}"])


    # validate the form data
    if not Song.validate_song(data, keyword_ids):
        return redirect("/new_song")

    # save the new song to the db
    new_song_id = Song.create_song(data)

    #create many to many links
    for keyword_id in keyword_ids:
        keyword_data = {
            "keyword_id": keyword_id,
            "new_song_id": new_song_id
        }
        Song.create_keyword_link(keyword_data)
        

    # do I want this flash message or nah?
    flash("Song has been added! Keep adding more songs, or return to the dashboard to find your new song.")

    # redirect
    return redirect('/new_song')

# =======================================
# Render Edit One Song
# =======================================


@app.route('/song/<int:song_id>')
def show_one_song(song_id):
    if "user_id" not in session:
        flash("You have to login or register before entering! no sneaking in!!")
        return redirect("/")

    data = {
        "song_id" : song_id,
        "user_id": session["user_id"]
    }

    user = User.get_by_id(data)

    all_composers = Composer.get_all_composers(data)

    all_sources = Source.get_all_sources(data)

    all_albums = Album.get_all_albums(data)

    # all_keywords = Keyword.get_all_keywords(data)

    # all_mediums = Medium.get_all_mediums()

    song = Song.get_one_song(data)

    return render_template("edit_song.html", song=song, all_composers=all_composers, all_sources=all_sources, all_albums=all_albums, user=user)


# =======================================
# Process Edit One Song
# =======================================

@app.route('/song/edit/<int:song_id>/process', methods=['POST'])
def edit_song_process(song_id):

    data = {
        "title": request.form["title"],
        "user_id": request.form["user_id"],
        "audio": request.form.get("audio"),
        "composer": request.form["composer"],
        "source": request.form["source"],
        "album": request.form["album"],
        "song_id": song_id
    }

    # save the new song to the db
    Song.create_song(data)

    # do I want this flash message or nah?
    flash("Song has been added! Keep adding more songs, or return to the dashboard to find your new song.")

    # redirect
    return redirect(f'/song/{song_id}')