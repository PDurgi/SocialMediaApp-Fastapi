#every model represents a table in our DB
#with ORM we will not need sql
#in models.py we have tables in our db and we define them using classes 

from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,ForeignKey
from sqlalchemy.sql.expression import null,text
from .database import Base
from sqlalchemy.orm import relationship
#from sqlalchemy import *
 #to create columns

#our class extends Base
class Post(Base):
    __tablename__="posts" #name the table
    #define columns
    id= Column(Integer,primary_key=True,nullable=False) # Id cannot be null
    title = Column(String, nullable=False)
    content=Column(String,nullable=False)
    #postgres server is going to set the value as True, therefore we use server_default
    published = Column(Boolean,server_default='TRUE',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    #foreignkey ownerid will reference the id in User table. We will use the tablename.column and
    #specify other constraints like cascade on delete and cannot be null etc properties

    #set up a relationship
    owner = relationship("User") #referencing a table
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)  # Id cannot be null
    email = Column(String, nullable=False, unique=True)  # One email one user
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_number = Column(String)

#votes table

class Vote(Base):
    __tablename__="votes"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)


