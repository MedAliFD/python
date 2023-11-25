from flask_app.config.mysqlconnection import connectToMySQL, DB

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# Method that will get all rows of the table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DB).query_db(query)
        users = []
        for row in results:
            user = cls(row)
            users.append(user)
        # Burgers = [instance_1 , instance_2]
        return users
