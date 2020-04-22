# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_meal_app_step2.utils import Utils

import uuid
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

meal_user_map = {}
meal_map = {}


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
        response_list = []
        for meal_id in meal_map:
            response_list.append(jsonify(meal_map[meal_id]))

        return response_list

    def post(self):
        body = request.get_json()
        body.meal_id = str(uuid.uuid4())

        # Get Calorie information from Nutritionix
        try:
            if not body.calorie:
                body.calorie = int(Utils.nutritionix_calorie_count(
                    body.food_name))
        except Exception as ex:
            print('Could not reach Nutritionix to get data' + str(ex))
            body.calorie = 0

        # Update is_in_days_limit flag

        meal_map[body.meal_id] = body

        if meal_user_map.get("user_name", None):
            meal_user_map["user_name"].append(body.meal_id)
        else:
            meal_user_map["user_name"] = [body.meal_id]

        return jsonify({'meal_id': body.meal_id}), 201


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