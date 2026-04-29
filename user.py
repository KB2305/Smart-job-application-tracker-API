from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database
from app import auth

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.post("/login")
def login(data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, data.email, data.password)
    if not user:
        return {"error": "Invalid credentials"}
    
    token = auth.create_access_token({"user_id": user.id})
    return {"access_token": token}