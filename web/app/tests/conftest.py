import pytest
from owlog.app import create_app
from owlog.app.config import TestingConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
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
    server = testing_config.DATABASE_SERVER
    database_name = testing_config.DATABASE_NAME
    engine = create_engine(server)
    conn = engine.connect()
    conn.execute(f'DROP DATABASE IF EXISTS {database_name}')
    conn.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
    rv = create_engine(f'{server}/{database_name}')

    db.create_all(rv)
    yield rv

    db.drop_all(rv)
    rv.dispose()