# app.py

from flask import Flask, request, jsonify
from tensorflow import keras

app = Flask(__name__)

# Load the entire model
model = keras.models.load_model('model_weights.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['input']])
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)