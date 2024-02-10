from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import SessionLocal, Base, engine
from models.students import Students
from sqlalchemy.orm import scoped_session
from config import DevelopementConfig
from werkzeug.security import generate_password_hash, check_password_hash


from dotenv import load_dotenv
load_dotenv() 

app = Flask(__name__)
app.config.from_object(DevelopementConfig)
Base.metadata.create_all(bind=engine)  # Create tables if they don't exist


db = SQLAlchemy(app)
db_session = scoped_session(SessionLocal)

@app.route('/')
def index():
    return "welcome to school management app iRead"


@app.route('/register', methods=['POST'])
def register_student():
    session = db_session()
    try:
        # Extract student data from request
        student_data = request.get_json
        new_student = Students(
            first_name=student_data['first_name'], 
            last_name=student_data['last_name'] ,
            mail=student_data['email'], 
            password_hash=generate_password_hash(student_data['password']))
        
        # Add new student to the session and commit
        session.add(new_student)
        session.commit()
        
        return jsonify({"message": "Student registered successfully"}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()


# @app.route('/')
# def hellop():
#     return "hello , python"

if __name__ == '__main__':
    app.run()