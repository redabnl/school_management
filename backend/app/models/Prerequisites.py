from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Prerequisites(db.Model):
    __tablename__ = 'PREREQUISITES'
    PrerequisiteID = db.Column(db.String(255), primary_key=True)
    CourseID = db.Column(db.String(255), db.ForeignKey('COURSES.CourseID'))
    PrerequisiteCourseID = db.Column(db.String(255), db.ForeignKey('COURSES.CourseID'))
