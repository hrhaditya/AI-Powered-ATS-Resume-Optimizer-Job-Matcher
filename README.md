🧠 AI-Powered ATS Resume Optimizer & Job Matcher

An intelligent, full-stack application designed to help job seekers optimize their resumes and improve their chances of passing Applicant Tracking Systems (ATS). This tool leverages Google Gemini Pro, FastAPI, and React (with Lovable UI) to parse resumes, compare them against job descriptions, and provide real-time feedback with actionable suggestions.
🎯 Objective

Job seekers often get rejected by automated ATS filters before a human even reviews their resume. This tool simulates ATS behavior using a Gemini Pro LLM engine and provides:

    Instant resume-to-JD compatibility scoring

    Smart, personalized rewrite suggestions

    Gap analysis to identify missing keywords or skills

✨ Live Demo

🔗 Try the Live App
🧪 Upload your resume (PDF or DOCX) and a job description, and get:

    An ATS Match Score

    Key gaps and mismatches

    AI-suggested improvements to align better with the role

📌 Key Features
📄 Resume Parsing

    Converts uploaded resumes (PDF/DOCX) into structured, clean text

    Extracts education, skills, experience, and more using NLP

🧠 LLM-Powered Scoring (Gemini Pro)

    Sends parsed resume and job description to Gemini Pro via prompt engineering

    Returns an ATS-style score, explanation, and keyword relevance

🔍 Gap Analysis

    Highlights key differences in skills, technologies, and language tone

    Identifies missing job-specific terms or experience areas

✍️ Resume Optimization Suggestions

    Offers rewrite suggestions for each job description

    Optional: export revised resume sections in real time (beta)

⚙️ Full-Stack Architecture

    Built using modern tech stack

    Modularized and production-ready for real-world deployment

🧰 Tech Stack
Layer	Tools/Frameworks
Frontend	React.js, Tailwind CSS, Lovable UI
Backend	FastAPI, Python, Pydantic, Resume Parser
AI Engine	Google Gemini Pro API (Text-based LLM prompt flow)
Hosting	Vercel (Frontend), Local/Cloud-hosted FastAPI Server
DevOps	CI/CD ready, GitHub workflows (optional integration)
📂 Project Structure

job-scan-pro/
├── backend/
│   ├── main.py                # FastAPI app
│   ├── ats_score_engine.py    # Gemini Pro prompt + analysis logic
│   └── parser.py              # Resume parsing (PDF/DOCX)
├── frontend/
│   ├── src/
│   │   ├── components/        # Lovable UI-based React components
│   │   └── pages/             # Upload, Score, and Results views
├── assets/                    # Icons, visuals
├── README.md
└── requirements.txt

📊 Example Output

    After uploading your resume and job description, you’ll receive:

    ✅ An ATS Score out of 100

    🧩 Key matches and mismatches (skills, experience, job-specific lingo)

    💡 Tailored recommendations to optimize your resume

🚀 How to Run Locally

    Clone the repository

git clone https://github.com/hrhaditya/job-scan-pro
cd job-scan-pro

Backend (FastAPI)

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Frontend (React)

    cd frontend
    npm install
    npm run dev

    Access

        Frontend: http://localhost:3000

        Backend: http://localhost:8000

🧠 Sample Prompt (Gemini Pro)

Compare the resume below with the job description and provide:
1. ATS-style match score out of 100
2. Top 5 matching keywords or phrases
3. Top 5 missing keywords
4. Bullet-point suggestions to optimize the resume for this job

Resume:
<parsed resume here>

Job Description:
<job description here>

🔮 Future Improvements

    ✨ Export resume suggestions directly into editable formats (Word, PDF)

    🤖 Resume rewriting assistant using Gemini chat

    📈 Dashboard to track job applications, scores, and improvements

    🧾 Cover letter generation based on JD + resume

📌 Repo

🔗 GitHub – job-scan-pro
🔗 Live App on Vercel
