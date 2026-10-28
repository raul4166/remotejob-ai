import requests
from datetime import datetime

from connectors.base import BaseConnector


class RemoteOKConnector(BaseConnector):
    name = "RemoteOK"
    description = "RemoteOK public jobs connector"

    def fetch_jobs(self, query=None):
        response = requests.get("https://remoteok.com/api", timeout=20)
        response.raise_for_status()
        payload = response.json()
        jobs = []
        for item in payload[:20]:
            if not isinstance(item, dict):
                continue
            jobs.append({
                "external_id": str(item.get("id")),
                "title": item.get("position"),
                "company": item.get("company"),
                "description": item.get("description") or "",
                "salary": item.get("salary") or "",
                "currency": "USD",
                "url": item.get("url"),
                "source": "RemoteOK",
                "job_type": "Remote",
                "contract_type": item.get("employment_type") or "Full Time",
                "skills": [],
                "technologies": [],
                "required_experience": "",
                "preferred_experience": "",
                "language_requirements": "",
                "is_remote": True,
                "posting_date": datetime.utcnow(),
                "last_update_date": datetime.utcnow(),
            })
        return jobs
