from typing import List, Dict

# "Tabelas" em memória
videos: List[Dict] = []  # cada vídeo: {"id", "title", "description", "notes": [ {...}, ... ]}
video_seq = 0

def next_video_id() -> int:
    global video_seq
    video_seq += 1
    return video_seq

def find_video(video_id: int):
    return next((v for v in videos if v["id"] == video_id), None)

# notes ficam dentro do próprio vídeo: video["notes"] = [ {"id", "text"} ]
def next_note_id_for(video: dict) -> int:
    # id incremental local por vídeo
    if not video["notes"]:
        return 1
    last = max(n["id"] for n in video["notes"])
    return last + 1
