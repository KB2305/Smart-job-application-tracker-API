# Smart-job-application-tracker-API
A backend system built to help users efficiently track and manage job applications. It supports authentication, job tracking, filtering, analytics, and automated reminders—simulating real-world backend workflows.


## 📌 Features
- 🔐 JWT Authentication (Register & Login)
- 📊 CRUD Operations for job applications
- 🔎 Filtering & Pagination for efficient data retrieval
- 📈 Analytics Endpoint to track application status
- ⏰ Background Reminder System for follow-ups
- 🧠 Enum-based Status Control (applied, interview, rejected, offer)
- 👤 User-specific Data Isolation


## 🛠️ Tech Stack
- Language: Python
- Framework: FastAPI
- Database: SQLite
- ORM: SQLAlchemy
- Authentication: JWT (JSON Web Tokens)
- Other: Background Threads (for reminders)

## 📂 Project Structure
```
App/
│── main.py 
│── models.py
│── schemas.py
│── database.py
│── crud.py
│── auth.py
│── scheduler.py
|
│── routes/
│   ├── __init__.py
│   ├── job.py
│   └── user.py
└── requirements.txt # Dependencies

```

## ⚙️ Installation & Setup


### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd job-application-tracker
```

### 2. Create a Virtual Environment

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```


### 3. Install Dependencies

If a `requirements.txt` file exists:
```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

## 📡 API Documentation

Once the server is running, open:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

👉 Interactive Swagger UI to test all endpoints

## 🔑 Authentication Flow

- Register user → /register
- Login → /login → get JWT token
- Use token in Swagger:
 Authorize → Bearer <your_token>



## 🧪 Example Request (Create Job)
```bash
{
"company": "Google",
"role": "Software Engineer",
"status": "applied",
"location": "Remote",
"salary": "10 LPA",
"applied_date": "2026-04-29",
"reminder_date": "2026-05-01"
}

```

## 📊 Example Features in Action

- Filter jobs by status or company
- Track progress of applications
- View analytics (applied vs interview vs rejected)
- Get reminders for follow-ups

## 🎯 Purpose
This project demonstrates:

- Backend system design
- Secure authentication
- Database modeling
- API development
- Background task handling


## 🚀 Future Improvements

- Email notifications for reminders
- Frontend dashboard
- Deployment (AWS / Docker)
- Advanced analytics  

---

## 📄 License

This project is released under the **MIT License**. You can add a `LICENSE` file to reflect this.

---
