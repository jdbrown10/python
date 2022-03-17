# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User: 
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database


#=================================
# Select all of the users
#=================================
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users

#=================================
# Select one of the users
#=================================

    @classmethod
    def get_one_user(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(user_id)s"

        result = connectToMySQL('users_schema').query_db(query, user_id)

        return cls(result[0])

#=================================
# Update data of one user
#=================================

    @classmethod
    def edit_one_user(cls, data):

        #The hidden input in the form is passing the user_ID into this query
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(eml)s, updated_at=NOW() WHERE id=%(id)s"


        return connectToMySQL('users_schema').query_db(query, data)
    
#===================================
# Create a new user (returns the ID)
#===================================

    @classmethod
    def save(cls, data):
        
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(eml)s , NOW() , NOW() );"

        return connectToMySQL('users_schema').query_db( query, data )

#===================================
# Delete a new user -->(FOREVER)<--
#===================================

    @classmethod
    def delete_user(cls, data):

        query = "DELETE FROM users WHERE id = %(id)s"
        
        return connectToMySQL('users_schema').query_db( query, data )
