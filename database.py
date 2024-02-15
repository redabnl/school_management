from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.engine.url import URL
import os
import snowflake.connector
# import logging

# logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
load_dotenv() 

user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')
schema = os.getenv('SNOWFLAKE_SCHEMA')
role = os.getenv('SNOWFLAKE_ROLE')



if not all([user, password, account, warehouse, database, schema]):
    raise ValueError("Snowflake environment variables are not set properly.")

# Construct the connection string
CONNECTION_STRING = f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}&role={role}"

# Create the engine
engine = create_engine(CONNECTION_STRING)

try:
    with  engine.connect() :
        print("connection succeded for user :", user, " on database : ", database)
except Exception as E :
    print("error connecting to db:", database , "error : ", E)


SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

