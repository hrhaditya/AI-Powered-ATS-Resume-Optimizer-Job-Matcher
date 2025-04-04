from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import os
import io
from dotenv import load_dotenv

# Load the .env file manually
load_dotenv(dotenv_path=".env")

# Get your Google API key from the .env file
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the .env file.")
else:
    print(f"Google API Key Loaded Successfully: {GOOGLE_API_KEY[:10]}...")  # For security, only print part of the key

genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI()

# Allow CORS so your Vercel app can communicate with your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze(resume: UploadFile, job_description: str = Form(...)):
    content = await resume.read()
    resume_text = extract_text(content, resume.filename)
    
    prompt = f"""
    Compare the following resume with the job description.
    Resume: {resume_text}
    Job Description: {job_description}
    """
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate(prompt=prompt)
    return {"result": response.text}

def extract_text(content, filename):
    text = ''
    if filename.endswith('.pdf'):
        reader = PdfReader(io.BytesIO(content))
        for page in reader.pages:
            text += page.extract_text()
    elif filename.endswith('.docx'):
        doc = Document(io.BytesIO(content))
        for para in doc.paragraphs:
            text += para.text + '\n'
    return text
