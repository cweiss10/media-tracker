from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Base, MediaItem, MediaStatus
from database import engine, SessionLocal
from crud import create_media_item, get_media_items
from schemas import MediaItemCreate, MediaItemResponse
from fastapi.middleware.cors import CORSMiddleware

# Initialize Database
Base.metadata.create_all(bind=engine)


app = FastAPI()

# Allow all origins (be more specific in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change "*" to specific URLs in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/media/", response_model=MediaItemResponse)
def create_media(media_item: MediaItemCreate, db: Session = Depends(get_db)):
    media_db_item = MediaItem(**media_item.dict())
    return create_media_item(db, media_db_item)

@app.get("/media/", response_model=list[MediaItemResponse])
def read_media(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_media_items(db, skip, limit)
