from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URI = "mongodb://localhost:27017"  # or use os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_URI)
db = client.school_blog

async def init_indexes():
    # Create a unique index on the 'title' field of the 'posts' collection
    await db.posts.create_index([("title", ASCENDING)], unique=True)
