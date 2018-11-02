
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