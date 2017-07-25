import argparse

from flask import Flask, request
from orator.orm import belongs_to, has_many, belongs_to_many
from flask_orator import Orator, jsonify

from config import ApplicationConfig

parser = argparse.ArgumentParser()
parser.add_argument("-e", action="store", dest="environment",
        default="development", help="The app server environment")
options = parser.parse_args()

application_config = ApplicationConfig(options.environment)

# Flask application
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=application_config.debug_mode_is_enabled())
