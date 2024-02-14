from database import Base
from sqlalchemy import Column, Integer, String, Number

class Professors(Base):
    __tablename__ = 'courses'

    id_course = Column(Integer, primary_key=True)
    course_title = Column(String)
    course_desc = Column(String)
    nb_hours = Column(Number)
    course_category = Column(String)
    