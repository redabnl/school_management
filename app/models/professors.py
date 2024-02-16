from app.extensions import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

class Professors(db.Model):
    __tablename__ = 'PROFESSORS'
    
    ID_PROFESSOR = Column(String(100), primary_key=True)
    FIRST_NAME = Column(String(100))
    LAST_NAME = Column(String(100))
    MAIL = Column(String(100))
    PASSWORD = Column(String(255))
    DEPARTEMENT = Column(String(100))
    