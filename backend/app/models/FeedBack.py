from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Feedback(db.Model):
    __tablename__ = 'FEEDBACK'
    FeedbackID = db.Column(db.String(255), primary_key=True)
    OfferingID = db.Column(db.String(255), db.ForeignKey('COURSEOFFERINGS.OfferingID'))
    Content = db.Column(db.Text)
    Timestamp = db.Column(db.DateTime)
    Anonymous = db.Column(db.Boolean)