import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    name = Column(String(80), nullable=False)
    description = Column(String(250))
    id = Column(Integer, primary_key=True)


class ClassInfo(Base):
    __tablename__ = 'classinfo'

    name = Column(String(80), nullable=False)
    teacher = Column(String(80))
    time = Column(DateTime, nullable=False)
    price = Column(String(8))
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship(Course)

class Student(Base):
    __tablename__ = 'student'

    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    phone = Column(Integer)
    signed = Column(Boolean)
    id = Column(Integer, primary_key=True)
    classinfo_id = Column(Integer, ForeignKey('classinfo.id'))
    classinfo = relationship(ClassInfo)



engine = create_engine('sqlite:///school.db')

Base.metadata.create_all(engine)
