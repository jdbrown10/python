from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
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
# Static Methods
#================================================================
    @staticmethod
    def validate_register(form_data):
        is_valid = True

        if len(form_data["first_name"]) < 2:
            flash("First name must be at least 2 characters long.")
            is_valid = False

        if len(form_data["last_name"]) < 2:
            flash("Last name must be at least 2 characters long.")
            is_valid = False

        if len(form_data["password"]) < 8:
            flash("Password must be at least 8 characters long.")
            is_valid = False

        if form_data["password"] != form_data["conf_pass"]:
            flash("Password and Password Confirmation must match!")
            is_valid = False

        if not EMAIL_REGEX.match(form_data["email"]):
            flash("Please enter a valid e-mail address... come onnnn. we both know that isn't an e-mail")
            is_valid = False

        return is_valid


    @staticmethod
    def validate_login(form_data):

        is_valid = True

        user_from_db = User.get_by_email(form_data)

        if not user_from_db:
            flash("Invalid Email/Password")
            is_valid = False

        elif not bcrypt.check_password_hash(user_from_db.password, form_data['password']):
            flash("Invalid Email/Password")
            is_valid = False


        return is_valid

#================================================================
# Class Methods
#================================================================

    @classmethod
    def create_user(cls, data):

        #remember INSERT returns an ID
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        results = connectToMySQL('login_and_reg_schema').query_db(query, data)

        return results

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("login_and_reg_schema").query_db(query,data)

        # If there's no matching user:
        if len(result) < 1:
            return False
        return cls(result[0])