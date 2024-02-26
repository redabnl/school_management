from app.extensions import db

class Class(db.Model):
    __tablename__ = 'CLASSES'

    ID_CLASS = db.Column(db.String, primary_key=True)
    CLASS_TITLE = db.Column(db.String)
    CLASS_DATE = db.Column(db.Date)
    
    