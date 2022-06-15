from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Composer:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.user= {}
        self.songs = []

#================================================================
#Static Methods
#================================================================

    @staticmethod
    def validate_composer(data):
        is_valid = True

        if isinstance(data['name']) == False:
            flash("Please select a composer from the list.")
            is_valid = False

        if len(data['name']) < 2:
            flash("Composer's name must be at least 2 characters")
            is_valid = False

        if Composer.get_composer_by_name(data):
            flash("That composer is already in your database!")
            is_valid = False
        

        return is_valid

#================================================================
#Class Methods
#================================================================

    @classmethod
    def create_composer(cls, data):
        query = "INSERT INTO composers (name, user_id, created_at) VALUES (%(name)s, %(user_id)s, NOW() )"

        results = connectToMySQL("music_schema").query_db(query,data)

        #returns the ID of the new composer
        return results

    @classmethod
    def get_all_composers(cls, data):
        query = "SELECT * FROM composers WHERE composers.user_id = %(user_id)s ORDER BY name ASC"

        results = connectToMySQL("music_schema").query_db(query, data)

        return results

    @classmethod
    def get_composer_by_name(cls,data):
        query = "SELECT * FROM composers WHERE name = %(name)s AND user_id = %(user_id)s"
        result = connectToMySQL("music_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False
            
        return cls(result[0])