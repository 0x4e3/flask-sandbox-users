import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    # instantiate the app
    app = Flask(__name__)

    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from users.api.users import users_blueprint
    from users.api.auth import auth_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
