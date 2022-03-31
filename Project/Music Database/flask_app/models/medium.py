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
#Class Methods
#================================================================
    @classmethod
    def get_all_mediums(cls):
        query = "SELECT * FROM mediums ORDER BY type ASC"

        results = connectToMySQL("music_schema").query_db(query)

        return results