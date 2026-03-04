import os
from datetime import datetime

import bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient

from backendSrc.schema.NoteSche import Note
from backendSrc.schema.UserSche import UserQuery

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DEFAULT_SEED_USER_ID = os.getenv("SEED_NOTE_USER_ID", "696fbdd0be46967353045384")

if not MONGODB_URI:
    raise RuntimeError(
        "MONGODB_URI is required to run backendSrc.data.query. "
        "Copy .env.example to .env and set a real MongoDB connection string."
    )

client = MongoClient(MONGODB_URI)
db = client["WebNote"]
users = db["User"]


def create_user(email: str, password: str, provider, full_name: str = "", provider_id: str = ""):
    hashed_pw = None if not password else bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    pro_id = None if provider == "local" else provider_id

    new_user = UserQuery(
        full_name=full_name,
        password=hashed_pw,
        email=email,
        provider=provider,
        provider_id=pro_id,
    )

    users.insert_one(new_user.__todict__())
    print("User created")


def create_note(user_id: str):
    notes = db["Note"]
    new_note = Note.default_note(user_id, datetime.now().strftime("%d/%m/%Y"))

    notes.insert_one(new_note.__todict__())
    print("Note created")


if __name__ == "__main__":
    for _ in range(0, 5):
        create_note(DEFAULT_SEED_USER_ID)
