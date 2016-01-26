"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import session

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
      
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        return self.load_view('index.html')

    def logout(self):
        session.clear()
        return redirect('/')

    def create(self):
        format_user = {
        "name" : request.form['name'],
        "username" : request.form['username'],
        "password" : request.form['password'],
        "pw_check" : request.form['pw_check'],
        "date_hired" : request.form['date_hired']
        }
        user_info = self.models['User'].set_new_user(format_user)
        print user_info
        if user_info['status'] == True:
            return redirect('/dashboard')
        else:
            for message in user_info['errors']:
                flash(message, 'regis_errors')
            return redirect('/')
    def submitlogin(self):

        user_info = {
        'username': request.form['username'],
        'password' : request.form['password']
        }
        user = self.models['User'].get_login_check(user_info)

        if user['status'] == True:
            id = session['user_id']
            return redirect('/dashboard')
        else:
            flash('Email or password incorrect.')
            return redirect('/')