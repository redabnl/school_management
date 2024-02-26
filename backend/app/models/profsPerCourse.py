from app.extensions import db

# Association table for the Many-to-Many relationship between professors and courses
professor_courses = db.Table('PROFESSORSPERCOURSE',
    db.Column('ID_PROFESSOR', db.String(100), db.ForeignKey('USERS.ID_USER'), primary_key=True),
    db.Column('ID_COURSE', db.String(100), db.ForeignKey('COURSES.ID_COURSE'), primary_key=True)
)
