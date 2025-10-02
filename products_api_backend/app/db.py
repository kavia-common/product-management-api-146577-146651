from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy instance shared across modules
db = SQLAlchemy()


def init_db(app: Flask) -> None:
    """
    Initialize database with the given Flask app and create all tables.
    This sets up the SQLite database connection using SQLAlchemy.

    Args:
        app: Flask application instance.
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
