from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Album:
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
    def validate_album(data):
        is_valid = True

        if len(data['title']) < 2:
            flash("Album's title must be at least 2 characters")
            is_valid = False

        if Album.get_album_by_title(data):
            flash("That album is already in your database!")
            is_valid = False
        

        return is_valid

#================================================================
#Class Methods
#================================================================

    @classmethod
    def create_album(cls, data):
        query = "INSERT INTO albums (title, user_id, created_at) VALUES (%(title)s, %(user_id)s, NOW() )"

        results = connectToMySQL("music_schema").query_db(query,data)

        #returns the ID of the new album
        return results

    @classmethod
    def get_all_albums(cls, data):
        query = "SELECT * FROM albums WHERE albums.user_id = %(user_id)s ORDER BY title ASC"

        results = connectToMySQL("music_schema").query_db(query, data)

        return results

    @classmethod
    def get_album_by_title(cls,data):
        query = "SELECT * FROM albums WHERE title = %(title)s AND user_id = %(user_id)s"
        result = connectToMySQL("music_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False
            
        return cls(result[0])