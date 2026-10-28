from database import db


class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(120), nullable=True)
    title = db.Column(db.String(250), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    salary = db.Column(db.String(120), nullable=True)
    currency = db.Column(db.String(20), nullable=True)
    url = db.Column(db.String(500), nullable=False)
    source = db.Column(db.String(120), nullable=False)
    job_type = db.Column(db.String(80), nullable=True)
    contract_type = db.Column(db.String(80), nullable=True)
    skills = db.Column(db.Text, nullable=True)
    technologies = db.Column(db.Text, nullable=True)
    required_experience = db.Column(db.String(120), nullable=True)
    preferred_experience = db.Column(db.String(120), nullable=True)
    language_requirements = db.Column(db.Text, nullable=True)
    geographic_restrictions = db.Column(db.Text, nullable=True)
    accepted_countries = db.Column(db.Text, nullable=True)
    time_zone_requirements = db.Column(db.Text, nullable=True)
    posting_date = db.Column(db.DateTime, nullable=True)
    last_update_date = db.Column(db.DateTime, nullable=True)
    is_remote = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
