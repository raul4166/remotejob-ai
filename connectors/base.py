class BaseConnector:
    name = "base"
    version = "1.0"
    description = "Base connector implementation"

    def fetch_jobs(self, query=None):
        return []
