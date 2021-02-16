from flask import Flask
from flask_restful import Api
from src.helpers.log_handler import InterceptHandler
from src.resourses.packages import Packages
from src.resourses.hostgroups import Hostgroups
from src.resourses.main import Main


app = Flask(__name__)
app.logger.addHandler(InterceptHandler)
api = Api(app)
api.add_resource(Packages, '/packages')
api.add_resource(Hostgroups, '/hostgroups')
api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
