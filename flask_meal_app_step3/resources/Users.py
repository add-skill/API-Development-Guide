from flask_restful import Resource, request
from flask import jsonify


class Users(Resource):

    def get(self):
        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):
        data = request.get_json()  # status code

        return jsonify({'data': data}), 201