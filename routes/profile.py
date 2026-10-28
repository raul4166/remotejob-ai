from collections import Counter
from pathlib import Path

from pypdf import PdfReader


def extract_keywords(text):
    if not text:
        return []
    words = [w.lower() for w in text.replace("/", " ").replace("-", " ").split() if len(w) > 3]
    counter = Counter(words)
    return [word for word, _ in counter.most_common(20)]


def _read_pdf_text(path):
    text_chunks = []
    try:
        reader = PdfReader(path)
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text_chunks.append(page_text)
    except Exception:
        return ""
    return "\n".join(text_chunks)


def load_resume_text(file_path):
    if not file_path:
        return ""
    file_path = str(file_path)
    resume_path = Path(file_path)
    if not resume_path.exists():
        return ""
    if resume_path.suffix.lower() == ".pdf":
        return _read_pdf_text(resume_path)
    if resume_path.suffix.lower() in {".txt", ".md"}:
        try:
            return resume_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return ""
    return ""


def generate_ats_resume(profile, job):
    if not profile:
        return {"title": "ATS Resume", "summary": "Profile not available."}

    resume_text = ""
    if getattr(profile, "resume_file", None):
        resume_text = load_resume_text(profile.resume_file)

    skills = (profile.technical_skills or "").split(",") if profile.technical_skills else []
    keywords = extract_keywords(job.description or "")
    base_summary = f"Experienced {profile.professional_title or 'professional'} with {profile.years_of_experience or 0} years of practical experience."

    if resume_text:
        resume_summary = base_summary + " Resume file uploaded and analyzed for ATS alignment."
    else:
        resume_summary = base_summary

    resume = {
        "title": profile.professional_title or "Technology Professional",
        "summary": resume_summary,
        "technical_skills": [s.strip() for s in skills if s.strip()],
        "keywords": keywords,
        "work_experience": profile.work_experience or "Professional experience in software products and delivery.",
        "resume_text_preview": resume_text[:1200],
    }
    return resume


def analyze_job_compatibility(profile, job):
    if not profile:
        return {"match_score": 0, "matching_skills": [], "missing_skills": []}

    resume_text = ""
    if getattr(profile, "resume_file", None):
        resume_text = load_resume_text(profile.resume_file)
    skills = [s.strip().lower() for s in (profile.technical_skills or "").split(",") if s.strip()]
    if resume_text:
        skills.extend([word.lower() for word in resume_text.split() if len(word) > 3])
    job_words = [w.lower() for w in (job.description or "").replace("-", " ").split() if len(w) > 3]
    matching = [word for word in job_words if word in skills]
    missing = [word for word in job_words if word not in skills][:8]
    score = min(100, max(0, int((len(matching) / max(1, len(job_words))) * 100)))
    return {
        "match_score": score,
        "matching_skills": matching,
        "missing_skills": missing,
        "recommendation": "Tailor the resume to the role requirements and improve keyword alignment.",
    }
