from classes_keeper import app
from flask import render_template, redirect, url_for, request
from classes_keeper.database_setup import Base, Course, ClassInfo
from classes_keeper.db import session


@app.route('/courses/<int:course_id>/')
def showClasses(course_id):
    course = session.query(Course).filter_by(id=course_id).first()
    classes = session.query(ClassInfo).filter_by(course_id=course_id).all()

    return render_template('classes.html', classes=classes, course=course, course_id=course_id)


@app.route('/courses/<int:course_id>/new/', methods=['GET', 'POST'])
def newClass(course_id):
    if request.method == 'POST':
        newClass = ClassInfo(name=request.form['name'],
                             teacher=request.form['teacher'],
                             schedule=request.form['schedule'],
                             price=request.form['price'],
                             course_id=course_id)
        session.add(newClass)
        session.commit()

        return redirect(url_for('showClasses', course_id=course_id))

    else:
        return render_template('new_class.html', course_id=course_id)

@app.route('/courses/<int:course_id>/classes/<int:class_id>/edit',
           methods=['GET', 'POST'])
def editClass(course_id, class_id):
    editedClass = session.query(ClassInfo).filter_by(id=class_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedClass.name = request.form['name']

        if request.form['teacher']:
            editedClass.teacher = request.form['teacher']

        if request.form['schedule']:
            editedClass.schedule= request.form['schedule']

        if request.form['price']:
            editedClass.price= request.form['price']

        session.add(editedClass)
        session.commit()

        return redirect(url_for('showClasses', course_id=course_id))

    else:
        return render_template('edit_class.html',
                               course_id=course_id,
                               class_id=class_id,
                               classinfo=editedClass)

@app.route('/courses/<int:course_id>/classes/<int:class_id>/delete',
           methods=['GET', 'POST'])
def deleteClass(course_id, class_id):
    deletedClass = session.query(ClassInfo).filter_by(id=class_id).one()

    if request.method == 'POST':
        session.delete(deletedClass)
        session.commit()

        return redirect(url_for('showClasses', course_id=course_id))

    else:
        return render_template('delete_class.html',
                               course_id=course_id,
                               classinfo=deletedClass)
