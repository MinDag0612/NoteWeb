import os
import re
import uuid
from datetime import datetime
from pathlib import Path
import base64

import bcrypt
import cloudinary
import cloudinary.uploader
from bson import ObjectId
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, File, HTTPException, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from google.auth.transport import requests
from google.oauth2 import id_token

import backendSrc.jwt_auth as jwt
import backendSrc.schema.schema_req as schema_req
from backendSrc.data.conn import Conn
from backendSrc.schema.NoteSche import Note
from backendSrc.schema.UserSche import User

load_dotenv()

API_ROOT_PATH = os.getenv("API_ROOT_PATH", "/api")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
BACKEND_CORS_ORIGINS_RAW = os.getenv(
    "BACKEND_CORS_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000",
)

UPLOAD_STORAGE_MODE = os.getenv("UPLOAD_STORAGE_MODE", "hybrid").strip().lower()
UPLOAD_LOCAL_DIR = Path(os.getenv("UPLOAD_LOCAL_DIR", "uploads")).expanduser().resolve()
PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL", "").strip().rstrip("/")
UPLOAD_CLOUDINARY_FOLDER = os.getenv("UPLOAD_CLOUDINARY_FOLDER", "NoteWeb")

CLOUDY_NAME = os.getenv("CLOUDY_NAME") or os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDY_API_KEY = os.getenv("CLOUDY_API_KEY") or os.getenv("CLOUDINARY_API_KEY")
CLOUDY_SECRET = os.getenv("CLOUDY_SECRET") or os.getenv("CLOUDINARY_API_SECRET")
CLOUDINARY_READY = bool(CLOUDY_NAME and CLOUDY_API_KEY and CLOUDY_SECRET)

VALID_UPLOAD_MODES = {"local", "cloudinary", "hybrid"}
SAFE_EXTENSION_PATTERN = re.compile(r"^\.[a-z0-9]{1,10}$")


def parse_cors_origins(raw_value: str) -> list[str]:
    origins = [item.strip() for item in raw_value.split(",") if item.strip()]
    return origins if origins else ["http://localhost:3000", "http://127.0.0.1:3000"]


def safe_extension(filename: str | None) -> str:
    suffix = Path(filename or "").suffix.lower()
    if SAFE_EXTENSION_PATTERN.match(suffix):
        return suffix
    return ".bin"


def build_upload_url(request: Request, filename: str) -> str:
    if PUBLIC_BASE_URL:
        return f"{PUBLIC_BASE_URL}/uploads/{filename}"
    return f"{str(request.base_url).rstrip('/')}/uploads/{filename}"


def persist_local_upload(request: Request, content: bytes, original_name: str | None) -> str:
    extension = safe_extension(original_name)
    file_name = f"{uuid.uuid4().hex}{extension}"
    destination = UPLOAD_LOCAL_DIR / file_name
    destination.write_bytes(content)
    return build_upload_url(request, file_name)


def upload_to_cloudinary(content: bytes, content_type: str | None) -> str:
    if not CLOUDINARY_READY:
        raise HTTPException(
            status_code=500,
            detail="Cloudinary is not configured. Set CLOUDY_NAME, CLOUDY_API_KEY, and CLOUDY_SECRET.",
        )

    mime_type = content_type or "application/octet-stream"
    encoded_content = base64.b64encode(content).decode("ascii")
    data_uri = f"data:{mime_type};base64,{encoded_content}"

    result = cloudinary.uploader.upload(data_uri, folder=UPLOAD_CLOUDINARY_FOLDER)
    return result["secure_url"]


if UPLOAD_STORAGE_MODE not in VALID_UPLOAD_MODES:
    raise RuntimeError(
        "UPLOAD_STORAGE_MODE must be one of: local, cloudinary, hybrid. "
        f"Received: {UPLOAD_STORAGE_MODE}"
    )

UPLOAD_LOCAL_DIR.mkdir(parents=True, exist_ok=True)
if CLOUDINARY_READY:
    cloudinary.config(
        cloud_name=CLOUDY_NAME,
        api_key=CLOUDY_API_KEY,
        api_secret=CLOUDY_SECRET,
    )

cors_origins = parse_cors_origins(BACKEND_CORS_ORIGINS_RAW)
allow_credentials = "*" not in cors_origins

app = FastAPI(root_path=API_ROOT_PATH)
connDB = Conn()
app.mount("/uploads", StaticFiles(directory=str(UPLOAD_LOCAL_DIR)), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=allow_credentials,
    allow_methods=["*"],
    allow_headers=["*"],
)


