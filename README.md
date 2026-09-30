# AI Recruitment & Candidate Screening System

An AI-assisted recruitment system that analyzes candidate resumes, compares them with job requirements, calculates a suitability score, retrieves relevant resume evidence, and generates an AI-based explanation to support recruiter review.

## Objective

The objective of this project is to simplify the initial candidate screening process by comparing job-related information from candidate resumes with stored job requirements.

The system is designed as a decision-support tool for recruiters. The final hiring decision remains with the human recruiter.

## Features

- Create and manage job requirements using REST APIs
- Store job information in PostgreSQL
- Upload candidate resumes in PDF format
- Extract resume text using PyMuPDF
- Extract candidate skills, experience, and education
- Compare candidate skills with job requirements
- Check minimum experience requirements
- Calculate a suitability score
- Rank candidates based on suitability score
- Retrieve relevant evidence from resume text
- Generate evidence-based AI explanations
- LangGraph-based screening workflow
- Redis caching for repeated screening requests
- Recruiter web dashboard
- FastAPI Swagger documentation
- Public cloud deployment using Render

## Technology Stack

### Backend
- Python
- FastAPI
- REST APIs
- SQLAlchemy
- PostgreSQL
- PyMuPDF

### AI and Retrieval
- Groq LLM
- LangGraph
- LangChain components
- TF-IDF Vectorization
- Cosine Similarity
- Retrieval-based AI workflow

### Caching
- Redis

### Frontend
- HTML
- CSS
- JavaScript

### Development and Deployment
- Git
- GitHub
- Postman
- Render

## System Workflow

1. Recruiter creates job requirements.
2. Job information is stored in PostgreSQL.
3. Recruiter selects a Job ID and uploads a candidate resume.
4. The system extracts text from the PDF resume.
5. Candidate skills, experience, and education are extracted.
6. Candidate information is compared with the selected job requirements.
7. A suitability score is calculated.
8. Relevant resume evidence is retrieved.
9. LangGraph manages the AI screening workflow.
10. Groq LLM generates an explanation based on the retrieved evidence.
11. Redis caches repeated screening results.
12. The final screening result is displayed on the recruiter dashboard.

## Suitability Scoring

The current project uses a simple job-related scoring method:

- Skill Match: 80%
- Experience Match: 20%

The score is intended only to assist recruiter review and should not be treated as an automatic hiring decision.

## API Endpoints

- `GET /` - API home
- `GET /health` - Health check
- `POST /jobs` - Create a new job
- `GET /jobs` - View all jobs
- `GET /jobs/{job_id}` - View a specific job
- `POST /upload-resume` - Upload and analyze a PDF resume
- `POST /match-candidate/{job_id}` - Match a candidate with a job
- `POST /ai-screen-candidate/{job_id}` - AI-assisted candidate screening

## Public Deployment

### Recruiter Dashboard
https://ai-recruitment-system-1-qfxe.onrender.com

### Backend API
https://ai-recruitment-system-xruu.onrender.com

### Swagger API Documentation
https://ai-recruitment-system-xruu.onrender.com/docs

The backend is hosted on a free cloud instance, so the first request after inactivity may take additional time while the service starts.

## Retrieval and Deployment Optimization

During development, the retrieval system was initially implemented using Chroma and HuggingFace embeddings.

Because the free deployment environment has limited memory, the deployed version was optimized to use TF-IDF vectorization and cosine similarity for lightweight resume evidence retrieval.

This allows the application to perform retrieval while remaining suitable for the available deployment resources.

## Project Structure

AI-Recruitment-System/
- backend/
  - database.py
  - extractor.py
  - llm.py
  - main.py
  - matcher.py
  - models.py
  - rag.py
  - redis_client.py
  - resume.py
  - schemas.py
  - workflow.py
- frontend/
  - index.html
  - style.css
  - script.js
- README.md
- requirements.txt

## Current Limitations

- Skill extraction currently uses a predefined skill list.
- The suitability scoring formula is a project-specific scoring method.
- The recruiter currently enters the Job ID manually.
- Scanned/image-only resumes are not supported because OCR is not implemented.
- The deployed retrieval implementation uses TF-IDF and cosine similarity instead of a persistent vector database.
- The system is a prototype and is not intended to make autonomous hiring decisions.

## Future Enhancements

- Job selection dropdown in the recruiter dashboard
- More advanced skill and experience extraction
- OCR support for scanned resumes
- Bulk resume screening
- Recruiter authentication
- Candidate comparison and ranking dashboard
- Persistent vector database deployment
- Improved configurable scoring criteria

## Responsible Use

The system evaluates job-related information such as skills and experience. It is designed to assist human recruiters and not replace human judgment.

Candidate screening should avoid the use of protected or sensitive personal characteristics when making employment decisions.

## Author

Sanket Pusande