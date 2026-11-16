from pydantic import BaseModel


class UpdateNoteRequest(BaseModel):
    noteId: str
    newTitle: str
    newContent: str
    newImages: list[str]


class DeleteNoteRequest(BaseModel):
    noteId: str
