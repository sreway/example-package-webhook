from flask_restful import Resource, original_flask_make_response as make_respone
from flask_restful import reqparse

packages = {
    "group1": {
        "packages": ["vim", "code", "python3-devel"]
    },

    "group2": {
        "packages": ["vi", "python2-devel"]
    },

}


class Packages(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hostgroup', help="hosgroup is required", required=True)
        args = parser.parse_args()
        try:
            hostgroup_data = packages[args['hostgroup']]
        except KeyError:
            hostgroup_data = {"message": "Hostgroup not found"}
            return make_respone(hostgroup_data, 404)
        return make_respone(hostgroup_data, 200)