from .auth import auth_bp
from .dashboard import dashboard_bp
from .jobs import jobs_bp
from .profile import profile_bp
from .ats import ats_bp
from .applications import applications_bp

__all__ = ["auth_bp", "dashboard_bp", "jobs_bp", "profile_bp", "ats_bp", "applications_bp"]
