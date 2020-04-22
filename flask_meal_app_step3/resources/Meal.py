from flask_restful import Resource
from flask import jsonify


class Meal(Resource):

    def get(self, meal_id):
        return jsonify({'message': 'hello world'})

    def put(self, meal_id):
        return jsonify({'message': 'hello world'})

    def delete(self, meal_id):
        return jsonify({'message': 'hello world'})