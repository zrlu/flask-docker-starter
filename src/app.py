from flask import Flask, jsonify, request
from flask_api import status


app = Flask(__name__)


@app.route('/api/ping')
def ping():
    args = request.args.to_dict()
    return jsonify({"args": args}), status.HTTP_200_OK