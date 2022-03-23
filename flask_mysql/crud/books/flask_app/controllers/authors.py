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

# ================================
# RENDER SHOW ONE AUTHOR
# ================================

@app.route("/authors/<int:author_id>")
def author_show(author_id):

    data = {
        "author_id" : author_id
    }

    one_author = Author.get_author_with_books(data)

    books = Book.get_all_books()

    return render_template("show_author.html", one_author = one_author, books=books)

# ================================
# PROCESS LINKING BOOK TO AUTHOR
# ================================

@app.route("/create_link/author", methods=['POST'])
def create_link_author(): 

    data = {
        "author_id": request.form["author_id"],
        "book_id": request.form["book_id"]
    }

    #if book ID is equal to existing book ID, then alert (this author has already favorited that book)

    Author.create_link(data)

    return redirect(f'/authors/{request.form["author_id"]}')