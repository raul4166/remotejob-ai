from database import db


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)

    full_name = db.Column(db.String(200), nullable=True)
    professional_title = db.Column(db.String(200), nullable=True)
    country = db.Column(db.String(120), nullable=True)
    time_zone = db.Column(db.String(120), nullable=True)
    languages = db.Column(db.Text, nullable=True)
    technical_skills = db.Column(db.Text, nullable=True)
    soft_skills = db.Column(db.Text, nullable=True)
    years_of_experience = db.Column(db.Integer, nullable=True)
    work_experience = db.Column(db.Text, nullable=True)
    education = db.Column(db.Text, nullable=True)
    certifications = db.Column(db.Text, nullable=True)
    portfolio = db.Column(db.String(255), nullable=True)
    github = db.Column(db.String(255), nullable=True)
    linkedin = db.Column(db.String(255), nullable=True)
    personal_website = db.Column(db.String(255), nullable=True)
    salary_expectations = db.Column(db.String(120), nullable=True)
    employment_preferences = db.Column(db.Text, nullable=True)
    availability = db.Column(db.String(120), nullable=True)
    preferred_job_categories = db.Column(db.Text, nullable=True)
    preferred_industries = db.Column(db.Text, nullable=True)
    remote_work_preferences = db.Column(db.Text, nullable=True)
    contractor_availability = db.Column(db.String(50), nullable=True)
    eligible_regions = db.Column(db.Text, nullable=True)
    resume_file = db.Column(db.String(255), nullable=True)
