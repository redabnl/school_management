from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app.extensions import db 
from app.models.students import Students

def register_student():
    try:
        # Extract student data from request
        student_data = request.get_json()
        new_student = Students(
            first_name=student_data['first_name'], 
            last_name=student_data['last_name'],
            mail=student_data['email'], 
            password_hash=generate_password_hash(student_data['password'])
        )
        
        # Add new student to the session and commit
        db.session.add(new_student)
        db.session.commit()
        
        return jsonify({"message": "Student registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
    
