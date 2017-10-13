import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


def create_app():

    # instantiate the app
    app = Flask(__name__)

    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from users.api.views import users_blueprint
    app.register_blueprint(users_blueprint)

    return app
