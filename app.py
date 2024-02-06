from flask import Flask, request, jsonify
from database import SessionLocal, Base, engine
from flask_sqlalchemy import SQLAlchemy
from config import DevelopementConfig
from werkzeug.security import generate_password_hash, check_password_hash


from models.student import Student

from dotenv import load_dotenv
load_dotenv() 

app = Flask(__name__)
app.config.from_object(DevelopementConfig)
Base.metadata.create_all(bind=engine)  # Create tables if they don't exist


db = SQLAlchemy(app)

@app.route('/')
def index():
    return "welcome to school management app iRead"


@app.route('/register', methods=['POST'])
def register_student():
    db = SessionLocal()
    try:
        # Extract student data from request
        student_data = request.json
        new_student = Student(first_name=student_data['first_name'], last_name=student_data['last_name'] ,email=student_data['email'], password_hash=generate_password_hash(student_data['password']))
        
        # Add new student to the session and commit
        db.add(new_student)
        db.commit()
        
        return jsonify({"message": "Student registered successfully"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


# @app.route('/')
# def hellop():
#     return "hello , python"

if __name__ == '__main__':
    app.run()