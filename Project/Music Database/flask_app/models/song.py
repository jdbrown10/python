from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import album
from flask_app.models import composer
from flask_app.models import source

# model the class after the song table from our database
class Song: 
    db = "music_schema"
    def __init__( self , data ):
        self.id = data['id']

        self.title = data['title']
        self.audio = data['audio']

        self.user_id = data["user_id"]
        self.composer_id = data["composer_id"]
        self.album_id = data["album_id"]
        self.source_id = data["source_id"]

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.composer = {}
        self.album = {}
        self.source = {}

        self.keywords = [] #placeholder for related data

#================================================================
#Static Methods
#================================================================

    @staticmethod
    def validate_song(data, keyword_ids):
        is_valid = True

        if len(data['title']) < 2:
            flash("Song's title must be at least 2 characters")
            is_valid = False

        # if len(data['audio']) < 1:
        #     flash("Song must have an audio file!")
        #     is_valid = False

        #gotta build this method- get song with keyword ID
        # for keyword_id in keyword_ids:
        #     if Song.get_song_with_keyword_id(keyword_id):
        #         flash("That song already has one of those keywords!")
        #         is_valid = False

        return is_valid

#================================================================
#Class Methods
#================================================================

    @classmethod
    def create_song(cls, data):
        query = "INSERT INTO songs (title, audio, user_id, created_at, composer_id, source_id, album_id) VALUES ( %(title)s, %(audio)s, %(user_id)s, NOW(), %(composer)s, %(source)s, %(album)s )"

        results = connectToMySQL('music_schema').query_db( query, data )

        #returns the ID of the new song that was created
        return results

    @classmethod
    def create_keyword_link(cls, keyword_data):
        query = "INSERT INTO songs_keywords ( song_id, keyword_id ) VALUES ( %(new_song_id)s, %(keyword_id)s )"

        return connectToMySQL('music_schema').query_db( query, keyword_data )

    @classmethod
    def get_all_songs(cls, data):
        query = "SELECT * FROM songs LEFT JOIN composers ON songs.composer_id = composers.id LEFT JOIN albums ON songs.album_id = albums.id LEFT JOIN sources ON songs.source_id = sources.id WHERE songs.user_id = %(user_id)s;"
        results = connectToMySQL("music_schema").query_db(query, data)

        all_songs = []

        for row in results:
            song = cls(row)

            composer_data = {
                "id" : row["composers.id"],
                "name" : row["name"],
                "created_at" : row["composers.created_at"],
                "updated_at" : row["composers.updated_at"]
            }

            album_data = {
                "id" : row["albums.id"],
                "title" : row["albums.title"],
                "created_at" : row["albums.created_at"],
                "updated_at" : row["albums.updated_at"]
            }

            source_data = {
                "id" : row["sources.id"],
                "title" : row["sources.title"],
                "created_at" : row["sources.created_at"],
                "updated_at" : row["sources.updated_at"]
            }

            song.composer = composer.Composer(composer_data)
            song.album = album.Album(album_data)
            song.source = source.Source(source_data)

            all_songs.append(song)

        return all_songs