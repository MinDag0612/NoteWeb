import os

import bcrypt
from fastapi import APIRouter, HTTPException
from google.auth.transport import requests
from google.oauth2 import id_token

from backend.app.core.database import connDB
from backend.app.core.security import create_access_token
from backend.app.features.auth.models import User
from backend.app.features.auth.schemas import LoginGoogleRequest, LoginRequest

router = APIRouter()


def verify_google_token(credential: str):
    gg_client_id = os.getenv("GG_CLIENT_ID")
    try:
        idinfo = id_token.verify_oauth2_token(
            credential,
            requests.Request(),
            gg_client_id,
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


@router.post("/login")
def login(loginReq: LoginRequest):
    user = connDB.users.find_one({"email": loginReq.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["_id"] = str(user["_id"])

    if user["provider"] != "local":
        raise HTTPException(
            status_code=400,
            detail=f"Please login with {user['provider']} provider",
        )
    if not bcrypt.checkpw(
        loginReq.password.encode("utf-8"),
        user["password"].encode("utf-8"),
    ):
        raise HTTPException(status_code=401, detail="Invalid password")

    userOb = User(
        full_name=user["full_name"],
        email=user["email"],
        provider=user["provider"],
        provider_id=user["provider_id"],
    )
    token = create_access_token(
        payload={
            "sub": user["_id"],
            "full_name": userOb.full_name,
            "email": userOb.email,
        }
    )
    return {
        "status": "success",
        "user": userOb.__todict__(),
        "access_token": token,
    }


@router.post("/login-google")
def login_google(loginReq: LoginGoogleRequest):
    google_user = verify_google_token(loginReq.credential)
    if not google_user:
        raise HTTPException(status_code=401, detail="Invalid Google token")

    user = connDB.users.find_one({"email": google_user["email"]})
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found, please register first",
        )
    user["_id"] = str(user["_id"])

    if user["provider"] != "google":
        raise HTTPException(
            status_code=400,
            detail=f"Please login with {user['provider']} provider",
        )

    userOb = User(
        full_name=user["full_name"],
        email=user["email"],
        provider=user["provider"],
        provider_id=user["provider_id"],
    )
    token = create_access_token(
        payload={
            "sub": str(user["_id"]),
            "full_name": userOb.full_name,
            "email": userOb.email,
        }
    )
    return {
        "status": "success",
        "user": userOb.__todict__(),
        "access_token": token,
    }
