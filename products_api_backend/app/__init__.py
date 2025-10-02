from flask import Flask
from flask_cors import CORS
from flask_smorest import Api

# Import blueprints
from .routes.health import blp as health_blp
from .routes.products import blp as products_blp

# Import database initialization
from .db import init_db


def create_app() -> Flask:
    """
    Factory to create and configure the Flask application.

    - Configures API metadata and OpenAPI/Swagger UI.
    - Initializes SQLite database and creates tables.
    - Registers blueprints for routes.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # CORS for all endpoints (development-friendly)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Ocean Professional theme-aligned API metadata
    app.config["API_TITLE"] = "Products API - Ocean Professional"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # SQLite configuration (file-based persistence, development-ready)
    # Note: Do not hard-code sensitive config; for dev this is acceptable.
    # For production, move to environment variables.
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize DB and API
    init_db(app)
    api = Api(app)

    # Register route blueprints
    api.register_blueprint(health_blp)
    api.register_blueprint(products_blp)

    return app


# Create app instance for WSGI servers
app = create_app()
