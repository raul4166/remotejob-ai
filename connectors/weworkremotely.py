import requests
import xml.etree.ElementTree as ET
from datetime import datetime

from connectors.base import BaseConnector


class WeWorkRemotelyConnector(BaseConnector):
    name = "We Work Remotely"
    description = "We Work Remotely RSS connector"

    def fetch_jobs(self, query=None):
        response = requests.get("https://weworkremotely.com/remote-jobs.rss", timeout=20)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        jobs = []
        for item in root.findall("./channel/item")[:20]:
            title = item.findtext("title") or "Remote Role"
            link = item.findtext("link") or "#"
            description = item.findtext("description") or ""
            jobs.append({
                "external_id": link,
                "title": title,
                "company": (title.split("-")[-1].strip() if "-" in title else "We Work Remotely"),
                "description": description,
                "salary": "",
                "currency": "USD",
                "url": link,
                "source": "We Work Remotely",
                "job_type": "Remote",
                "contract_type": "Full Time",
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
