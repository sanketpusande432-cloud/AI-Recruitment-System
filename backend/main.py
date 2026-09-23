from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.database import engine, Base, SessionLocal
from backend import models, schemas

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="AI Recruitment & Candidate Screening System"
)

@app.get("/")
def home():
    return {
        "message": "AI Recruitment System API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.post("/jobs")
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):

    new_job = models.Job(
        title=job.title,
        description=job.description,
        required_skills=job.required_skills,
        minimum_experience=job.minimum_experience
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job

@app.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs

@app.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):

    job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if job is None:
        return {"message": "Job not found"}

    return job