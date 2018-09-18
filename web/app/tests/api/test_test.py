import pytest


@pytest.mark.usefixtures('db_setup')
async def test_fixture_test_client_get(app, sanic_server):
    """
    GET request
    """
    print(app)
