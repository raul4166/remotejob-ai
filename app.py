from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

from config import Config
from database import db
from routes import auth_bp, dashboard_bp, jobs_bp, profile_bp, ats_bp, applications_bp
from services import refresh_jobs_from_sources

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(jobs_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(ats_bp)
    app.register_blueprint(applications_bp)

    with app.app_context():
        db.create_all()

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: refresh_jobs_from_sources(), trigger="interval", hours=6)
    scheduler.start()

    @app.context_processor
    def inject_defaults():
        return {
            "app_name": "RemoteJob AI",
            "year": 2026,
        }

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
