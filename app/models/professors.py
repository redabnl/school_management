from app.extensions import db
from .users import Users

class Professors(Users):
    __tablename__ = 'professors'
    departement = db.Column(db.String)
    