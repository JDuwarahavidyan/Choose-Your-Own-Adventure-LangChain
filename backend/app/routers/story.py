import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from db.database import SessionLocal, get_db
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.strory import CompleteStoryResponse, CompleteStoryNodeResponse, CreateStoryRequest
from schemas.job import StoryJobResponse

router = APIRouter(
    prefix="/stories",
    tags=["stories"]
)

def get_session_id(session_id: Optional[str] = Cookie(None)) -> str:
    if not session_id:
        session_id = str(uuid.uuid4())
    return session_id


@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/create", response_model=StoryJobResponse) # Check Nortan
def create_story(
    request: CreateStoryRequest,
    background_tasks: BackgroundTasks,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db)
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    
    job_id = str(uuid.uuid4())
    
    job = StoryJob(
        job_id=job_id,
        session_id=session_id,
        theme=request.theme,
        status="pending"
    )
    
    db.add(job)
    db.commit()
    
    background_tasks.add_task(
        generate_story_task,
        job_id=job_id,
        session_id=session_id,
        theme=request.theme
    )
    
    return job

def generate_story_task(job_id: str, session_id: str, theme: str):
    
    db = SessionLocal()
    
    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
        
        if not job:
            return
        
        try:
            job.status = "processing"
            db.commit()
            
            story = {} # TODO: Generate story based on theme
            
            job.story_id = story.id
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()
            
        except Exception as e:
            job.status = "failed"
            job.completed_at = datetime.now()
            job.error = str(e)
            db.commit()
    
    finally:
        db.close()
    

@router.get("/{story_id}/complete", response_model=CompleteStoryResponse)
def get_complete_story(
    story_id: int,
    db: Session = Depends(get_db)
):
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    
    # TODO: Parse the story that can be accepted by the frontend
    
    #This function converts database data into the frontend format.
    # Because database models are usually not structured exactly how the frontend expects.
    complete_story = build_complete_story_response(db, story)
    
    return complete_story

def build_complete_story_response(db: Session, story: Story) -> CompleteStoryResponse:
    """
    This function is supposed to:
        - fetch story nodes
        - determine the root node
        - organize nodes
        - return a structured response

    """
    pass
 