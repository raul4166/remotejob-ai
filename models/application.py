from database import db


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.id"), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(200), nullable=False)
    source = db.Column(db.String(120), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    salary = db.Column(db.String(120), nullable=True)
    resume_used = db.Column(db.String(200), nullable=True)
    cover_letter_used = db.Column(db.String(200), nullable=True)
    application_date = db.Column(db.DateTime, nullable=True)
    follow_up_date = db.Column(db.DateTime, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(80), default="New")
    status_history = db.Column(db.Text, default="[]")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
