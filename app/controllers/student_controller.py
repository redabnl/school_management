from flask import request, jsonify, session
from werkzeug.security import check_password_hash
from app.extensions import db 
from app.models.students import Students


    
def login_student():
    data = request.get_json()
    student = Students.query.filter_by(MAIL=data['mail']).first()
    pwd = data.get("password")
    
    if student and check_password_hash(student.PASSWORD, pwd):
        #if the student is found 
        session['student_id'] = student.ID_STUDENT
        return jsonify({
            'success' : True,
            "message" : "logged in successfully"
        }),200
    else:
        # If the user does not exist or password is wrong
        return jsonify({"success": False, "message": "Invalid credentials"}), 401