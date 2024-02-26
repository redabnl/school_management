from app.extensions import db

class Session(db.Model):
    __tablename__ = 'SESSIONS'
    
    ID_SESSION = db.Column(db.String(100), primary_key=True)
    ID_COURSE = db.Column(db.String(100), db.ForeignKey('COURSES.ID_COURSE'), nullable=False)
    START_DATE = db.Column(db.Date, nullable=False)
    END_DATE = db.Column(db.Date, nullable=False)

    # Relationships
    course = db.relationship('Course', back_populates='sessions')
    enrollments = db.relationship('Enrollement', back_populates='session')
