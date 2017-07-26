import os

from dotenv import load_dotenv
from flask import Flask, request
from flask_orator import Orator, jsonify

from config import ApplicationConfig
from controllers.api import ApiController

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
environment = os.getenv("ENVIRONMENT", "development")
application_config = ApplicationConfig.get_instance(environment=environment)

# Flask application
app = Flask(__name__)
app.config["APPLICATION_CONFIG"] = application_config
app.config["ORATOR_DATABASES"] = {
        environment: application_config.database_config()
        }

# Orator db
db = Orator(app)

# controllers
ApiController(app).register()

if __name__ == "__main__":
    app.run(debug=application_config.debug_mode_is_enabled())
