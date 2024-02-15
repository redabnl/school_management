# from database import Base
# from sqlalchemy import Column, Integer, String
from app.extensions import db
from .users import Users

class Students(Users):
    __tablename__ = 'students'
    sessionA = db.Column(db.String)
    status = db.Column(db.String)