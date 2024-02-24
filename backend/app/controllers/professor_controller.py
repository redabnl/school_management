from flask import request, jsonify, session
from werkzeug.security import check_password_hash
from app.extensions import db 
from app.models.professors import Professors

    
def login_professor():
    data = request.get_json()
    professor = Professors.query.filter_by(MAIL=data['mail']).first()
    pwd = data.get("password")
    
    if professor and check_password_hash(professor.PASSWORD, pwd):
        #if the professors is found 
        session['professor_id'] = professor.ID_PROFESSOR
        return jsonify({
            'success' : True,
            "message" : "logged in successfully"
        }),200
    else:
        # If the user does not exist or password is wrong
        return jsonify({"success": False, "message": "Invalid credentials"}), 401