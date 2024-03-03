from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

# ACADEMICCYCLES Model
class AcademicCycles(db.Model):
    __tablename__ = 'ACADEMICCYCLES'
    CycleID = db.Column(db.String(255), primary_key=True)
    Name = db.Column(db.String(255))
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)