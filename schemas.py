from pydantic import BaseModel
from typing import List, Optional

# ---------- NOTES ----------
class NoteCreate(BaseModel):
    text: str

class NoteRead(BaseModel):
    id: int
    text: str

class NoteUpdate(BaseModel):
    text: Optional[str] = None

# ---------- VIDEOS ----------
class VideoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class VideoRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    notes: List[NoteRead] = []

class VideoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
