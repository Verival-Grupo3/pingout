import pytest

@pytest.fixture
def create_pingout(client):
    response = client.post('create-pingout')
    uuid = response.json['uuid']
    return uuid

def test_return_200_on_root(client):
    """ Return status code 200 on root url"""
    response = client.get('/')
    assert response.status_code == 200

# Test route create-pingout for a post
def test_return_201_on_post_create_pingout(client):
    response = client.post('create-pingout')
    assert response.status_code == 201
    assert response.data != ''

# Test route create-pingout for a get
def test_return_405_on_get_create_pingout(client):
    response = client.get('create-pingout')
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
