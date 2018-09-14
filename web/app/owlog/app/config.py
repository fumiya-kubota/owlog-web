import os


class BaseConfig:
    DATABASE_URI = ''
    REDIS_HOST = ''
    REDIS_PORT = 0


class DevelopmentConfig(BaseConfig):
    DATABASE_URI = 'postgresql://root@127.0.0.1:13306/owlog?charset=utf8mb4'
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 16379


class ProductionConfig(BaseConfig):
    DATABASE_URI = 'postgresql://root@db:3306/owlog?charset=utf8mb4'
    REDIS_HOST = 'redis'
    REDIS_PORT = 6379


def get_configuration_object():
    config_name = os.getenv('OWLOG_CONFIGRATION')
    config = {'production': ProductionConfig}.get(config_name, DevelopmentConfig)
    return config()
