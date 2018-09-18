import pytest
from owlog.app import create_app
from owlog.app.config import TestingConfig
from sqlalchemy import create_engine
from owlog.app.model import db


@pytest.fixture(scope='session')
def app(request):
    app = create_app()
    return app


@pytest.fixture
def sanic_server(loop, app, test_server):
    print('loop', loop, 'app', app, 'test_server', test_server)
    return loop.run_until_complete(test_server(app))


@pytest.fixture(scope='module')
def db_setup():
    testing_config = TestingConfig()
    server = testing_config.DATABASE_URI
    database_name = testing_config.DATABASE_NAME
    engine = create_engine(f'postgresql://{server}')
    conn = engine.connect()
    try:
        conn.execution_options(isolation_level="AUTOCOMMIT").execute(f"CREATE DATABASE {database_name}")
    except Exception:
        pass
    rv = create_engine(f'postgresql://{server}/{database_name}')

    db.create_all(rv)
    yield rv

    db.drop_all(rv)
    rv.dispose()
