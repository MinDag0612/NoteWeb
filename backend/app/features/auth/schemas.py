from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginGoogleRequest(BaseModel):
    credential: str
