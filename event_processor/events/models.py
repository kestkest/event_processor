from datetime import datetime

from event_processor.db import db


class Event(db.Document):
    meta = {
        'collection': 'events'
    }

    event_type = db.StringField(required=True)
    status = db.IntField(default=0)
    started_at = db.DateTimeField(default=datetime.now)
    finished_at = db.DateTimeField()
