from datetime import datetime
from flask import Blueprint, request, Response

from .models import Event

events = Blueprint('events', __name__)


@events.route('start', methods=['POST'], endpoint='events-start')
def start():
    status = 200
    event_type = request.json['type']
    event = Event.objects(event_type=event_type, status=0).first()

    if not event:
        new_event = Event(event_type=event_type)
        new_event.save()
        status = 201

    return Response(status=status)


@events.route('finish', methods=['POST'])
def finish():

    status = 200
    event_type = request.json['type']
    event = Event.objects(event_type=event_type, status=0).first()

    if event:
        event.status = 1
        event.finished_at = datetime.now()
        event.save()
    else:
        status = 404

    return Response(status=status)
