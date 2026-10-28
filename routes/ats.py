from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models import Job
from services import analyze_job_compatibility, generate_ats_resume


ats_bp = Blueprint("ats", __name__)


@ats_bp.route("/ats")
@login_required
def ats_index():
    jobs = Job.query.order_by(Job.created_at.desc()).limit(20).all()
    return render_template("ats.html", jobs=jobs)


@ats_bp.route("/ats/<int:job_id>")
@login_required
def analyze_job(job_id):
    job = Job.query.get_or_404(job_id)
    profile = current_user.profile
    analysis = analyze_job_compatibility(profile, job)
    resume = generate_ats_resume(profile, job)
    return render_template("ats.html", job=job, analysis=analysis, resume=resume, jobs=Job.query.order_by(Job.created_at.desc()).limit(20).all())
