from fastapi import FastAPI, Path, Query, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db import get_db, Note


app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.get("/hello")
async def hello():
    return {"mesage": "Hello World!"}


@app.get("/notes/{note_id}")
async def read_notes(
    note_id: int = Path(
        description="The ID of the note to get", gt=0, le=10
    ),
    skip: int = 0, 
    limit: int = Query(default=10, le=100, ge=10),
    session: Session = Depends(get_db)
):
    return session.query(Note).get(note_id)


class NoteModel(BaseModel):
    name: str
    description: str
    done: bool
    

@app.post("/notes")
async def create_note(
    note: NoteModel,
    session: Session = Depends(get_db)
):
    session.add(Note(**note.dict()))
    session.commit()
    return note
