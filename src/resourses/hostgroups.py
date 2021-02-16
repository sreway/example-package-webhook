from flask_restful import Resource, original_flask_make_response as make_respone
from flask import jsonify

hostgroups = {
    "hostgroups": ["group1", "group2"]
}


class Hostgroups(Resource):
    def get(self):
        return make_respone(hostgroups, 200)