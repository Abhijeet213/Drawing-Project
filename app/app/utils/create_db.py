# create_db.py
from sqlalchemy import create_engine
from setting import DATABASE_HOST, DATABASE_PORT


from app.model.drawing import Base

# Replace the following URL with your PostgreSQL connection URL
DATABASE_URL = f'{DATABASE_HOST}:{DATABASE_PORT}'
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(engine)
