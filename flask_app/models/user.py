from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add(cls, data):
        query = "INSERT INTO users (email) VALUES (%(email)s);"
        result = connectToMySQL('email_schema').query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = "select * from users;"
        results = connectToMySQL('email_schema').query_db(query)
        users = []
        for row in results:
            users.append(User(row))
        return users

    @ classmethod
    def delete(cls, data):
        query = "Delete FROM users where users.id = %(id)s;"
        return connectToMySQL('email_schema').query_db(query, data)

    @staticmethod
    def validate_email(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        else:
            flash("The Email Address you Entered is a VALID email address thank you!")
            is_valid = True
        return is_valid
