from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
import re

bcrypt = Bcrypt(app)


class User():

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls , data):
        print(data['password'])
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encrypted_password
        query = "INSERT INTO users (first_name, last_name , email , password) VALUES (%(first_name)s ,%(last_name)s , %(email)s , %(password)s);"
        return connectToMySQL(DB).query_db(query, data)

    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not User.EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("You are using the wrong format of an email")
        if not user_in_db:
            is_valid = False
            flash("email doesn't exist", "login")
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            is_valid = False
            flash("Incorrect Password", "login")
        return is_valid

    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['first_name']) <= 2:
            flash("first name doesn't respect rules", "register")
            is_valid = False
        if len(data['last_name']) <= 2:
            flash("last name doesn't respect rules", "register")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be longer than 8 characters.", "register")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("please confirm your password correctly", "register")
            is_valid = False
        if user_in_db:
            flash("this email already used.", "register")
            is_valid = False
        if not User.EMAIL_REGEX.match(data['email']):
            flash("Email rules not respected")
            is_valid = False
            
        return is_valid

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            return cls(result[0])
        return False
