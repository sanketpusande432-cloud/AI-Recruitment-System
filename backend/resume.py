from fastapi import APIRouter, UploadFile, File, HTTPException
import pymupdf

router = APIRouter()

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

    # Return the extracted text
    return {
        "filename": file.filename,
        "extracted_text": extracted_text
    }