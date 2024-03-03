from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class ClassMeetings(db.Model):
    __tablename__ = 'CLASSMEETINGS'
    ClassMeetingID = db.Column(db.String(255), primary_key=True)
    OfferingID = db.Column(db.String(255), db.ForeignKey('COURSEOFFERINGS.OfferingID'))
    Date = db.Column(db.Date)
    StartTime = db.Column(db.DateTime)
    EndTime = db.Column(db.DateTime)
    Location = db.Column(db.String(255))