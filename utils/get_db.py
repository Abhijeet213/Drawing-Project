from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from setting import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME

# DATABASE_URL = f'postgresql://postgres:@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
DATABASE_URL = f'postgresql://postgres@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}?password='

engine = create_engine(DATABASE_URL)

def get_db():
    db = Session(engine)
    try:
        return db
    finally:
        db.close()