def verify_google_token(credential: str):
    if not GOOGLE_CLIENT_ID:
        return None

    try:
        idinfo = id_token.verify_oauth2_token(
            credential,
            requests.Request(),
            GOOGLE_CLIENT_ID,
        )

        return {
            "google_id": idinfo["sub"],
            "email": idinfo["email"],
            "name": idinfo.get("name"),
            "picture": idinfo.get("picture"),
            "email_verified": idinfo.get("email_verified"),
        }
    except ValueError:
        return None


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/upload-image")
async def upload_image(request: Request, file: UploadFile = File(...)):
    content = await file.read()
    await file.close()

    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    if UPLOAD_STORAGE_MODE == "local":
        return {"url": persist_local_upload(request, content, file.filename)}

    if UPLOAD_STORAGE_MODE == "cloudinary":
        return {"url": upload_to_cloudinary(content, file.content_type)}

    try:
        return {"url": persist_local_upload(request, content, file.filename)}
    except OSError:
        return {"url": upload_to_cloudinary(content, file.content_type)}


@app.post("/login")
def login(loginReq: schema_req.LoginRequest):
    user = connDB.users.find_one({"email": loginReq.email})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["_id"] = str(user["_id"])

    if user["provider"] != "local":
        raise HTTPException(status_code=400, detail=f"Please login with {user['provider']} provider")

    if not bcrypt.checkpw(loginReq.password.encode("utf-8"), user["password"].encode("utf-8")):
        raise HTTPException(status_code=401, detail="Invalid password")

    userOb = User(
        full_name=user["full_name"],
        email=user["email"],
        provider=user["provider"],
        provider_id=user["provider_id"],
    )

    token = jwt.create_access_token(
        payload={
            "sub": user["_id"],
            "full_name": userOb.full_name,
            "email": userOb.email,
        }
    )

    return {"status": "success", "user": userOb.__todict__(), "access_token": token}


@app.post("/login-google")
def login_google(loginReq: schema_req.LoginGoogleRequest):
    if not GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="Google login is not configured on the server")

    google_user = verify_google_token(loginReq.credential)
    if not google_user:
        raise HTTPException(status_code=401, detail="Invalid Google token")

    user = connDB.users.find_one({"email": google_user["email"]})
    if not user:
        raise HTTPException(status_code=404, detail="User not found, please register first")

    user["_id"] = str(user["_id"])

    if user["provider"] != "google":
        raise HTTPException(status_code=400, detail=f"Please login with {user['provider']} provider")

    userOb = User(
        full_name=user["full_name"],
        email=user["email"],
        provider=user["provider"],
        provider_id=user["provider_id"],
    )

    token = jwt.create_access_token(
        payload={
            "sub": str(user["_id"]),
            "full_name": userOb.full_name,
            "email": userOb.email,
        }
    )

    return {"status": "success", "user": userOb.__todict__(), "access_token": token}


@app.post("/create-note")
def create_note(user: dict = Depends(jwt.get_current_user)):
    new_note = Note.default_note(user["sub"], datetime.now().strftime("%d/%m/%Y"))
    result = connDB.notes.insert_one(new_note.__todict__())

    note = connDB.notes.find_one({"_id": result.inserted_id})

    return {
        "status": "success",
        "note": {
            "noteId": str(note["_id"]),
            "title": note["title"],
            "content": note["content"],
            "img": note["img"],
        },
    }


@app.get("/get-notes")
def get_notes(user: dict = Depends(jwt.get_current_user)):
    user_id = user["sub"]
    notes_cursor = connDB.notes.find({"user_id": user_id})
    notes = []

    for note in notes_cursor:
        notes.append(
            {
                "noteId": str(note["_id"]),
                "title": note["title"],
                "content": note["content"],
                "img": note["img"],
                "created_at": note["created_at"],
            }
        )

    return {"status": "success", "notes": notes}


@app.post("/notes/update")
def update_note(noteReq: schema_req.UpdateNoteRequest, user: dict = Depends(jwt.get_current_user)):
    user_id = user["sub"]
    note = connDB.notes.find_one({"_id": ObjectId(noteReq.noteId)})

    if not note or note["user_id"] != user_id:
        raise HTTPException(status_code=404, detail="Note not found")

    update_result = connDB.notes.update_one(
        {"_id": ObjectId(noteReq.noteId)},
        {
            "$set": {
                "title": noteReq.newTitle,
                "content": noteReq.newContent,
                "img": noteReq.newImages,
            }
        },
    )

    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {
        "status": "success",
        "note": {
            "noteId": noteReq.noteId,
            "title": noteReq.newTitle,
            "content": noteReq.newContent,
            "img": noteReq.newImages,
        },
    }


@app.delete("/delete-note")
def delete_note(noteReq: schema_req.DeleteNoteRequest, user: dict = Depends(jwt.get_current_user)):
    user_id = user["sub"]
    note = connDB.notes.find_one({"_id": ObjectId(noteReq.noteId)})

    if not note or note["user_id"] != user_id:
        raise HTTPException(status_code=404, detail="Note not found")

    delete_result = connDB.notes.delete_one({"_id": ObjectId(noteReq.noteId)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")

    return {"status": "success", "message": "Note deleted successfully"}
