import http.client
import json


class Utils:
    def nutritionix_calorie_count(food_name):
        payload = {"query": food_name}
        conn = http.client.HTTPSConnection("trackapi.nutritionix.com")
        headers = {
            'x-app-id': 'd4983d18',
            'x-app-key': '37d94b8bdafb17343b894dd69b4d3bf6',
            'Content-Type': 'application/json',
            'x-remote-user-id': '0'
        }
        conn.request("POST", "/v2/natural/nutrients", json.dumps(payload), headers)
        res = conn.getresponse()
        data = res.read()
        result = json.loads(data)
        return result["foods"][0]["nf_calories"]
