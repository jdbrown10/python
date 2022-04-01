from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# model the class after the friend table from our database
class Song: 
    db = "music_schema"
    def __init__( self , data ):
        self.id = data['id']

        self.title = data['title']
        self.audio = data['audio']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.keywords = [] #placeholder for related data

        self.composer = {}
        self.album = {}
        self.source = {}

# #================================================================
# #Static Methods
# #================================================================

#     @staticmethod
#     def validate_song(data, keyword_ids):
#         is_valid = True

#         if len(data['title']) < 2:
#             flash("Song's title must be at least 2 characters")
#             is_valid = False

#         if len(data['file']) < 1:
#             flash("Song must have a file!")
#             is_valid = False

#         for keyword_id in keyword_ids:
#             if Song.get_song_with_keyword_id(keyword_id):
#                 flash("That song already has one of those keywords!")
#                 is_valid = False
        

#         return is_valid

# #================================================================
# #Class Methods
# #================================================================

#     @classmethod
#     def create_song(cls, data):
        
        
#         query = "INSERT INTO songs ( title, audio, created_at, composer_id, source_id, album_id) VALUES ( %(title)s, %(audio)s), NOW(), %(composer_id)s, %(source_id)s, %(album_id)s, %(keyword_id)s ;"




#         #loop here using counter variable to create keyword tables



#         return connectToMySQL('music_schema').query_db( query, data )

#     @classmethod
#     def get_song_with_keyword_id(cls, data):

#         #need to build this out still...