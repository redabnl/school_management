from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Homeworks(db.Model):
    __tablename__ = 'HOMEWORKS'
    HomeworkID = db.Column(db.String(255), primary_key=True)
    OfferingID = db.Column(db.String(255), db.ForeignKey('COURSEOFFERINGS.OfferingID'))
    Title = db.Column(db.String(255))
    Description = db.Column(db.Text)
    AcceptLate = db.Column(db.Boolean)
    DueDate = db.Column(db.DateTime)
