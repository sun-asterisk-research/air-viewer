from app.main import app
from flask import jsonify

@app.route("/api/")
def root():
    return jsonify({"message": "Hello World"})
