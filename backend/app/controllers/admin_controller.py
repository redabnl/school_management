from flask import request, jsonify
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models import Users


def generate_custom_id(first_name, last_name, user_role):
    # Extract first 2 letters from first and last name for a custom id
    first_two_letters = (first_name[:2] + last_name[:2]).upper()

    # Get the current count of users with the specific user_role and increment it by 1
    user_count = Users.query.filter_by(UserRole=user_role).count() + 1
    user_count_str = str(user_count).zfill(4)  # Ensure it's a four-digit number, zero-padded

    # Combine the first two letters and the incremented number
    custom_id = first_two_letters + user_count_str
    return custom_id


def register_user():
    
    # # Only admin can register new users // we'll use this later
    # if not current_user.is_admin:
    #     return jsonify({'success': False, 'message': 'Unauthorized'}), 403
    
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Invalid content type'}), 400
    
    data = request.get_json()

    #check all no field is empty 
    required_fields = ['first_name', 'last_name', 'email', 'password', 'user_role']
    if not all(field in data for field in required_fields):
        return jsonify({'success': False, 'message': 'Missing field!'}), 400

  #generate a new customised id of the new registered new 
    custom_id = generate_custom_id(data['first_name'], data['last_name'], data['user_role'])

    # Hash the password
    hashed_password = generate_password_hash(data['password'])

    # Create a new user instance
    new_user = Users(
        UserID=custom_id,
        FirstName=data['first_name'],
        LastName=data['last_name'],
        Email=data['email'],
        Password=hashed_password,
        UserRole=data['user_role'],
       
    )

    # Attempt to add the new user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True, 'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Email already registered'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500