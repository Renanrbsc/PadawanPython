from flask_restful import Api

from flask import Flask

from Controller.open_txt import ControllerAmigo
app = Flask(__name__)
api = Api(app)

api.add_resource(ControllerAmigo, '/amigo', endpoint='amigos')


app.run(debug=True)


