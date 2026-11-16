import os

import cloudinary
import cloudinary.uploader
from fastapi import APIRouter, File, UploadFile

router = APIRouter()

cloudinary.config(
    cloud_name=os.getenv("CLOUDY_NAME"),
    api_key=os.getenv("CLOUDY_API_KEY"),
    api_secret=os.getenv("CLOUDY_SECRET"),
)


@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    result = cloudinary.uploader.upload(file.file, folder="NoteWeb")
    return {"url": result["secure_url"]}
