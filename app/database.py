from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

#SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<databasename>"
#SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:Pooja8374@localhost:5432/FastapiDB'
SQLALCHEMY_DATABASE_URL= f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
#create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)
#create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#setup DB connection
# while(True):
#     try:

#         conn = psycopg2.connect(host='localhost', database='FastapiDB', user='postgres', password='Pooja8374', cursor_factory=RealDictCursor)

#         #psycopg2 lib only displays values without column names when we query it
#         #to get the col names we are passing the parameter cursor_factory
#         cursor=conn.cursor()
#         #cursor helps us execute sql statments
#         print("Database connection successful")
#         break
#     except Exception as error:
#         print("connecting to DB failed")
#         print("Error:",error)
#         time.sleep(2)
