from event_processor.app import create_app
from event_processor.models import Event
from event_processor import test_settings

app = create_app('test_settings.py')
# def create_test_db():



# def drop_test_db():
