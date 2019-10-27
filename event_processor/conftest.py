import pytest

from mongoengine import connection
from .test_settings import MONGODB_DB
from .app import create_app


@pytest.fixture
def app():
    app = create_app('test_settings.py')
    return app


@pytest.fixture(autouse=True)
def clear_test_database():
    # "Before" logic is empty
    yield
    db = connection.get_connection()
    db.drop_database(MONGODB_DB)
