from fastapi import FastAPI

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