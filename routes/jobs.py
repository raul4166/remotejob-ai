from flask import Blueprint, render_template, request, flash, redirect, url_for

from models import Job
from services import save_job, get_jobs_by_filters


jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/jobs")
def list_jobs():
    keyword = request.args.get("keyword", "")
    source = request.args.get("source", "")
    contract = request.args.get("contract", "")
    jobs = get_jobs_by_filters(keyword=keyword, source=source, contract=contract)
    return render_template("jobs.html", jobs=jobs, keyword=keyword, source=source, contract=contract)


@jobs_bp.route("/jobs/<int:job_id>/save", methods=["POST"])
def save_job_route(job_id):
    job = Job.query.get_or_404(job_id)
    save_job(job)
    flash(f"Job saved: {job.title}", "success")
    return redirect(url_for("jobs.list_jobs"))
