# using flask_restful

from flask import Flask
from flask_restful import Api
from flask_meal_app_step3.resources.Users import Users
from flask_meal_app_step3.resources.User import User
from flask_meal_app_step3.resources.Meals import Meals
from flask_meal_app_step3.resources.Meal import Meal
from flask_meal_app_step3.resources.Hello import Hello


# https://flask-restful.readthedocs.io/en/latest/intermediate-usage.html <-- Reference doc

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

api.add_resource(Hello, '/')
api.add_resource(Users, '/users')
api.add_resource(Meals, '/meals')
api.add_resource(Meal, '/users/<string:meal_id>')
api.add_resource(User, '/meals/<string:username>')

# driver function
if __name__ == '__main__':
    app.run(debug=True)