import re

from database import db
from models import Job
from connectors import fetch_jobs_from_sources


def similarity(a, b):
    if not a or not b:
        return 0
    a = re.sub(r"\s+", " ", a.lower()).strip()
    b = re.sub(r"\s+", " ", b.lower()).strip()
    if a == b:
        return 1
    if a in b or b in a:
        return 0.8
    return 0


def is_duplicate(job_data):
    if job_data.get("url"):
        existing = Job.query.filter_by(url=job_data["url"]).first()
        if existing:
            return True
    for job in Job.query.all():
        if similarity(job.title, job_data.get("title", "")) > 0.7 and similarity(job.company, job_data.get("company", "")) > 0.7:
            return True
    return False


def save_job(job):
    if not job or not job.url:
        return None
    existing = Job.query.filter_by(url=job.url).first()
    if existing:
        return existing
    db.session.add(job)
    db.session.commit()
    return job


def refresh_jobs_from_sources():
    jobs = fetch_jobs_from_sources()
    count = 0
    for item in jobs:
        if is_duplicate(item):
            continue
        job = Job(
            external_id=item.get("external_id"),
            title=item.get("title") or "Untitled Role",
            company=item.get("company") or "Unknown Company",
            description=item.get("description") or "",
            salary=item.get("salary"),
            currency=item.get("currency"),
            url=item.get("url"),
            source=item.get("source") or "Unknown",
            job_type=item.get("job_type"),
            contract_type=item.get("contract_type"),
            skills=",".join(item.get("skills", [])),
            technologies=",".join(item.get("technologies", [])),
            required_experience=item.get("required_experience"),
            preferred_experience=item.get("preferred_experience"),
            language_requirements=item.get("language_requirements"),
            geographic_restrictions=item.get("geographic_restrictions"),
            accepted_countries=item.get("accepted_countries"),
            time_zone_requirements=item.get("time_zone_requirements"),
            posting_date=item.get("posting_date"),
            last_update_date=item.get("last_update_date"),
            is_remote=item.get("is_remote", True),
        )
        db.session.add(job)
        count += 1
    db.session.commit()
    return count


def get_jobs_by_filters(keyword="", source="", contract=""):
    query = Job.query
    if keyword:
        query = query.filter((Job.title.ilike(f"%{keyword}%")) | (Job.description.ilike(f"%{keyword}%")) | (Job.skills.ilike(f"%{keyword}%")))
    if source:
        query = query.filter(Job.source.ilike(f"%{source}%"))
    if contract:
        query = query.filter(Job.contract_type.ilike(f"%{contract}%"))
    return query.order_by(Job.created_at.desc()).all()
