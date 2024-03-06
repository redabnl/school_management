from app import db
from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

class Users(db.Model):
    __tablename__ = 'USERS'
    USERID = db.Column(db.String(255), primary_key=True)
    FIRSTNAME = db.Column(db.String(255))
    LASTNAME = db.Column(db.String(255))
    EMAIL = db.Column(db.String(255))
    PASSWORD = db.Column(db.String(255))
    USERROLE = db.Column(db.String(255))
    ADDITIONALINFO = db.Column(db.Text)