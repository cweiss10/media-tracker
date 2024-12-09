from pydantic import BaseModel
from typing import Optional
from datetime import date
from models import MediaStatus

# Pydantic Schema for MediaItem
class MediaItemBase(BaseModel):
    title: str
    author_creator: Optional[str] = None
    genre: Optional[str] = None
    date_started: Optional[date] = None
    date_finished: Optional[date] = None
    rating: Optional[float] = None
    review: Optional[str] = None
    description: Optional[str] = None
    media_type: str
    status: MediaStatus

class MediaItemCreate(MediaItemBase):
    pass

class MediaItemResponse(MediaItemBase):
    id: int

    class Config:
        orm_mode = True
