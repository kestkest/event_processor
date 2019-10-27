from flask import Flask

from event_processor.db import db
from event_processor.events.views import events


def create_app(settings):

    app = Flask(__name__)
    app.config.from_pyfile(settings)
    db.init_app(app)
    app.register_blueprint(events, url_prefix='/api/v1')

    return app


# app = create_app('settings.py')
