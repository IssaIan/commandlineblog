from flask_api import FlaskAPI
from .api.v1 import version_1 as v1
from flask_jwt_extended import (JWTManager)


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.register_blueprint(v1)
    app.config['JWT_SECRET_KEY'] = 'HUNCHO'
    jwt = JWTManager(app)

    return app