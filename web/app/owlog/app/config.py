import os


class BaseConfig:
    DATABASE_URI = ''
    REDIS_HOST = ''
    REDIS_PORT = 0


class DevelopmentConfig(BaseConfig):
    DATABASE_SERVER = 'postgresql+asyncpg://owlog@127.0.0.1:5432'
    DATABASE_NAME = 'owlog'
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 16379


class ProductionConfig(BaseConfig):
    DATABASE_SERVER = 'postgresql+asyncpg://owlog@db:5432'
    DATABASE_NAME = 'owlog'
    REDIS_HOST = 'redis'
    REDIS_PORT = 6379

class TestingConfig(BaseConfig):
    DATABASE_PROTOCOL = 'postgresql+asyncpg'
    DATABASE_URI = 'owlog@127.0.0.1:5432'
    DATABASE_SERVER = f'{DATABASE_PROTOCOL}://{DATABASE_URI}'
    DATABASE_NAME = 'owlog_testing'
    REDIS_HOST = 'redis'
    REDIS_PORT = 6379



def get_configuration_object():
    config_name = os.getenv('OWLOG_CONFIGRATION')
    config = {
        'production': ProductionConfig,
        'testing': TestingConfig}.get(config_name, DevelopmentConfig)
    return config()
