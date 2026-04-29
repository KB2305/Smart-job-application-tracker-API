from sqlalchemy.orm import Session
from app import models, schemas, auth
from sqlalchemy import func


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = auth.hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    print("USER CREATED:", db_user.email, db_user.password)  # 👈 DEBUG

    return db_user

def create_job(db: Session, job: schemas.JobCreate, user_id: int):
    db_job = models.Job(**job.dict(), user_id=user_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_jobs(db: Session):
    return db.query(models.Job).all()

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()

    print("LOGIN ATTEMPT:", email, password)  # 👈
    print("DB USER:", user)  # 👈

    if not user:
        return None

    print("HASHED PW:", user.password)  # 👈

    if not auth.verify_password(password, user.password):
        print("PASSWORD MISMATCH")  # 👈
        return None

    return user


def get_jobs_by_user(db: Session, user_id: int):
    return db.query(models.Job).filter(models.Job.user_id == user_id).all()

def get_jobs_filtered(db, user_id, status, company, limit, offset):
    query = db.query(models.Job).filter(models.Job.user_id == user_id)

    if status:
        query = query.filter(models.Job.status == status)

    if company:
        query = query.filter(models.Job.company == company)

    return query.offset(offset).limit(limit).all()


def get_analytics(db, user_id):
    total_jobs = db.query(models.Job).filter(
        models.Job.user_id == user_id
    ).count()

    status_counts = db.query(
        models.Job.status,
        func.count(models.Job.status)
    ).filter(
        models.Job.user_id == user_id
    ).group_by(models.Job.status).all()

    status_dict = {status: count for status, count in status_counts}

    return {
        "total_jobs": total_jobs,
        "status_breakdown": status_dict
    }

def update_job(db, job_id, job, user_id):
    db_job = db.query(models.Job).filter(
        models.Job.id == job_id,
        models.Job.user_id == user_id
    ).first()

    if not db_job:
        return {"error": "Job not found"}

    for key, value in job.dict().items():
        setattr(db_job, key, value)

    db.commit()
    db.refresh(db_job)

    return db_job