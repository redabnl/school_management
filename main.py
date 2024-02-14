# main.py
from app import app
from .app.controllers.student_controller import register_student

@app.route('/')
def index():
    return "Welcome to the School Management App iRead"

@app.route('/register', methods=['POST'])
def register():
    return register_student()

if __name__ == '__main__':
    app.run()
