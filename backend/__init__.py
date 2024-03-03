from flask import Flask 
from flask_cors import CORS
from app.extensions import db, migrate
from config import DevelopmentConfig
from flask_migrate import migrate
from app.controllers.admin_controller import register_user as register_func

from app.models import *
import os

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.secret_key = os.environ.get('SECRET_KEY', 'fallback_secret_key')

db.init_app(app)
migrate.init_app(app, db)


@app.route('/')
def index():
    return "Welcome to the School Management App iRead"

@app.route('register_user', methods=['POST'])
def registerUser():
    return register_func()

# @app.route('/register_student', methods=['POST'])
# def register_student():
#     return register_user('student')

# @app.route('/register_professor', methods=['POST'])
# def register_professor():
#     return register_user('professor')


# @app.route('/student_login', methods=['POST'])
# def  student_login():
#     return login_student()

# @app.route('/professor_login', methods=['POST'])
# def professor_login():
#     return login_professor()

# @app.route('/search_student/', methods=['GET'])
# def student_search():
#     return search_student()



  
