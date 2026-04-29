from sqlalchemy import Column, Integer, String, ForeignKey, Date
from app.database import Base
import enum
from sqlalchemy import Enum

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)


class JobStatus(enum.Enum):
    applied = "applied"
    interview = "interview"
    rejected = "rejected"
    offer = "offer"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    role = Column(String)
    reminder_date = Column(Date, nullable=True)  # 👈 ADD THIS
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Enum(JobStatus), default=JobStatus.applied)
    location = Column(String)
    salary = Column(String)
    job_link = Column(String)
    notes = Column(String)
    applied_date = Column(Date)