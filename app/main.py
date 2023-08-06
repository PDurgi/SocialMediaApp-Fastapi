
from fastapi import FastAPI
from . import models
from .database import engine
from .router import post,user,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#from pydantic import BaseSettings

#models.Base.metadata.create_all(bind=engine)
# create Dependency
#session object is responsible to talk to db
# everytime we get a request we get a session to which we send sql statements

app = FastAPI() #create and instance of fastapi
  
#list of domains that can talk to our api

origins=["*"]
#    allow_methods=["*"] = we can also allow only specific methods from domains like just get requests etc
"""
let us create a list that will store all our posts 
since we donot have a database
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#path/route operation
#decorator
@app.get("/") 
async def root(): #name can be anything #root is convention
#async is optional. We can use this keyword whenever we are doing asyncronous tasks
    return {"message": "Welcome to Pooja Durgi's API !!!!!!!"} #returning a dictionary
#this function can have any logic


