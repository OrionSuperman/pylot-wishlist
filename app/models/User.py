""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
from flask import session

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def set_new_user(self, user_info):

            errors = []
            query = "SELECT * FROM users WHERE username='{}'".format(user_info['username'])
            exists = self.db.query_db(query)
            if not user_info['username']:
                errors.append('Username cannot be blank')
            elif len(user_info['username']) < 2:
                errors.append('Username must be at least 2 characters long') 
            elif exists:
                errors.append('Username is in use, please choose another')

            if not user_info['name']:
                errors.append('Name cannot be blank')
            elif len(user_info['name']) < 2:
                errors.append('Name must be at least 2 characters long')   

            if not user_info['password']:
                errors.append('Password must not be blank')
            elif len(user_info['password']) < 8:
                errors.append('Password must be at least 8 characters long')
            elif user_info['password'] != user_info['pw_check']:
                errors.append('Passwords must match!')

            if errors:
                return {'status':False, 'errors':errors}
            else:
                pw_hash = self.bcrypt.generate_password_hash(user_info['password'])
                query = "INSERT INTO users (name, username, pass_hash, date_hired, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(user_info['name'], user_info['username'], pw_hash, user_info['date_hired'])
                self.db.query_db(query)
                id_query = "SELECT * FROM users WHERE username='{}' LIMIT 1".format(user_info['username'])
                user=self.db.query_db(id_query)
                session['user_id'] = user[0]['id']
                session['username'] = user[0]['username']
                return {'status':True, 'user':user[0]}

    def get_login_check(self, info):
        query = "SELECT * FROM users WHERE username='{}'".format(info['username'])
        user = self.db.query_db(query)
        if user:
            pass_hash = user[0]['pass_hash']
            password = info['password']

            if self.bcrypt.check_password_hash(pass_hash, password):
            
                session['user_id'] = user[0]['id']
                session['username'] = user[0]['username']

                return {'status':True}
            else:
                return {'status':False}
        else:
            return {'status': False}