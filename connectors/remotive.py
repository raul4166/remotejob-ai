import requests
from datetime import datetime

from connectors.base import BaseConnector


class RemotiveConnector(BaseConnector):
    name = "Remotive"
    description = "Remotive remote jobs connector"

    def fetch_jobs(self, query=None):
        response = requests.get("https://remotive.com/api/remote-jobs", timeout=20)
        response.raise_for_status()
        payload = response.json()
        jobs = []
        for item in payload.get("jobs", [])[:20]:
            jobs.append({
                "external_id": str(item.get("id")),
                "title": item.get("title"),
                "company": item.get("company"),
                "description": item.get("description") or "",
                "salary": item.get("salary") or "",
                "currency": item.get("currency") or "USD",
                "url": item.get("url"),
                "source": "Remotive",
                "job_type": item.get("job_type") or "Remote",
                "contract_type": item.get("job_type") or "Full Time",
                "skills": item.get("tags") or [],
                "technologies": item.get("tags") or [],
                "required_experience": "",
                "preferred_experience": "",
                "language_requirements": "",
                "is_remote": True,
                "posting_date": datetime.utcnow(),
                "last_update_date": datetime.utcnow(),
            })
        return jobs
