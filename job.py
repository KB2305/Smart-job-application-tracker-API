from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app.auth import get_current_user
from typing import Optional

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/jobs")
def create_job(
    job: schemas.JobCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.create_job(db, job, user_id=user_id)



@router.get("/jobs")
def get_jobs(
    status: Optional[schemas.JobStatus] = None,
    company: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.get_jobs_filtered(
        db, user_id, status, company, limit, offset
    )

@router.get("/analytics")
def analytics(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.get_analytics(db, user_id)

@router.put("/jobs/{job_id}")
def update_job(
    job_id: int,
    job: schemas.JobCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.update_job(db, job_id, job, user_id)

@router.delete("/jobs/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud.delete_job(db, job_id, user_id)