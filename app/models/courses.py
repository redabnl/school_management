from app.extensions import db 
from sqlalchemy import Column, Integer, String, Number

class Professors(db.Model):
    __tablename__ = 'courses'

    id_course = Column(Integer, primary_key=True)
    course_title = Column(String)
    course_desc = Column(String)
    nb_hours = Column(Number)
    course_category = Column(String)
    