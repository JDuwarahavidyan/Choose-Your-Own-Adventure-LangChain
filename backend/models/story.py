from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import (
    func,
)  # To specify timestamp with timezone, we can use func.now() to get the current time in the database's timezone. This is useful for ensuring that timestamps are consistent regardless of the server's timezone settings.

from db.database import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(
        Integer, primary_key=True, index=True
    )  # Index makes it faster to search by id, rather than scanning the each row it directly goes to the row with that id.
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes = relationship("StoryNode", back_populates="story")


class StoryNode(Base):
    __tablename__ = "story_nodes"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id"), index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(JSON, default=list)
    options = Column(JSON, default=list)
    story = relationship("Story", back_populates="nodes")
