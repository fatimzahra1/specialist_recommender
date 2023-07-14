from flask import Flask, jsonify, request
import joblib
from waitress import serve 
import numpy as np

app = Flask(__name__)

# Load the model

model= joblib.load("trained_model.joblib")

# Define a route for prediction 

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    data = np.array(list(data.values())).reshape(1,-1)
    prediction= model.predict(data)
    return jsonify({'prediction':prediction.tolist()})

# Run the Flask app

if __name__== '__main__':
    print("Flask app is running")
    app.run( host='0.0.0.0', port=5001)
