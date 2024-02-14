# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import Base, engine
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

Base.metadata.create_all(bind=engine)  # Create tables if they don't exist
