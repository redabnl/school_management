from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class CourseOfferings(db.Model):
    __tablename__ = 'COURSEOFFERINGS'
    OfferingID = db.Column(db.String(255), primary_key=True)
    CycleID = db.Column(db.String(255), db.ForeignKey('ACADEMICCYCLES.CycleID'))
    CourseID = db.Column(db.String(255), db.ForeignKey('COURSES.CourseID'))
    ProfessorID = db.Column(db.String(255), db.ForeignKey('USERS.UserID'))
