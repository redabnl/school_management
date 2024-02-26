from app.extensions import db 
from sqlalchemy import Column, Integer, String, Number


class Course(db.Model):
    __tablename__ = 'COURSES'
    
    ID_COURSE = db.Column(db.String(100), primary_key=True)
    NAME = db.Column(db.String(100), nullable=False)
    DESCRIPTION = db.Column(db.Text)
    PREREQUISITE = db.Column(db.String(100), db.ForeignKey('COURSES.ID_COURSE'))

    # Relationships
    sessions = db.relationship('Session', back_populates='course')
    professors = db.relationship('User', secondary='PROFESSORSPERCOURSE', back_populates='courses_taught')

    