from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.author import Author
from flask_app.models.book import Book

# ================================
# RENDER ALL AUTHORS
# ================================

@app.route("/authors")
def index():
    authors = Author.get_all_authors()
    print(authors)
    return render_template("authors.html", authors=authors)


# ================================
# PROCESS CREATE AUTHOR
# ================================

@app.route("/create_author", methods=['POST'])
def create_user_process(): 

    data = {
        "name": request.form["name"],
    }

    Author.create_author(data)

    return redirect('/authors')