from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data["id"]

        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

#================================================================
#Static Methods
#================================================================

    @staticmethod
    def validate_register(data):
        is_valid = True

        if len(data["first_name"]) < 2:
            flash("First name must be at least 2 characters long!")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last name must be at least 2 characters long!")
            is_valid = False

        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email!")
            is_valid = False
        if User.get_by_email(data):
            flash("Email already in use! Please register new email or login!")
            is_valid = False

        if len(data["password"]) < 5:
            flash("Password must be at least 5 characters long!")
            is_valid = False
        if data["password"] != data["conf_pass"]:
            flash("Password must match password confirmation!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):

        is_valid = True

        user_from_db = User.get_by_email(data)

        if not user_from_db:
            flash("Invalid Email/Password")
            is_valid = False
        
        elif not bcrypt.check_password_hash(user_from_db.password, data['password']):
            flash("Invalid Email/Password")
            is_valid = False


        return is_valid

#================================================================
#Class Methods
#================================================================

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recipes_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False
            
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL("recipes_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False

        return cls(result[0])

    @classmethod
    def create_user(cls, data):
        #no password confirmation here! that's not part of the database
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW())"

        results = connectToMySQL("recipes_schema").query_db(query,data)

        #insert queries return an ID, so results are just a single ID of the newly created user
        return results