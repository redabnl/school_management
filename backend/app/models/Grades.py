from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Grades(db.Model):
    __tablename__ = 'GRADES'
    GradeID = db.Column(db.String(255), primary_key=True)
    StudentID = db.Column(db.String(255), db.ForeignKey('USERS.UserID'))
    OfferingID = db.Column(db.String(255), db.ForeignKey('COURSEOFFERINGS.OfferingID'))
    NumericGrade = db.Column(db.Integer)
    LetterGrade = db.Column(db.String(255))