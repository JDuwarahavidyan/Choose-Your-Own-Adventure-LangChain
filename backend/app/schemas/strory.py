from typing import Optional, List, Dict
from pydantic import BaseModel
from datetime import datetime

class StoryOptionsSchema(BaseModel):
   txt: str
   node_id: Optional[int] = None
   
class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False

class CompleteStoryNodeResponse(StoryNodeBase):
    id: int
    story_id: int
    options: List[StoryOptionsSchema] = []

    class Config:
        from_attributes = True
        
class StoryBase(BaseModel):
    title: str
    session_id: Optional[str] = None
    
    class Config:
        from_attributes = True

class CreateStoryRequest(StoryBase):
    theme: str
    
class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_node: CompleteStoryNodeResponse
    all_nodes: Dict[int, CompleteStoryNodeResponse]
    
    class Config:
        from_attributes = True # Allow Pydantic schemas to read values from object attributes (like SQLAlchemy models) instead of only dictionaries.
