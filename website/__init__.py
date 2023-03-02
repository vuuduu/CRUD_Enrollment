# name: __init__.py
# desc: This initialize the website, flask app, and make the website folder a python package  

# import libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# initializing the database object
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'a;slkdvalksjfaosjdal;skdjoiasjef'

    # My Sqlite data base is store the the f'sqlite:///{DB_NAME}' location. Which will be in the website folders
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # importing and registering the views after adding the route
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    # checking to see if we have our database load in yet
    from .models import Student, Instructor, Course, Enrollment
    create_database(app)

    return app

# check if the database already exist. Yes = Not create new database, No = Create new database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
