from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.features.auth.router import router as auth_router
from backend.app.features.images.router import router as images_router
from backend.app.features.notes.router import router as notes_router

app = FastAPI(root_path="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # "https://dangtm.pro",
        # "https://www.dangtm.pro",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(notes_router)
app.include_router(images_router)


@app.get("/")
def health_check():
    return {"status": "API is running"}
