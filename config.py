import os 

class Config(object):
    SECRERT_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
class DevelopementConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False