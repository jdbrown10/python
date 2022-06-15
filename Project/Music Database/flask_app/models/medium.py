from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Medium:
    def __init__(self, data):
        self.id = data["id"]

        self.type = data["name"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.sources = []

#================================================================
#Static Methods
#================================================================

    @staticmethod
    def validate_medium(data):
        is_valid = True

        if isinstance(data['type']) == False:
            flash("Please select a composer from the list.")
            is_valid = False

        if len(data['type']) < 2:
            flash("Medium must be at least 2 characters")
            is_valid = False

        if Medium.get_medium_by_type(data):
            flash("That medium is already in your database!")
            is_valid = False
        

        return is_valid

#================================================================
#Class Methods
#================================================================
    @classmethod
    def create_medium(cls, data):
        query = "INSERT INTO mediums (type, user_id, created_at) VALUES (%(type)s, %(user_id)s, NOW() )"

        results = connectToMySQL("music_schema").query_db(query,data)

        #returns the ID of the new composer
        return results
    
    @classmethod
    def get_all_mediums(cls):
        query = "SELECT * FROM mediums ORDER BY type ASC"

        results = connectToMySQL("music_schema").query_db(query)

        return results

    @classmethod
    def get_medium_by_type(cls,data):
        query = "SELECT * FROM mediums WHERE type = %(type)s AND user_id = %(user_id)s"
        result = connectToMySQL("music_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False
            
        return cls(result[0])