from flask import Flask
from flask_cors import CORS
from splunk_handler import SplunkHandler
import logging
from .config import Configuration

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Configuration)

    # Set up logging
    splunk_logger = SplunkHandler(
        token=app.config['SPLUNK_TOKEN'],
        host=app.config['SPLUNK_HOST'],
        port=app.config['SPLUNK_PORT'],
        index=app.config['SPLUNK_INDEX'],
        sourcetype=app.config['SPLUNK_SOURCETYPE'],
        source=app.config['SPLUNK_SOURCE'],
        protocol='https',
        verify=False
    )
    app.logger.addHandler(splunk_logger)
    app.logger.setLevel(logging.INFO)

    with app.app_context():
        # Import routes
        from . import routes

    return app
