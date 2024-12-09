from sqlalchemy.orm import Session
from models import MediaItem

def create_media_item(db: Session, media_item: MediaItem):
    db.add(media_item)
    db.commit()
    db.refresh(media_item)
    return media_item

def get_media_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MediaItem).offset(skip).limit(limit).all()
