from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user

class Recipe:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.description = data["description"]
        self.under_30 = data["under_30"]
        self.instructions = data["instructions"]
        self.user_id = data["user_id"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        #this is a dictionary so it's a single object (because a recipe only has one user -- if it needed to contain the many side of a relationship, it could be a list)
        self.user = {}

#================================================================
#Static Methods
#================================================================

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 2:
            flash("Recipe must be at least 2 characters")
            is_valid = False
        if len(data['description']) < 2:
            flash("Description must be at least 2 characters")
            is_valid = False
        if (data['under_30'] != 'yes' and data['under_30'] != 'no'):
            flash("Under 30 must be either yes or no!")
            is_valid = False
        if len(data['instructions']) < 2:
            flash("Instructions must be at least 2 characters")
            is_valid = False
        

        return is_valid

#================================================================
#Class Methods
#================================================================

    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, under_30, instructions, user_id, created_at) VALUES (%(name)s, %(description)s, %(under_30)s, %(instructions)s, %(user_id)s, NOW() )"

        results = connectToMySQL("recipes_schema").query_db(query,data)

        #returns the ID of the new recipe
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL("recipes_schema").query_db(query)

        all_recipes = []

        for row in results:
            recipe = cls(row)

            user_data = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"],
            }

            recipe.user = user.User(user_data)

            all_recipes.append(recipe)

        return all_recipes

    @classmethod
    def get_recipe_with_user(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(recipe_id)s;"

        results = connectToMySQL("recipes_schema").query_db(query, data)

        recipe = cls(results[0])

        user_data = {
            "id" : results[0]["users.id"],
            "first_name" : results[0]["first_name"],
            "last_name" : results[0]["last_name"],
            "email" : results[0]["email"],
            "password" : results[0]["password"],
            "created_at" : results[0]["users.created_at"],
            "updated_at" : results[0]["users.updated_at"],
        }

        recipe.user = user.User(user_data)

        return recipe

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, under_30 = %(under_30)s, instructions = %(instructions)s, updated_at = NOW() WHERE id = %(recipe_id)s"

        results = connectToMySQL("recipes_schema").query_db(query, data)

        #update queries don't return anything so just return to end the function
        return

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s"

        results = connectToMySQL("recipes_schema").query_db(query, data)

        return