# create_db.py
from sqlalchemy import create_engine
from model.drawing import Base
from setting import DATABASE_HOST,DATABASE_PORT


# Replace the following URL with your PostgreSQL connection URL
DATABASE_URL = f'{DATABASE_HOST}:{DATABASE_PORT}'
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)
