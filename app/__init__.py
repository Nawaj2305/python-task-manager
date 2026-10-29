from flask import Flask

from app.routes import main


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "change-this-for-production"

    if test_config:
        app.config.update(test_config)

    app.register_blueprint(main)

    return app