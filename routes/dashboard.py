from flask import Blueprint, render_template

from models import Job, Application


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    total_jobs = Job.query.count()
    applications = Application.query.count()
    interviews = Application.query.filter_by(status="Interview").count()
    return render_template(
        "dashboard.html",
        total_jobs=total_jobs,
        applications=applications,
        saved_jobs=total_jobs,
        interviews=interviews,
        jobs=Job.query.order_by(Job.created_at.desc()).limit(8).all(),
    )
