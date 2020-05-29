import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy 

from app import app
from models import db

class CastingAgencyTestCase(unittest.TestCase):
  """This class represents the casting agency test case"""

  def setUp(self):
    self.app = app
    self.client = self.app.test_client
    
