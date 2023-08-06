from pydantic import BaseModel,EmailStr
from datetime import datetime 
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True 

class PostCreate(PostBase):
    pass

"""
class PostUpdate(PostBase):
    published : bool 
"""
#when we create a post, we can pass a owner_id
#this is our response for create post

#this is our response for create user
class UserOut(BaseModel):
    email: EmailStr
    id : int
    created_at: datetime 

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: UserOut  # Add the correct type annotation here

    class Config:
        from_attributes = True



class UserCreate(BaseModel):
    email :EmailStr
    password : str

#login and auth
class UserLogin(BaseModel):
    email : EmailStr
    password : str
#access token and type of token
class Token(BaseModel):
    access_token : str
    token_type :str

#schema for token data
class TokenData(BaseModel):
    id : Optional[str]= None

#schema for voting
class Vote(BaseModel):
    post_id:int
    dir:conint(le=1) #we just want the value to be 0 or 1 

class PostOut(BaseModel):
    Post:Post
    votes:int

    class Config:
        from_attributes = True