# app/db/database.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

# MongoDB client
client = None

async def connect_to_mongo():
    """Connect to MongoDB."""
    global client
    if client is None:
        client = MongoClient(MONGODB_URI)
        # Test the connection
        client.admin.command('ping')
        print("Connected to MongoDB!")

async def close_mongo_connection():
    """Close MongoDB connection."""
    global client
    if client is not None:
        client.close()
        print("MongoDB connection closed.")

def get_db():
    """Get MongoDB database."""
    if client is None:
        raise Exception("MongoDB client not initialized")
    return client["weather"]