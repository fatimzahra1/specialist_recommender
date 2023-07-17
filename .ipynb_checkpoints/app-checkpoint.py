from flask import Flask, jsonify, request
import joblib
from waitress import serve
import numpy as np
from symptoms import my_dict

app = Flask(__name__)

# Load the model
model = joblib.load("trained_model.joblib")


@app.route('/', methods=['GET'])
def get():
    try:
        return jsonify(my_dict)
    except Exception as e:
        return jsonify({"error": str(e)})


# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data_array = request.json

        for symptom in data_array:
            if symptom in my_dict:
                my_dict[symptom] = 1

        data = np.array(list(my_dict.values())).reshape(1, -1)

        prediction = model.predict(data)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500


# Run the Flask app
if __name__ == '__main__':
    print("Flask app is running")
    app.run(host='0.0.0.0', port=5000)