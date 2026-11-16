from datetime import datetime

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException

from backend.app.core.database import connDB
from backend.app.core.security import get_current_user
from backend.app.features.notes.models import Note
from backend.app.features.notes.schemas import DeleteNoteRequest, UpdateNoteRequest

router = APIRouter()


@router.post("/create-note")
def create_note(user: dict = Depends(get_current_user)):
    new_note = Note.default_note(
        user["sub"],
        datetime.now().strftime("%d/%m/%Y"),
    )
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


@router.get("/get-notes")
def get_notes(user: dict = Depends(get_current_user)):
    notes_cursor = connDB.notes.find({"user_id": user["sub"]})
    notes = [
        {
            "noteId": str(note["_id"]),
            "title": note["title"],
            "content": note["content"],
            "img": note["img"],
            "created_at": note["created_at"],
        }
        for note in notes_cursor
    ]
    return {"status": "success", "notes": notes}


@router.post("/notes/update")
def update_note(
    noteReq: UpdateNoteRequest,
    user: dict = Depends(get_current_user),
):
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


@router.delete("/delete-note")
def delete_note(
    noteReq: DeleteNoteRequest,
    user: dict = Depends(get_current_user),
):
    user_id = user["sub"]
    note = connDB.notes.find_one({"_id": ObjectId(noteReq.noteId)})
    if not note or note["user_id"] != user_id:
        raise HTTPException(status_code=404, detail="Note not found")

    delete_result = connDB.notes.delete_one({"_id": ObjectId(noteReq.noteId)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"status": "success", "message": "Note deleted successfully"}
