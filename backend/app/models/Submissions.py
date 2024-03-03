from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class Submissions(db.Model):
    __tablename__ = 'SUBMISSIONS'
    SubmissionID = db.Column(db.String(255), primary_key=True)
    HomeworkID = db.Column(db.String(255), db.ForeignKey('HOMEWORKS.HomeworkID'))
    StudentID = db.Column(db.String(255), db.ForeignKey('USERS.UserID'))
    Timestamp = db.Column(db.DateTime)
    FileLink = db.Column(db.Text)
    Grade_Status = db.Column(db.String(255))