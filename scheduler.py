import time
from datetime import date
from app.database import SessionLocal
from app import models

def check_reminders():
    while True:
        try:
            db = SessionLocal()
            today = date.today()

            jobs = db.query(models.Job).filter(
                models.Job.reminder_date == today
            ).all()

            for job in jobs:
                print(f"🔔 Reminder: {job.company} - {job.role}")

            db.close()

        except Exception as e:
            print("Scheduler error:", e)

        time.sleep(60)