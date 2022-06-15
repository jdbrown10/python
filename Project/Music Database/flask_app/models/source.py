from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Source:
    def __init__(self, data):
        self.id = data["id"]

        self.title = data["title"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.user= {}
        self.songs = []

#================================================================
#Static Methods
#================================================================

    @staticmethod
    def validate_source(data):
        is_valid = True

        if len(data['title']) < 2:
            flash("Source's name must be at least 2 characters")
            is_valid = False

        if Source.get_source_by_title(data):
            flash("That source is already in your database!")
            is_valid = False

        if isinstance(data['type']) == False:
            flash("Please select a composer from the list.")
            is_valid = False
        
        #these are just the IDs from the mediums that I created
        #the user cannot create/edit/delete any mediums on their end, so the values within this list should never change
        if (data['medium_id']) not in ["6", "7", "8", "9"]:
            flash("Your source needs to have a medium!")
            is_valid = False

        return is_valid

#================================================================
#Class Methods
#================================================================

    @classmethod
    def create_source(cls, data):
        query = "INSERT INTO sources (title, user_id, medium_id, created_at) VALUES (%(title)s, %(user_id)s, %(medium_id)s, NOW() )"

        results = connectToMySQL("music_schema").query_db(query,data)

        #returns the ID of the new source
        return results

    @classmethod
    def get_all_sources(cls, data):
        query = "SELECT * FROM sources WHERE sources.user_id = %(user_id)s ORDER BY title ASC"

        results = connectToMySQL("music_schema").query_db(query, data)

        return results

    @classmethod
    def get_source_by_title(cls,data):
        query = "SELECT * FROM sources WHERE title = %(title)s AND user_id = %(user_id)s"
        result = connectToMySQL("music_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False
            
        return cls(result[0])