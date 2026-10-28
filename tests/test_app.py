from app import app


def test_app_creates_client():
    with app.test_client() as client:
        response = client.get('/login')
        assert response.status_code == 200


def test_dashboard_requires_login():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 302
