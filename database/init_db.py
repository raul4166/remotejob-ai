from database import db


def initialize_database(app):
    with app.app_context():
        db.create_all()
