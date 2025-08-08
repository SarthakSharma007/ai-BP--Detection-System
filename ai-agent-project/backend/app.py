from flask import Flask, request, jsonify
from flask_cors import CORS
from model import analyze_symptoms

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    symptoms = data.get("symptoms", "")
    result = analyze_symptoms(symptoms)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
