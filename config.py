import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@127.0.0.1:5432/micro_blog'
    #os.environ.get('DATABASE_URL') or \
    SQLALCHEMY_TRACK_MODIFICATIONS = False
