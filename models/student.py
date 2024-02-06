from database import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    sessionA = Column(String)
    status = Column(String)