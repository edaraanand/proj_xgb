from flask import request, jsonify, current_app as app
import xgboost as xgb
import numpy as np
from .utils import download_artifact

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return jsonify({"message": "Hello, APS!"})

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    if 'values' in data and isinstance(data['values'], list):
        li = data['values']
    feature_data = np.array([li])
    app.logger.info("Input data is transformed")

    # Download and load mode
    model_name= app.config['MODEL_NAME']
    model_path = f"./{model_name}"
    download_artifact(model_name, model_path)
    loaded_model = xgb.Booster()
    loaded_model.load_model(model_path)
    app.logger.info("Model is loaded")

    score = loaded_model.predict(xgb.DMatrix(feature_data))

    return jsonify({'score': score.tolist()})

@app.route('/error')
def error():
    app.logger.error("This is an error message")
    return "This is an error route!", 500
