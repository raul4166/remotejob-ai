from connectors.remotive import RemotiveConnector
from connectors.remoteok import RemoteOKConnector
from connectors.weworkremotely import WeWorkRemotelyConnector


def fetch_jobs_from_sources():
    jobs = []
    for connector in [RemotiveConnector(), RemoteOKConnector(), WeWorkRemotelyConnector()]:
        try:
            jobs.extend(connector.fetch_jobs())
        except Exception:
            continue
    return jobs
