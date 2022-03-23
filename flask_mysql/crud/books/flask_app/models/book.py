from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book: 
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = [] #placeholder for related data -- a book will have a list of authors attached

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"

        results = connectToMySQL('books_schema').query_db(query)

        books = []

        for book in results:
            books.append( cls(book) )

        return books

    @classmethod
    def create_book(cls, data):
        
        query = "INSERT INTO books ( title, num_of_pages, created_at, updated_at ) VALUES ( %(title)s, %(num_of_pages)s, NOW() , NOW() );"

        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_book_with_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors on favorites.author_id = authors.id WHERE books.id = %(book_id)s;"

        results = connectToMySQL('books_schema').query_db( query, data)

        book = cls(results[0]) #create instance of author to get the books for

        for data in results: #loop to get all the books

            author_data = {
                "id": data['authors.id'],
                "name": data['name'],
                "created_at": data['authors.created_at'],
                "updated_at": data['authors.updated_at']
            }
            
            author_instance = author.Author(author_data)

            book.authors.append(author_instance)

        return book