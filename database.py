from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.engine.url import URL
import os

from dotenv import load_dotenv
load_dotenv() 

user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')
schema = os.getenv('SNOWFLAKE_SCHEMA')



if not all([user, password, account, warehouse, database, schema]):
    raise ValueError("Snowflake environment variables are not set properly.")


engine_url = URL.create(
    drivername="snowflake", 
    username=user,
    password=password,
    host=account,
    database=database,
    query={
        'warehouse': warehouse,
        'schema': schema
    }
)
engine = create_engine(engine_url)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

