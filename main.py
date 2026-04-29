from fastapi import FastAPI
from app.database import Base, engine
from app.routes.job import router as job_router
from app.routes.user import router as user_router
import threading
from app.scheduler import check_reminders

app = FastAPI()

# ✅ FIRST create tables
Base.metadata.create_all(bind=engine)

# ✅ THEN start background thread
threading.Thread(target=check_reminders, daemon=True).start()

# ✅ THEN include routes
app.include_router(user_router)
app.include_router(job_router)

@app.get("/")
def root():
    return {"message": "Job Tracker API Running"}