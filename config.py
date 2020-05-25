import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'udacitycapstone'
  DATABASE_URL = os.environ.get('DATABASE_URL')
