import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUD_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUD_SECRET = os.getenv("CLOUDINARY_API_SECRET")
    LLM_PATH = os.getenv("LLM_MODEL_PATH") 