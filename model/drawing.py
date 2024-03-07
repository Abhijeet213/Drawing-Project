
from sqlalchemy import create_engine, Column, Integer, String, Sequence,LargeBinary,INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Drawing(Base):
    __tablename__ = 'drawing'
    id = Column(Integer, Sequence('drawing_id_seq'), primary_key=True,autoincrement=True)
    image = Column(LargeBinary)
    name = Column(String(100), unique=True)
    price= Column(INTEGER)
    discount=Column(INTEGER)
    quantity=Column(INTEGER)