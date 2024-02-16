from app.extensions import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()

class Students(Base):
    __tablename__ = 'STUDENTS'  # uppercase tablename if it's defined as such in Snowflake

    ID_STUDENT = Column(String(100), primary_key=True)
    FIRST_NAME = Column(String(100))
    LAST_NAME = Column(String(100))
    MAIL = Column(String(100))
    PASSWORD = Column(String(255))
    STATUS = Column(String(100))
    SESSIONA = Column(String(100))

