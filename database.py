from flask import app
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
import os

user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')
schema = os.getenv('SNOWFLAKE_SCHEMA')


if not all([user, password, account, warehouse, database, schema]):
    raise ValueError("Snowflake environment variables are not set properly.")

# engine_url = f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}"
engine_url = URL(
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

# MetaData object to hold schema and other options
metadata = MetaData(bind=engine)

# Call remove() after each request to cleanup the session
@app.teardown_appcontext
def remove_session(*args, **kwargs):
    SessionLocal.remove()

# Call dispose() when app stops to close the engine connection
@app.before_first_request
def setup(*args, **kwargs):
    # Assuming 'app' is your Flask application
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        engine.dispose()