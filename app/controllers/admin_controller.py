from flask import request, jsonify
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models.students import Students
from app.models.professors import Professors


def generate_custom_id(first_name, last_name):
    # extract first 2 letters for a custom id
    first_two_letters = (first_name[:2] + last_name[:2]).upper()

    # Get the current count of users and increment it by 1
    user_count = Students.query.count() + Professors.query.count() + 1
    user_count_str = str(user_count).zfill(4)  # Ensure it's a four-digit number, zero-padded

    # Combine the first two letters and the incremented number
    custom_id = first_two_letters + user_count_str

    return custom_id
def register_user(user_type):
    if request.is_json:
        data = request.get_json()
    else:
        return jsonify({
            'success' : False,
            "message" : "invalid content type"
        }), 400
    
    #check if all the needed fields are i
    required_fields = ['first_name','last_name', 'mail', 'password']
    if not all(field  in data for field in required_fields):
        return jsonify({
            'success' : False,
            "error": "missing field !"
        })
    #hasing the pwd
    hashed_pwd = generate_password_hash(data["password"])
    custom_id = generate_custom_id(data['first_name'], data['last_name'])
    
    if user_type == 'student' :
        new_user = Students(
        ID_STUDENT = custom_id,
        FIRST_NAME=data['first_name'],
        LAST_NAME=data['last_name'],
        MAIL=data['mail'],
        PASSWORD=hashed_pwd,  
        STATUS='active',  
        SESSIONA=None
        )
    elif user_type == 'professor':
        new_user = Professors(
            ID_PROFESSOR = custom_id,
            FIRST_NAME=data['first_name'],
            LAST_NAME=data['last_name'],
            MAIL=data['mail'],
            PASSWORD=hashed_pwd, 
            DEPARTEMENT = ['departement']
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
