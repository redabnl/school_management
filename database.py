from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')
schema = os.getenv('SNOWFLAKE_SCHEMA')

engine_url = f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
engine = create_engine(engine_url)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()