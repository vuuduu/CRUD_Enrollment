# Name: views.py
# Description: This holds all the functionality and information of the website like student, instructor, courses, and enrollment

# import libraries
from flask import Blueprint, render_template, request, flash, redirect, jsonify
from .models import *
from . import db # means from __init__.py import db
import random
import json

# defining the blueprints for views file (how the website would function/look)
views = Blueprint('views', __name__)

# student will be the home page
@views.route('/', methods=['GET', 'POST'])
def student():
    # retrieving data that was part of a form. In this case, I've get: studentId, studentName, creditEarned
    if request.method == 'POST':
        studentId = request.form.get('studentId')
        studentName = request.form.get('studentName')
        creditEarned = request.form.get('creditEarned')

        # check to see if the information user enter is valid
        if len(studentId) < 3:
            flash("Invalid student's id. Must be 3 digit number!", category="error")
        elif len(studentName) < 2:
            flash("Student's name must have at least 2 characters!", category="error")
        elif len(creditEarned) < 1:
            flash("Student's credit must be at least 1 characters, preferabably a number!", category="error")
        else:
            # check to see if the student already exist
            existingStudent = Student.query.filter_by(studentId=studentId).first()
            if existingStudent:
                flash("Must enter a unique id!", category="error")
            else:
            # adding new student to the database
                newStudent = Student(studentId=studentId, studentName=studentName, creditEarned=creditEarned)
                db.session.add(newStudent)
                db.session.commit()
                flash("Student sucessfully added!", category="success")
    # retrieving all the students in the database
    students = Student.query.all()
    return render_template("student.html", students=students)

@views.route('/instructor', methods=['GET', 'POST'])
def instructor():
    # retrieving data that was part of a form. instructorId, instructorName, department
    if request.method == 'POST':
        instructorId = request.form.get('instructorId')
        instructorName = request.form.get('instructorName')
        department = request.form.get('department')

        # check to see if the information user enter is valid
        if len(instructorId) < 3:
            flash("Invalid instructor's id. Must be 3 digit number!", category="error")
        elif len(instructorName) < 2:
            flash("Instructor's name must have at least 2 characters!", category="error")
        elif len(department) < 1:
            flash("Instructor's department must be at least 1 characters!", category="error")
        else:
            # check to see if the instructor already exist
            existingInstructor = Instructor.query.filter_by(instructorId=instructorId).first()
            if existingInstructor:
                flash("ID ALREADY EXIST!", category="error")
            else:
            # adding new student to the database
                newInstructor = Instructor(instructorId=instructorId, instructorName=instructorName, department=department)
                db.session.add(newInstructor)
                db.session.commit()
                flash("Instructor sucessfully added!", category="success")
    # Retrieving all the instructor in the database
    instructors = Instructor.query.all();
    return render_template("instructor.html", instructors=instructors)

@views.route('/course', methods=['GET', 'POST'])
def course():
    # retrieving data that was part of a form. courseId, courseTitle, instructorId
    if request.method == 'POST':
        courseId = request.form.get('courseId')
        courseTitle = request.form.get('courseTitle')
        instructorId = request.form.get('instructorId')
        existingInstructor = Instructor.query.filter_by(instructorId=instructorId).first()

        # check to see if the information user enter is valid
        if len(courseId) < 3:
            flash("Invalid course's id. Must be 3 digit number!", category="error")
        elif len(courseTitle) < 2:
            flash("Course's title must have at least 2 characters!", category="error")
        else:
            # check to see if the instructor exist, if not pass a string of TBA to newCourse
            if not existingInstructor:
                instructorId = "TBA"
            newCourse = Course(courseId=courseId, courseTitle=courseTitle, instructorId=instructorId)
            db.session.add(newCourse)
            db.session.commit()
            flash("Course sucessfully added!", category="success")
    # Retrieving all the courses from the databases
    courses = Course.query.all()
    return render_template("course.html", courses=courses)

@views.route('/enrollment', methods=['GET', 'POST'])
def enrollment():
    if request.method == 'POST':
        studentId = request.form.get('studentId')
        courseId = request.form.get('courseId')
        existingStudent = Student.query.filter_by(studentId=studentId).first()
        existingCourse = Course.query.filter_by(courseId=courseId).first()
        existingEnrollment = Enrollment.query.filter_by(studentId=studentId, courseId=courseId).first()
        
        if not existingStudent:
            flash("Student does not exist!", category='error')
        elif not existingCourse:
            flash("Course does not exist!", category='error')
        elif existingEnrollment:
            flash("This student is already enrolled in this course!", category='error')
        else:
            # Creating new enrollment
            grade = random.choice(['A', 'B', 'C', 'D', 'F'])
            newEnrollment = Enrollment(studentId=studentId, courseId=courseId, grade=grade)
            db.session.add(newEnrollment)
            db.session.commit()
            flash("Successfully Enroll!", category='success')
            
    enrollments = Enrollment.query.all()
    return render_template("enrollment.html", enrollments=enrollments)


# Deleting data (student, instructor, courses, and enrollment) from database. 
@views.route('/delete-student', methods=['POST'])
def deleteStudent():
    # turning the jsonify string into dictionary and acessing the id
    student = json.loads(request.data)
    studentId = student['studentId']
    student = Student.query.get(studentId) # grabbing the studentId from database

    db.session.delete(student)
    db.session.commit()

    return jsonify({})

@views.route('/delete-instructor', methods=['POST'])
def deleteInstructor():
    # turning the jsonify string into dictionary and acessing the id
    instructor = json.loads(request.data)
    instructorId = instructor['instructorId']
    instructor = Instructor.query.get(instructorId) # grabbing the instructor from database
    # condition to check if the instructor is still teaching a class.
    db.session.delete(instructor)
    db.session.commit()
    flash("Successfully remove an instructor.", category='success')

    return jsonify({})

@views.route('/delete-course', methods=['POST'])
def deleteCourse():
    # turning the jsonify string into dictionary and acessing the id
    course = json.loads(request.data)
    print("TESTING ===========", course)
    courseId = course['courseId']
    print("TESTING ===========", courseId)
    course = Course.query.get(courseId) # grabbing the instructor from database
    print("TESTING ===========", course) 
    # condition to check if the instructor is still teaching a class.
    db.session.delete(course)
    db.session.commit()
    flash("Successfully remove an instructor.", category='success')

    return jsonify({}) 

@views.route('/delete-enrollment', methods=['POST'])
def deleteEnrollment():
    enrollment = json.loads(request.data)
    enrollmentId = enrollment['enrollmentId']
    enrollment = Enrollment.query.filter_by(id=enrollmentId).first()
    # check if the enrollment record exists
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        flash("Successfully deleted enrollment.", category='success')
    else:
        flash("Enrollment record does not exist.", category='error')

    return jsonify({})