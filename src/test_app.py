import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        return client


def test_ping(client):
    """Test ping."""

    rv = client.get('/api/ping')
    assert('OK' in rv.status)
    assert(rv.json['success'] == True)