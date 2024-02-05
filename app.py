from flask import Flask
# from .database import SessionLocal, Base, engine
from flask_sqlalchemy import SQLAlchemy
from config import DevelopementConfig

from dotenv import load_dotenv
load_dotenv() 

app = Flask(__name__)
app.config.from_object(DevelopementConfig)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "welcome to school management app iRead"

# @app.route('/')
# def hellop():
#     return "hello , python"

if __name__ == '__main__':
    app.run()