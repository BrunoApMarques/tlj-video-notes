from fastapi import FastAPI, HTTPException
from typing import List
from . import schemas
from .models_memory import videos, next_video_id, find_video, next_note_id_for

app = FastAPI(title="TLJ Video Notes", version="0.2.0")

@app.get("/health")
def health():
    # simples: se o app importou, está ok
    return {"ok": True}

# ---------- VIDEOS ----------
@app.post("/videos", response_model=schemas.VideoRead, status_code=201)
def create_video(payload: schemas.VideoCreate):
    vid = next_video_id()
    video = {
        "id": vid,
        "title": payload.title,
        "description": payload.description,
        "notes": [],  # lista de notas
    }
    videos.append(video)
    return _to_video_read(video)

@app.get("/videos", response_model=List[schemas.VideoRead])
def list_videos():
    return [_to_video_read(v) for v in videos]

@app.get("/videos/{video_id}", response_model=schemas.VideoRead)
def get_video(video_id: int):
    v = find_video(video_id)
    if not v:
        raise HTTPException(404, "video not found")
    return _to_video_read(v)

@app.put("/videos/{video_id}", response_model=schemas.VideoRead)
def update_video(video_id: int, payload: schemas.VideoUpdate):
    v = find_video(video_id)
    if not v:
        raise HTTPException(404, "video not found")
    if payload.title is not None:
        v["title"] = payload.title
    if payload.description is not None:
        v["description"] = payload.description
    return _to_video_read(v)

@app.delete("/videos/{video_id}", status_code=204)
def delete_video(video_id: int):
    idx = next((i for i, v in enumerate(videos) if v["id"] == video_id), None)
    if idx is None:
        raise HTTPException(404, "video not found")
    videos.pop(idx)
    return

# ---------- NOTES ----------
@app.post("/videos/{video_id}/notes", response_model=schemas.NoteRead, status_code=201)
def add_note(video_id: int, payload: schemas.NoteCreate):
    v = find_video(video_id)
    if not v:
        raise HTTPException(404, "video not found")
    nid = next_note_id_for(v)
    note = {"id": nid, "text": payload.text}
    v["notes"].append(note)
    return schemas.NoteRead(**note)

@app.get("/videos/{video_id}/notes", response_model=List[schemas.NoteRead])
def list_notes(video_id: int):
    v = find_video(video_id)
    if not v:
        raise HTTPException(404, "video not found")
    return [schemas.NoteRead(**n) for n in v["notes"]]

@app.delete("/videos/{video_id}/notes/{note_id}", status_code=204)
def delete_note(video_id: int, note_id: int):
    v = find_video(video_id)
    if not v:
        raise HTTPException(404, "video not found")
    idx = next((i for i, n in enumerate(v["notes"]) if n["id"] == note_id), None)
    if idx is None:
        raise HTTPException(404, "note not found")
    v["notes"].pop(idx)
    return

# ---------- helpers ----------
def _to_video_read(video: dict) -> schemas.VideoRead:
    return schemas.VideoRead(
        id=video["id"],
        title=video["title"],
        description=video["description"],
        notes=[schemas.NoteRead(**n) for n in video["notes"]],
    )
