from flask import request, jsonify, session
from werkzeug.security import check_password_hash
from app.extensions import db 
from app.models.students import Students    
from sqlalchemy import or_


    
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
    


def search_student():
    
    query = request.args.get('query')

    if not query:
        return jsonify({"success": False, "message": "Search query is required"}), 400

    # Use the `ilike` operator for case-insensitive search
    students = Students.query.filter(or_(
        Students.FIRST_NAME.ilike(f'%{query}%'),
        Students.LAST_NAME.ilike(f'%{query}%')
    )).all()

    if not students:
        return jsonify({"success": False, "message": "No students found"}), 404

    student_data_list = [{
        'student_id': student.ID_STUDENT,
        'student_name': f'{student.FIRST_NAME} {student.LAST_NAME}',
        'email': student.email,
        # Add other attributes specific to students
    } for student in students]

    return jsonify({"success": True, "data": student_data_list}), 200
