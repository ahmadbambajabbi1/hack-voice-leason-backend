import cloudinary
import cloudinary.uploader
from config import Config

cloudinary.config(
    cloud_name=Config.CLOUD_NAME,
    api_key=Config.CLOUD_KEY,
    api_secret=Config.CLOUD_SECRET,
)

def upload_video(file_path):
    resp = cloudinary.uploader.upload_large(
        file_path,
        resource_type="video",
        chunk_size=6000000,
    )
    return resp['secure_url'] 