from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
import pymupdf

from backend.database import SessionLocal
from backend import models
from backend.extractor import extract_skills, extract_experience, extract_education, extract_job_skills
from backend.matcher import match_skills, match_experience, calculate_score

router = APIRouter()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # Check whether the uploaded file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    # Read the uploaded PDF
    pdf_bytes = await file.read()

    # Open the PDF
    try:
        pdf = pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file"
        )

    # Extract text from every page
    extracted_text = ""

    try:
        for page in pdf:
            extracted_text += page.get_text()

    finally:
        pdf.close()

    skills = extract_skills(extracted_text)
    experience = extract_experience(extracted_text)
    education = extract_education(extracted_text)

    return {
    "filename": file.filename,
    "extracted_text": extracted_text,
    "skills": skills,
    "experience": experience,
    "education": education
}

@router.post("/match-candidate/{job_id}")
async def match_candidate(
    job_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    job = db.query(models.Job).filter(models.Job.id == job_id).first()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    pdf_bytes = await file.read()

    try:
        pdf = pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf"
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file"
        )

    extracted_text = ""

    try:
        for page in pdf:
            extracted_text += page.get_text()
    finally:
        pdf.close()

    candidate_skills = extract_skills(extracted_text)
    candidate_experience = extract_experience(extracted_text)

    job_skills = extract_job_skills(job.required_skills)

    matched_skills, missing_skills = match_skills(
        candidate_skills,
        job_skills
    )

    experience_match = match_experience(
        candidate_experience,
        job.minimum_experience
    )

    score = calculate_score(
        matched_skills,
        job_skills,
        experience_match
    )

    return {
        "job_title": job.title,
        "candidate_skills": candidate_skills,
        "required_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "candidate_experience": candidate_experience,
        "required_experience": job.minimum_experience,
        "experience_match": experience_match,
        "suitability_score": score
    }