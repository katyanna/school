from classes_keeper import app
from flask import render_template, redirect, url_for, request
from classes_keeper.database_setup import Base, Course, ClassInfo
from classes_keeper.db import session


@app.route('/')
@app.route('/courses/')
def showCourses():
    courses =  session.query(Course).all()

    return render_template('courses.html', courses=courses)


@app.route('/courses/new/', methods=['GET', 'POST'])
def newCourse():
    if request.method == 'POST':
        newCourse = Course(name=request.form['name'],
                           description=request.form['description'])
        session.add(newCourse)
        session.commit()

        return redirect(url_for('showCourses'))

    else:
        return render_template('new_course.html')

@app.route('/courses/<int:course_id>/edit', methods=['GET', 'POST'])
def editCourse(course_id):
    editedCourse = session.query(Course).filter_by(id=course_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCourse.name = request.form['name']

        if request.form['description']:
            editedCourse.description = request.form['description']

        session.add(editedCourse)
        session.commit()

        return redirect(url_for('showCourses'))

    else:
        return render_template('edit_course.html',
                               course_id=course_id,
                               course=editedCourse)

@app.route('/courses/<int:course_id>/delete', methods=['GET', 'POST'])
def deletedCourse(course_id):
    deletedCourse = session.query(Course).filter_by(id=course_id).one()

    if request.method == 'POST':
        session.delete(deletedCourse)
        session.commit()

        return redirect(url_for('showCourses'))

    else:
        return render_template('delete_course.html',
                               course_id=course_id,
                               course=deletedCourse)
