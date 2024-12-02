"""
the auth routes for our baseball_app
"""

from flask import Blueprint, render_template


auth = Blueprint('auth', __name__, template_folder='../../templates/auth')


@auth.route('/')
def index():
    return render_template('index.html')

@auth.route('/profile')
def profile():
    return render_template('profile.html')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'logout'