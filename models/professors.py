from database import Base
from sqlalchemy import Column, Integer, String

class Professors(Base):
    __tablename__ = 'professors'

    professor_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    phoneNo = Column(String)