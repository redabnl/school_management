from flask import Flask
from .database import SessionLocal, Base, engine

from dotenv import load_dotenv
load_dotenv() 

app = Flask(__name__)

# @app.route('/')
# def hellop():
#     return "hello , python"

if __name__ == '__main__':
    app.run(debug=True)