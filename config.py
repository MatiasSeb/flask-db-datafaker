import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRETKEY')
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False