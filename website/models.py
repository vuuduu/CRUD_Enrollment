# name: models.py
# desc: contains all of the schema for our website databases (students, course, instructor, and enrollment)
# Relationship explains:
#       Student has a one-to-many relationship with Enrollment, which means that a Student can have multiple enrollments.
#       Course has a one-to-many relationship with Enrollment, which means that a Course can have multiple enrollments.
#       Instructor has a one-to-many relationship with Course, which means that an Instructor can have multiple courses.
#       Course has a many-to-one relationship with Instructor, which means that a Course can have only one Instructor.

# importing libraries
from . import db
from sqlalchemy.sql import func

# defining data schema for student, course, instructor, and enrollment
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, unique=True)
    studentName = db.Column(db.String(100))
    creditEarned = db.Column(db.Integer)
    # everytime we made a new enrollment add its id to the enrollments of the students (basically a list full of enrollment)
    enrollments = db.relationship('Enrollment')

class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructorId = db.Column(db.Integer, unique=True)
    instructorName = db.Column(db.String(100))
    department = db.Column(db.String(50))
    courses = db.relationship('Course')

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseId = db.Column(db.Integer)
    courseTitle = db.Column(db.String(50))
    instructorId = db.Column(db.Integer, db.ForeignKey('instructor.id'))
    enrollments = db.relationship('Enrollment')

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'))
    courseId = db.Column(db.Integer, db.ForeignKey('course.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    grade = db.Column(db.String(1))

