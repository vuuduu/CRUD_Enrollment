# Name: views.py
# Description: This holds all the functionality and information of the website like student, instructor, courses, and enrollment

# import libraries
from flask import Blueprint

# defining the blueprints for views file (how the website would function/look)
views = Blueprint('views', __name__)

@views.route('/student')
def student():
    return "<h1>STUDENT Page</h1>"

@views.route('/instructor')
def instructor():
    return "<h1>Instructor Page</h1>"

@views.route('/course')
def course():
    return "<h1>Course Page</h1>"

@views.route('/enrollment')
def enrollment():
    return "<h1>Enrollment Page</h1>"


