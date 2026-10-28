from flask import Blueprint, render_template, redirect, url_for, flash
from datetime import datetime

from database import db
from models import Application, Job


applications_bp = Blueprint("applications", __name__)


@applications_bp.route("/applications")
def list_applications():
    apps = Application.query.order_by(Application.created_at.desc()).all()
    return render_template("applications.html", applications=apps)


@applications_bp.route("/applications/new/<int:job_id>", methods=["POST"])
def create_application(job_id):
    job = Job.query.get_or_404(job_id)
    app = Application(
        user_id=1,
        job_id=job.id,
        company=job.company,
        position=job.title,
        source=job.source,
        url=job.url,
        salary=job.salary,
        status="New",
        application_date=datetime.utcnow(),
        notes="Application prepared.",
        status_history='["New"]',
    )
    db.session.add(app)
    db.session.commit()
    flash("Application created", "success")
    return redirect(url_for("applications.list_applications"))
