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
    try:
         data = request.json
         data = np.array(list(data.values())).reshape(1,-1)
         prediction= model.predict(data)
         return jsonify({'prediction':prediction.tolist()})
    except Exception as e:
        return jsonify({"error":str(e)})
    
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error":"Not Found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error":"Not Found"}), 404
        
   

# Run the Flask app

if __name__== '__main__':
    print("Flask app is running")
    app.run( host='0.0.0.0', port=5000)
