import requests
import os
from flask import current_app as app

def download_artifact(file_name, path):
    artifact_url = f"{app.config['ARTIFACTORY_URL']}/artifactory/anand-local-generic/{file_name}"
    response = requests.get(artifact_url, auth=(app.config['ARTIFACTORY_USERNAME'], app.config['ARTIFACTORY_API_TOKEN']), verify=False)

    if response.status_code == 200:
        local_path = path
        with open(local_path, 'wb') as file:
            file.write(response.content)
        app.logger.info(f'Artifact downloaded to {local_path}')
    else:
        app.logger.error(f'Failed to download artifact. Status code: {response.status_code}')
