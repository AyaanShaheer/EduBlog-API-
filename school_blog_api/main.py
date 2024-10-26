from fastapi import FastAPI, HTTPException
from models import Post
from database import db, init_indexes
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from datetime import datetime

app = FastAPI()

# Run init_indexes at startup
@app.on_event("startup")
async def startup_db_client():
    await init_indexes()

@app.get("/")
async def root():
    return {"message": "Welcome to the School Blog API"}

@app.post("/posts/", response_model=Post)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict["created_at"] = datetime.utcnow()
    try:
        result = await db.posts.insert_one(post_dict)
        post_dict["_id"] = str(result.inserted_id)
        return post_dict
    except Exception as e:
        raise HTTPException(status_code=400, detail="Post with this title already exists.")

@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: str):
    post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if post:
        post["_id"] = str(post["_id"])
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: str, updated_post: Post):
    updated_post_dict = updated_post.dict(exclude_unset=True)
    result = await db.posts.update_one({"_id": ObjectId(post_id)}, {"$set": updated_post_dict})
    if result.modified_count == 1:
        updated_post = await db.posts.find_one({"_id": ObjectId(post_id)})
        updated_post["_id"] = str(updated_post["_id"])
        return updated_post
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    result = await db.posts.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 1:
        return {"message": "Post deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
