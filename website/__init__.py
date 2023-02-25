# name: __init__.py
# description: This initialize the website, flask app, and make the website folder a python package  

# import libraries
from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'a;slkdvalksjfaosjdal;skdjoiasjef'

    # importing and registering the views after adding the route
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
