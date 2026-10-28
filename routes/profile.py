from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from database import db
from models import Profile


profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    profile = current_user.profile or Profile(user_id=current_user.id)

    if request.method == "POST":
        profile.full_name = request.form.get("full_name")
        profile.professional_title = request.form.get("professional_title")
        profile.country = request.form.get("country")
        profile.time_zone = request.form.get("time_zone")
        profile.languages = request.form.get("languages")
        profile.technical_skills = request.form.get("technical_skills")
        profile.soft_skills = request.form.get("soft_skills")
        profile.years_of_experience = request.form.get("years_of_experience")
        profile.work_experience = request.form.get("work_experience")
        profile.education = request.form.get("education")
        profile.certifications = request.form.get("certifications")
        profile.portfolio = request.form.get("portfolio")
        profile.github = request.form.get("github")
        profile.linkedin = request.form.get("linkedin")
        profile.personal_website = request.form.get("personal_website")
        profile.salary_expectations = request.form.get("salary_expectations")
        profile.employment_preferences = request.form.get("employment_preferences")
        profile.availability = request.form.get("availability")
        profile.preferred_job_categories = request.form.get("preferred_job_categories")
        profile.preferred_industries = request.form.get("preferred_industries")
        profile.remote_work_preferences = request.form.get("remote_work_preferences")
        profile.contractor_availability = request.form.get("contractor_availability")
        profile.eligible_regions = request.form.get("eligible_regions")
        db.session.add(profile)
        db.session.commit()
        flash("Profile updated", "success")
        return redirect(url_for("profile.edit_profile"))

    return render_template("profile.html", profile=profile)
