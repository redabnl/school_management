from app.extensions import db

class Enrollement(db.Model):
    __tablename__ = 'ENROLLEMENTS'
    
    ID_ENROLLEMENT = db.Column(db.String(100), primary_key=True)
    ID_STUDENT = db.Column(db.String(100), db.ForeignKey('USERS.ID_USER'), nullable=False)
    ID_SESSION = db.Column(db.String(100), db.ForeignKey('SESSIONS.ID_SESSION'), nullable=False)
    ENROLLEMENT_DATE = db.Column(db.Date)
    STATUS = db.Column(db.String(100))

    # Relationships
    student = db.relationship('User', back_populates='enrollements')
    session = db.relationship('Session', back_populates='enrollements')
