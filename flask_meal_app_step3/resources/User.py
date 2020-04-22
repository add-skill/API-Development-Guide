from flask_restful import Resource
from flask import jsonify


class User(Resource):

    def get(self, username):
        return jsonify({'message': 'hello world'})

    def post(self, username):
        return jsonify({'message': 'hello world'})

    def post(self, username):
        return jsonify({'message': 'hello world'})