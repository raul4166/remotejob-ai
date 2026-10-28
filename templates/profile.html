from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from pathlib import Path

from database import db
from models import Profile


profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", methods=["GET", "POST"])
def edit_profile():
    profile = Profile()

    if request.method == "POST":
        data = request.form
        profile.full_name = data.get("full_name")
        profile.professional_title = data.get("professional_title")
        profile.country = data.get("country")
        profile.time_zone = data.get("time_zone")
        profile.languages = data.get("languages")
        profile.technical_skills = data.get("technical_skills")
        profile.soft_skills = data.get("soft_skills")
        profile.years_of_experience = data.get("years_of_experience")
        profile.work_experience = data.get("work_experience")
        profile.education = data.get("education")
        profile.certifications = data.get("certifications")
        profile.portfolio = data.get("portfolio")
        profile.github = data.get("github")
        profile.linkedin = data.get("linkedin")
        profile.personal_website = data.get("personal_website")
        profile.salary_expectations = data.get("salary_expectations")
        profile.employment_preferences = data.get("employment_preferences")
        profile.availability = data.get("availability")
        profile.preferred_job_categories = data.get("preferred_job_categories")
        profile.preferred_industries = data.get("preferred_industries")
        profile.remote_work_preferences = data.get("remote_work_preferences")
        profile.contractor_availability = data.get("contractor_availability")
        profile.eligible_regions = data.get("eligible_regions")

        uploaded = request.files.get("resume")
        if uploaded and uploaded.filename:
            save_dir = Path("uploads/resumes")
            save_dir.mkdir(parents=True, exist_ok=True)
            safe_name = secure_filename(uploaded.filename)
            saved_path = save_dir / safe_name
            uploaded.save(saved_path)
            profile.resume_file = str(saved_path)
            flash(f"Resume saved: {safe_name}", "success")

        flash("Profile updated", "success")
        return redirect(url_for("profile.edit_profile"))

    return render_template("profile.html", profile=profile)
