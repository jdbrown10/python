# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Dojo: 
    db = "dojos_and_ninjas_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )

        return dojos


    #WHOOPS- so, I'm adding this comment welllll after submitting this assignment. Parsing data went completely over my head when I originally worked on this, and instead I figured out a way to make the functionality work without actually relating the tables together in a single method. I didn't even realize I was doing something strange at the time-- I was just like, "huh, I guess I don't need all that parsing stuff for this part? That seems weird." Now I realize that was NOT the proper way to do this, lol-- so it's on my agenda to come back and fix it soon.
    @classmethod
    def get_certain_dojo_name(cls, dojo_id):
        query = "SELECT name FROM dojos WHERE id = %(dojo_id)s"

        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, dojo_id)

        return result[0]

    @classmethod
    def create_dojo(cls, data):
        
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"

        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )