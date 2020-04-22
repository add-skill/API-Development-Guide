from flask_restful import Resource, request
from flask_meal_app_step3.utils import Utils

import uuid

meal_user_map = {}
meal_map = {}


class Meals(Resource):

    def get(self):
        response_list = []
        for meal_id in meal_map:
            response_list.append((meal_map[meal_id]))

        return response_list

    def post(self):
        body = request.get_json()
        body["meal_id"] = str(uuid.uuid4())

        # Get Calorie information from Nutritionix
        try:
            if not body.get("calorie", None):
                body["calorie"] = int(Utils.nutritionix_calorie_count(
                    body.food_name))
        except Exception as ex:
            print('Could not reach Nutritionix to get data' + str(ex))
            body["calorie"] = 0

        # Update is_in_days_limit flag

        meal_map[body["meal_id"]] = body

        if meal_user_map.get("user_name", None):
            meal_user_map["user_name"].append(body["meal_id"])
        else:
            meal_user_map["user_name"] = [body["meal_id"]]

        return ({'meal_id': body["meal_id"]}), 201