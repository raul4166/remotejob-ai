from flask import Blueprint, render_template

from models import Job
from services import analyze_job_compatibility, generate_ats_resume


ats_bp = Blueprint("ats", __name__)


@ats_bp.route("/ats")
def ats_index():
    jobs = Job.query.order_by(Job.created_at.desc()).limit(20).all()
    return render_template("ats.html", jobs=jobs)


@ats_bp.route("/ats/<int:job_id>")
def analyze_job(job_id):
    job = Job.query.get_or_404(job_id)
    profile = type(
        "ProfileStub",
        (),
        {
            "resume_file": None,
            "technical_skills": "",
            "professional_title": "Technology Professional",
            "years_of_experience": 0,
            "work_experience": "Professional experience in software products and delivery.",
        },
    )()
    analysis = analyze_job_compatibility(profile, job)
    resume = generate_ats_resume(profile, job)
    return render_template("ats.html", job=job, analysis=analysis, resume=resume, jobs=Job.query.order_by(Job.created_at.desc()).limit(20).all())
