from database import Base
from sqlalchemy import Column, Integer, String

class Students(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    sessionA = Column(String)
    status = Column(String)