
from sqlalchemy import create_engine, Column, Integer, String, Sequence,LargeBinary,INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True,autoincrement=True)
    name = Column(String(100))
    email= Column(String(100),unique=True)
    password=Column(String(100))