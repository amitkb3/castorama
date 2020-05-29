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
    self.app = app
    self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URL')

    self.new_actor = {
      "name": "actor3",
      "age": "25",
      "gender":"F"
    }
  
  def tearDown(self):
    """Executed after reach test"""
    pass

  #  Success behavior tests
  #  ----------------------------------------------------------------
  def test_get_actors (self):
    res = self.client().get('/actors')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])
    self.assertTrue(len(data['actors']) >= 0)

# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()