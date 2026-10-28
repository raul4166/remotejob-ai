from connectors import fetch_jobs_from_sources


def test_connectors_run_without_error():
    jobs = fetch_jobs_from_sources()
    assert isinstance(jobs, list)
