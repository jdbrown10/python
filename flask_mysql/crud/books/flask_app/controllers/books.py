from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

# ================================
# RENDER ALL BOOKS
# ================================

@app.route("/books")
def create_book(): 

    books = Book.get_all_books()
    return render_template("books.html", books=books)



# ================================
# PROCESS CREATE BOOK
# ================================

@app.route("/create_book", methods=['POST'])
def create_book_process(): 

    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"],
    }

    Book.create_book(data)

    return redirect('/books')


# ================================
# RENDER SHOW ONE BOOK
# ================================

@app.route("/books/<int:book_id>")
def book_show(book_id):

    data = {
        "book_id" : book_id
    }

    one_book = Book.get_book_with_authors(data)

    authors = Author.get_all_authors()

    return render_template("show_book.html", one_book = one_book, authors=authors)

# ================================
# PROCESS LINKING AUTHOR TO BOOK
# ================================

@app.route("/create_link/book", methods=['POST'])
def create_link_book(): 


    data = {
        "author_id": request.form["author_id"],
        "book_id": request.form["book_id"]
    }

    #if book ID is equal to existing book ID, then alert (this author has already favorited that book)

    Favorite.create_link(data)

    return redirect(f'/books/{request.form["book_id"]}')