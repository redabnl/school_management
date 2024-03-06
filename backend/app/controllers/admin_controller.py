from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from app.extensions import db
from app.models import Users
from flask_login import login_user

# generate a custom id for every new user
def generate_custom_id(first_name, last_name):
    # Extract first 2 letters from first and last name for a custom id
    first_two_letters = (first_name[:2] + last_name[:2]).upper()

    # Get the current count of users with the specific user_role and increment it by 1
    user_count = Users.query.count() + 1
    user_count_str = str(user_count).zfill(4)  # Ensure it's a four-digit number, zero-padded

    # Combine the first two letters and the incremented number
    custom_id = first_two_letters + user_count_str
    return custom_id

# register a new user to the database
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
    custom_id = generate_custom_id(data['first_name'], data['last_name'])

    # Hash the password
    hashed_password = generate_password_hash(data['password'])

    # Create a new user instance
    new_user = Users(
        # UserID=custom_id,
        USERID = custom_id,
        FIRSTNAME=data['first_name'],
        LASTNAME=data['last_name'],
        EMAIL=data['email'],
        PASSWORD=hashed_password,
        USERROLE=data['user_role']
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
   
#login function for the admin    
def admin_login() :
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Invalid content type'}), 400

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Query the database for the user
    user = Users.query.filter_by(EMAIL=email)

    # Check if user exists, the password is correct, and the role is 'admin'
    if user and check_password_hash(user.PASSWORD, password) and user.UserRole.lower() == 'admin':
        login_user(user)  # This will set the current_user for the session
        return jsonify({'success': True, 'message': 'Admin logged in successfully'}), 200
    elif user and not user.UserRole.lower() == 'admin':
        return jsonify({'success': False, 'message': 'Access restricted to admin users'}), 403
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
 
#update user's info   
def edit_user(user_id):
    if not request.is_json:
        return jsonify({'success': False, 'message': 'Invalid content type'}), 400

    data = request.get_json()
    # Fetch the user from the database using the user_id
    user = Users.query.filter_by(UserID=user_id).first()

    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404

    # Update user details with the data received from the request
    user.FirstName = data.get('first_name', user.FirstName)
    user.LastName = data.get('last_name', user.LastName)
    user.Email = data.get('email', user.Email)
    user.UserRole = data.get('user_role', user.UserRole)
    user.AdditionalInfo = data.get('additionanal_info', user.AdditionalInfo)
    

    # Commit the changes to the database
    try:
        db.session.commit()
        return jsonify({'success': True, 'message': 'User updated successfully'}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'This email is already in use'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500