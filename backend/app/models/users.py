from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Users(db.Model):
    __tablename__ = 'USERS'
    UserID = db.Column(db.String(255), primary_key=True)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Password = db.Column(db.String(255))
    UserRole = db.Column(db.String(255))
    AdditionalInfo = db.Column(db.Text)