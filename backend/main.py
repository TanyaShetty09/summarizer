from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from services.summarizer import summarize_text
from services.pdf_generator import generate_pdf
from services.audio_generator import generate_audio
import shutil
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 1️⃣ Summarize text or uploaded document
@app.post("/summarize")
async def summarize(
    text: str = Form(None),
    file: UploadFile = File(None)
):
    content = ""

    if text:
        content = text

    elif file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Read text file only (for simplicity)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

    else:
        return {"error": "Provide text or upload a document"}

    summary = summarize_text(content)

    return {"summary": summary}


# 2️⃣ Generate PDF from text
@app.post("/generate-pdf")
async def create_pdf(text: str = Form(...)):
    pdf_path = os.path.join(UPLOAD_FOLDER, "summary.pdf")
    generate_pdf(text, pdf_path)
    return FileResponse(pdf_path, media_type="application/pdf", filename="summary.pdf")


# 3️⃣ Generate Audio from text
@app.post("/generate-audio")
async def create_audio(text: str = Form(...)):
    audio_path = os.path.join(UPLOAD_FOLDER, "summary.mp3")
    generate_audio(text, audio_path)
    return FileResponse(audio_path, media_type="audio/mpeg", filename="summary.mp3")