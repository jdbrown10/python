from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Author: 
    db = "books_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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