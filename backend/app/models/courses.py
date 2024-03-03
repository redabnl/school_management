from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Courses(db.Model):
    __tablename__ = 'COURSES'
    CourseID = db.Column(db.String(255), primary_key=True)
    Name = db.Column(db.String(255))
    Description = db.Column(db.Text)
    nbHours = db.Column(db.Integer)