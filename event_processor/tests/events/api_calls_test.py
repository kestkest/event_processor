import pytest

from event_processor.events.models import Event


@pytest.mark.parametrize('e_type,status_codes', [('qwerty', (201, 200))])
def test_create(app, e_type, status_codes):
    url = '/api/v1/start'
    data = {'type': e_type}

    client = app.test_client()
    response = client.post(url, json=data)
    event = Event.objects(event_type=e_type).first()

    assert event.event_type == e_type
    assert response.status_code == status_codes[0]

    response = client.post(url, json=data)
    assert response.status_code == status_codes[1]


@pytest.mark.parametrize('e_type,resp_codes', [('a1', (200, 404))])
def test_finish(app, e_type, resp_codes):
    url = '/api/v1/finish'
    data = {'type': e_type}
    event = Event(event_type=e_type)
    event.save()

    client = app.test_client()
    response = client.post(url, json=data)

    event.reload()
    assert event.status == 1
    assert response.status_code == resp_codes[0]

    response = client.post(url, json=data)
    assert response.status_code == resp_codes[1]
