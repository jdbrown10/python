from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Keyword:
    def __init__(self, data):
        self.id = data["id"]

        self.type = data["type"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.songs = []

#================================================================
#Static Methods
#================================================================

    @staticmethod
    def validate_keyword(data):
        is_valid = True

        if len(data['type']) < 2:
            flash("Keyword must be at least 2 characters.")
            is_valid = False

        if Keyword.get_keyword_by_type(data):
            flash("That keyword is already in your database!")
            is_valid = False
        

        return is_valid

#================================================================
#Class Methods
#================================================================

    @classmethod
    def create_keyword(cls, data):
        query = "INSERT INTO keywords (type, user_id, created_at) VALUES (%(type)s, %(user_id)s, NOW() )"

        results = connectToMySQL("music_schema").query_db(query,data)

        #returns the ID of the new composer
        return results

    @classmethod
    def get_all_keywords(cls, data):
        query = "SELECT * FROM keywords WHERE keywords.user_id = %(user_id)s ORDER BY type ASC"

        results = connectToMySQL("music_schema").query_db(query, data)

        return results

    @classmethod
    def get_keyword_by_type(cls,data):
        query = "SELECT * FROM keywords WHERE type = %(type)s AND user_id = %(user_id)s"
        result = connectToMySQL("music_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False
            
        return cls(result[0])