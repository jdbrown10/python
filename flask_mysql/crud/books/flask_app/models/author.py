from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
# model the class after the friend table from our database
class Author: 
    db = "books_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = [] #placeholder for related data -- an author will have a list of books attached

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"

        results = connectToMySQL('books_schema').query_db(query)

        authors = []

        for author in results:
            authors.append( cls(author) )

        return authors

    @classmethod
    def create_author(cls, data):
        
        query = "INSERT INTO authors ( name , created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"

        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_certain_author_name(cls, dojo_id):
        query = "SELECT name FROM authors WHERE id = %(author_id)s"

        result = connectToMySQL('books_schema').query_db(query, dojo_id)

        return result[0]

    @classmethod
    def get_author_with_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books on favorites.book_id = books.id WHERE authors.id = %(author_id)s;"

        results = connectToMySQL('books_schema').query_db( query, data)

        author = cls(results[0]) #create instance of author to get the books for

        for data in results: #loop to get all the books

            book_data = {
                "id" : data['books.id'],
                "title": data["title"],
                "num_of_pages": data['num_of_pages'],
                "created_at": data["books.created_at"],
                "updated_at": data["books.updated_at"]
            }
            
            book_instance = book.Book(book_data)

            author.books.append(book_instance)

        return author