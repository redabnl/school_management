from app import db

class Enrollments(db.Model):
    __tablename__ = 'ENROLLMENTS'
    EnrollmentID = db.Column(db.String(255), primary_key=True)
    StudentID = db.Column(db.String(255), db.ForeignKey('USERS.UserID'))
    OfferingID = db.Column(db.String(255), db.ForeignKey('COURSEOFFERINGS.OfferingID'))
    EnrollmentDate = db.Column(db.Date)
    Status = db.Column(db.String(255))
