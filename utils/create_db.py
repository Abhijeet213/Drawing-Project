# create_db.py
from sqlalchemy import create_engine
import sys

sys.path.append('C:\\Users\\Code It\\Documents\\Drawing Website')


from model.drawing import Base as drbase
from model.user import Base  as usbase


from setting import DATABASE_HOST, DATABASE_PORT, DATABASE_NAME

# DATABASE_URL = f'postgresql://postgres:@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
DATABASE_URL = f'postgresql://postgres@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}?password='


engine = create_engine(DATABASE_URL)

try:
    drbase.metadata.create_all(bind=engine)
    usbase.metadata.create_all(bind=engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")
