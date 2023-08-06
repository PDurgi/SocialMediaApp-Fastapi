
from typing import List,Optional
from fastapi import FastAPI,Response,status,HTTPException,Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import oauth2
from ..import models,schemas,oauth2
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)
#raw sql
# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts= cursor.fetchall()
#     print(posts)
#     return {"data":posts}

@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user),limit : int=10, 
    skip : int=0, search : Optional[str]=""):
    print(limit)
    #posts= db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    posts =db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #print(results)
    return posts

'''
@router.post("/createposts")
def create_posts(payload: dict = Body(...)):# extracts all the feilds from Body and load it into a dictionary a
    #assign it to a variable named payload.
    print(payload)
    return {"new_post":f"title {payload['title']} content: {payload['content']}"}

'''
#without DB
# @router.post("/posts",status_code=status.HTTP_201_CREATED)
# def createposts(new_post : Post): #
#     post_dict =new_post.dict()
#     post_dict['id']= randrange(0,100000)
#     my_posts.append(post_dict)
#     return { "data":post_dict}

#with DB
# @router.post("/posts",status_code=status.HTTP_201_CREATED)
# def createposts(new_post : Post): 
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING * """,
#     (new_post.title,new_post.content,new_post.published))
#     posted = cursor.fetchone()
#     #everytime we make changes to DB, we need to commit
#     conn.commit()
#     return {"data":posted}

#create post with ORM

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def createposts(post : schemas.PostCreate,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)): 
    #print(current_user.id)
    #print(current_user.email)
    new_post=models.Post(owner_id=current_user.id, **post.dict())
    #we created an entry but we need to commit just like raw sql
    db.add(new_post)
    db.commit()
    #we dont have RETURNING IN SQLALCHEMY
    db.refresh(new_post)
    return new_post

#Without DB
# #path parameter id has been passed
# #based on the id, we can extract the post
# @app.get("/posts/{id}")
# def get_post(id : int, response : Response):
#     post = find_post(id)
    
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail=f"post with id : {id} was not found")
# #        response.status_cosde=status.HTTP_404_NOT_FOUND 
# #       return {'message' : "post with id : {id} was not found"}
#     return {"post details" : post}

#withDB
#raw sql
# @app.get("/posts/{id}")
# def get_post(id : int, response : Response):
#     cursor.execute("""select * from posts where id=%s""",(str(id),))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail=f"post with id : {id} was not found")
#     return {"post details" : post}

#ORM SQLalchemy
@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id : int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    #post=db.query(models.Post).filter(models.Post.id==id).first()
    post =db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"post with id : {id} was not found")
    return post

#without DB
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id : int):
#     #deleting a post logic
#     #find the index in array that has the required ID
#     #my_posts.pop(index)
#     index = find_index_post(id)
#     if index== None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} does not exist")
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT )

#with DB
#raw SQL
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id : int):
#     cursor.execute("""DELETE FROM posts where id= %s RETURNING *""",(str(id),))
#     index = cursor.fetchone()
#     #everytime we make changes to DB, we need to commit
#     conn.commit()
#     if index== None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} does not exist")
#     return Response(status_code=status.HTTP_204_NO_CONTENT )

#SQLALCHEMY ORM 
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)

    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail ="Not authorized to perform requested action ")
    
    post_query.delete(synchronize_session =False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT )

#without DB  
# @app.put("/posts/{id}")
# def update_post(id: int,post:Post):
#     print(post)
#     #find the index od post with specific id that we need to update
#     index = find_index_post(id)
#     if index== None:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"post with id :{id} does not exist")
#     #front end will send the data that needs to be updated
#     #we will convert it to a dictionary and do necessary updation
#     post_dict =post.dict()
#     post_dict['id']=id
#     my_posts[index] = post_dict
#     return {"data" : post_dict}

#withDB
#raw sql
# @app.put("/posts/{id}")
# def update_post(id: int,post:Post):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s ,published = %s WHERE id=%s
#      RETURNING *""",
#     (post.title, post.content, post.published, str(id)))
#     #find the index od post with specific id that we need to update
#     index = cursor.fetchone()
#     conn.commit()
#     if index== None:
#         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"post with id :{id} does not exist")
#     #front end will send the data that needs to be updated
#     #we will convert it to a dictionary and do necessary updation

#     return {"data" : index}


#sqlalchemy #orm
@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int,updated_post:schemas.PostCreate,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{id} does not exist")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail ="Not authorized to perform requested action ")   
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()