from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
from flask_app.models import book

class Favorite: 
    def __init__( self , data ):
        self.author_id = data['author_id']
        self.book_id = data['book_id']

    @classmethod
    def create_link(cls, data):
        
        query = "INSERT INTO favorites ( author_id, book_id ) VALUES ( %(author_id)s, %(book_id)s);"

        return connectToMySQL('books_schema').query_db( query, data )