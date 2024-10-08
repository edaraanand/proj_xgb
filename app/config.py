import os
from dotenv import load_dotenv

load_dotenv()

class Configuration:
    ARTIFACTORY_URL = os.getenv('ARTIFACTORY_URL')
    ARTIFACTORY_USERNAME = os.getenv('ARTIFACTORY_USERNAME')
    ARTIFACTORY_API_TOKEN = os.getenv('ARTIFACTORY_API_TOKEN')
    SPLUNK_TOKEN = os.getenv('SPLUNK_TOKEN')
    SPLUNK_HOST = os.getenv('SPLUNK_HOST')
    SPLUNK_PORT = os.getenv('SPLUNK_PORT')
    SPLUNK_INDEX = os.getenv('SPLUNK_INDEX')
    SPLUNK_SOURCETYPE = os.getenv('SPLUNK_SOURCETYPE')
    SPLUNK_SOURCE = os.getenv('SPLUNK_SOURCE')
    MODEL_NAME = os.getenv('MODEL_NAME')
