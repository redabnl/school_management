from flask import request, jsonify
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.students import Students
from app.models.professors import Professors

def register_user(user_type):
    if request.is_json:
        data = request.get_json()
    else:
        return jsonify({
            'success' : False,
            "message" : "invalid content type"
        }), 400
    
    #check if all the needed fields are in
    required_fields = ['first_name','last_name', 'email', 'password']
    if not all(field  in data for field in required_fields):
        return jsonify({
            'success' : False,
            "error": "missing field !"
        })
    #hasing the pwd
    hashed_pwd = generate_password_hash(data["password"])
    
    if user_type == 'student' :
        new_user = Students(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password_hash=hashed_pwd
        )
    elif user_type == 'professor':
        new_user = Professors(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password_hash=hashed_pwd
        )
    else:
        return jsonify({"error": "Invalid user type"}), 400
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            'success': True,
            "message": f"{user_type.capitalize()} registered successfully"
            
            }), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already registered"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
