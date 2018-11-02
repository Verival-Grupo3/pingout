import pytest
from dateutil import parser

@pytest.fixture
def create_pingout(client):
    response = client.post('create-pingout')
    uuid = response.json['uuid']
    return uuid

def test_return_200_on_root(client):
    """ Return status code 200 on root url"""
    response = client.get('/')
    assert response.status_code == 200

def test_return_201_on_post_create_pingout(client):
    response = client.post('create-pingout')
    assert response.status_code == 201
    assert response.data != ''

def test_return_405_on_get_create_pingout(client):
    response = client.get('create-pingout')
    assert response.status_code == 405


def test_get_uuid_url(client):
    response = client.post('create-pingout')
    uuid = response.json['uuid']
    response = client.get(uuid)
    assert response.status_code == 200

def test_get_inexistent_uuid_url(client):
  response = client.post('create-pingout')
  invalid_uuid = '3106a663a8f642b8bd79dac0469bd739'
  response = client.get(invalid_uuid)
  assert response.status_code == 404

def test_get_invalid_uuid_url(client):
  invalid_uuid = 'notuuid'
  response = client.get(invalid_uuid)
  assert response.status_code == 400

def block_post_requisition_uuid_url(client):
  uuid = response.json['uuid']
  response = client.post(uuid)
  assert response.status_code == 405

def test_create_ping_with_valid_UUID(client):
    uuid = create_pingout(client)
    response = client.post(uuid + '/ping')
    assert response.status_code == 201

def test_create_ping_with_nonexistent_UUID(client):
    uuid = 'de21ff11e30047ae9698f6bed2529ca4'
    response = client.post(uuid + '/ping')
    assert response.status_code == 404

def test_create_ping_with_invalid_UUID(client):
    uuid = 'de21ff11e30047ae9698f6bed2529caj'
    response = client.post(uuid + '/ping')
    assert response.status_code == 400

def test_get_block_in_ping_url(client):
    uuid = create_pingout(client)
    response = client.get(uuid + '/ping')
    assert response.status_code == 405

def test_filter_with_valid_date(client):
    uuid = create_pingout(client)
    client.post(uuid + '/ping')
    data = client.get('/' + uuid).json
    pings = data['pingout']['pings']
    unformatted_date = pings[0]['date']
    date = parser.parse(unformatted_date)

    initial_date = '-'.join([str(date.year), str(date.month), str(date.day)])
    final_date = '-'.join([str(date.year), str(date.month), str(date.day)])

    response = client.get(f'/{uuid}/filter/?initial_date={initial_date}&final_date={final_date}').json

def test_filter_with_invalid_UUID_and_valid_date(client):
    uuid = 'invalidUUID'
    client.post(uuid + '/ping')
    initial_date = parser.parse('2018-09-24')
    final_date = parser.parse('2018-09-30')

    response = client.get(f'/{uuid}/filter/?initial_date={initial_date}&final_date={final_date}')
    assert response.status_code == 404

def test_filter_with_valid_UUID_and_unformatted_date(client):
    uuid = create_pingout(client)
    client.post(uuid + '/ping')
    data = client.get('/' + uuid).json
    pings = data['pingout']['pings']
    unformatted_date = pings[0]['date']

    initial_date = unformatted_date
    final_date = unformatted_date

    response = client.get(f'/{uuid}/filter/?initial_date={initial_date}&final_date={final_date}')
    assert response.status_code == 404    