# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


class Hello(Resource):

    def get(self):
        return jsonify({'message': 'hello world'})


class Users(Resource):

    def get(self):
        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):
        data = request.get_json()  # status code

        return jsonify({'data': data}), 201


class Meals(Resource):

    def get(self):
        return jsonify({'message': 'hello world'})

    def post(self):
        return jsonify({'message': 'hello world'})


class User(Resource):

    def get(self, username):
        return jsonify({'message': 'hello world'})

    def post(self, username):
        return jsonify({'message': 'hello world'})

    def post(self, username):
        return jsonify({'message': 'hello world'})


class Meal(Resource):

    def get(self, meal_id):
        return jsonify({'message': 'hello world'})

    def put(self, meal_id):
        return jsonify({'message': 'hello world'})

    def delete(self, meal_id):
        return jsonify({'message': 'hello world'})


api.add_resource(Hello, '/')
api.add_resource(Meals, '/users')
api.add_resource(Users, '/meals')
api.add_resource(Meal, '/users/<string:meal_id>')
api.add_resource(User, '/meals/<string:username>')

# driver function
if __name__ == '__main__':
    app.run(debug=True)