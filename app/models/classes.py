from database import Base
from sqlalchemy import Column, Integer, String, Date

class Professors(Base):
    __tablename__ = 'classes'

    class_NO = Column(Integer, primary_key=True)
    class_title = Column(String)
    class_date = Column(Date)
    
    