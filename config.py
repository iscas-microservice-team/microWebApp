import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aeaacf6364624879572615793'
    DB_CONNECTOR_URL = '174.137.53.55:9090'
