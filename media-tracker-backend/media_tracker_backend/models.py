from sqlalchemy import Column, Integer, String, Float, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()

# Media Status Enum
class MediaStatus(PyEnum):
    STARTED = "started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"
    DID_NOT_FINISH = "did not finish"

class MediaItem(Base):
    __tablename__ = "media_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_creator = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    date_started = Column(Date, nullable=True)
    date_finished = Column(Date, nullable=True)
    rating = Column(Float, nullable=True)
    review = Column(String, nullable=True)
    description = Column(String, nullable=True)
    media_type = Column(String, nullable=False)
    status = Column(Enum(MediaStatus), nullable=False)
