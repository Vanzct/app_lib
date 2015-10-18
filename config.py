__author__ = 'Van.zx'

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Wohaveadream@bookboy.com'

    def __init__(self):
        pass

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(object, Config):
    DEBUG = True

    def __init__(self):
        super(DevelopConfig, self).__init__()
        pass


class ProductionConfig(object, Config):

    def __init__(self):
        super(ProductionConfig, self).__init__()
        pass


class TestingConfig(object, Config):
    DEBUG = True

    def __init__(self):
        super(TestingConfig, self).__init__()
        pass

config_dict = {
    "develop": DevelopConfig,
    "test": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopConfig
}
