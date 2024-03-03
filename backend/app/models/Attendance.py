from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Attendance(db.Model):
    __tablename__ = 'ATTENDANCE'
    AttendanceID = db.Column(db.String(255), primary_key=True)
    ClassMeetingID = db.Column(db.String(255), db.ForeignKey('CLASSMEETINGS.ClassMeetingID'))
    StudentID = db.Column(db.String(255), db.ForeignKey('USERS.UserID'))
    AttendanceStatus = db.Column(db.String(255))