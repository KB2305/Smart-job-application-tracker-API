from pydantic import BaseModel
from datetime import date
from enum import Enum

class JobStatus(str, Enum):
    applied = "applied"
    interview = "interview"
    rejected = "rejected"
    offer = "offer"

class JobCreate(BaseModel):
    company: str
    role: str
    status: JobStatus
    reminder_date: date | None = None
    location: str | None = None
    salary: str | None = None
    job_link: str | None = None
    notes: str | None = None
    applied_date: date | None = None
    reminder_date: date | None = None

class UserCreate(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str