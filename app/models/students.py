from database import Base
from sqlalchemy import Column, Integer, String

class Students(Base):
    __tablename__ = 'students'

    id_student = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    mail = Column(String, unique=True)
    password_hash = Column(String)
    sessionA = Column(String)
    status = Column(String)