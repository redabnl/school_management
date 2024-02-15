
from flask import Flask 
from config import DevelopmentConfig
from .extensions import db
from app.controllers.admin_controller import register_user
from app.models import *
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.config.from_object('app.config.DevelopmentConfig')

db.init_app(app)



@app.route('/')
def index():
    return "Welcome to the School Management App iRead"

@app.route('/register_student', methods='POST')
def register_student():
    return register_user('student')

@app.route('/register_professor', methods='POST')
def register_professor():
    return register_user('professor')



  
