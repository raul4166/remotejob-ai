from collections import Counter


def extract_keywords(text):
    if not text:
        return []
    words = [w.lower() for w in text.replace("/", " ").replace("-", " ").split() if len(w) > 3]
    counter = Counter(words)
    return [word for word, _ in counter.most_common(20)]


def generate_ats_resume(profile, job):
    if not profile:
        return {"title": "ATS Resume", "summary": "Profile not available."}
    skills = (profile.technical_skills or "").split(",") if profile.technical_skills else []
    keywords = extract_keywords(job.description or "")
    resume = {
        "title": profile.professional_title or "Technology Professional",
        "summary": f"Experienced {profile.professional_title or 'professional'} with {profile.years_of_experience or 0} years of practical experience.",
        "technical_skills": [s.strip() for s in skills if s.strip()],
        "keywords": keywords,
        "work_experience": profile.work_experience or "Professional experience in software products and delivery.",
    }
    return resume


def analyze_job_compatibility(profile, job):
    if not profile:
        return {"match_score": 0, "matching_skills": [], "missing_skills": []}
    skills = [s.strip().lower() for s in (profile.technical_skills or "").split(",") if s.strip()]
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
