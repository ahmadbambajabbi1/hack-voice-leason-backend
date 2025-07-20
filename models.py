from pymongo import MongoClient
from config import Config
import logging

try:
    client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection on a request as the
    db = client.get_default_database()
    videos = db.videos
except Exception as e:
    logging.error(f"MongoDB connection failed: {e}")
    client = None
    db = None
    videos = None 