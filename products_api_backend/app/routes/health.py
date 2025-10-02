from flask_smorest import Blueprint
from flask.views import MethodView

# Health check blueprint for uptime verification
blp = Blueprint("Health Check", "health", url_prefix="/", description="Health check route")


@blp.route("/")
class HealthCheck(MethodView):
    """
    PUBLIC_INTERFACE
    get:
        Returns a simple health status message.
    """
    def get(self):
        """Health probe endpoint used for uptime checks."""
        return {"message": "Healthy"}
