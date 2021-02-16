from flask_restful import Resource, original_flask_make_response as make_respone

class Main(Resource):
    def get(self):
        data = {
            "message": "Example package parser by hostgroup"
        }
        return make_respone(data, 200)