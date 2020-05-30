import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import app
from models import db, Actor, Movie

assistant_token = "Bearer {}".format(os.environ.get('ASSISTANT_JWT'))
director_token = "Bearer {}".format(os.environ.get('DIRECTOR_JWT'))
producer_token = "Bearer {}".format(os.environ.get('PRODUCER_JWT'))

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

    self.new_movie = {
      "title": "movie3",
      "release_date": datetime.utcnow()
    }
  
  def tearDown(self):
    """Executed after reach test"""
    pass

  #  Success behavior tests
  #  ----------------------------------------------------------------
  def test_get_actors (self):
    """Test actors GET endpoint"""
    res = self.client().get('/actors')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])
    self.assertTrue(len(data['actors']) >= 0)
  
  def test_get_movies (self):
    """Test movies GET endpoint"""
    res = self.client().get('/movies')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])
    self.assertTrue(len(data['movies']) >= 0)
  
  def test_add_new_actor(self):
    """Test actors POST endpoint"""
    res = self.client().post('/actors', json=self.new_actor)
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['success'], True)
    self.assertEqual(data['actor']['name'],'actor3')
  
  def test_add_new_movie(self):
    """Test movie POST endpoint"""
    res = self.client().post('/movies', json=self.new_movie)
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)
    self.assertEqual(data['success'], True)
    self.assertEqual(data['movie']['title'],'movie3')
  
  def test_edit_actor(self):
    """Test actors PATCH endpoint"""
    res = self.client().patch('/actors/1', json=self.new_actor)
    data = json.loads(res.data)    
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertEqual(data['actor']['name'],'actor3')
  
  def test_edit_movie(self):
    """Test movie PATCH endpoint"""
    res = self.client().patch('/movies/1', json=self.new_movie)
    data = json.loads(res.data)    
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)
    self.assertEqual(data['movie']['title'],'movie3')
  
  def test_delete_actor(self):
    """Test actor DELETE endpoint"""
    res = self.client().post('/actors', json=self.new_actor)
    data = json.loads(res.data)
    actor_id = data['actor']['id']
    res_delete = self.client().delete(f'/actors/{actor_id}')
    data_delete = json.loads(res_delete.data)    
    self.assertEqual(res_delete.status_code, 200)
    self.assertEqual(data_delete['success'], True)
    self.assertEqual(data_delete['delete'], actor_id)
  
  def test_delete_movie(self):
    """Test movie DELETE endpoint"""
    res = self.client().post('/movies', json=self.new_movie)
    data = json.loads(res.data)
    movie_id = data['movie']['id']    
    res_delete = self.client().delete(f'/movies/{movie_id}')
    data_delete = json.loads(res_delete.data)    
    self.assertEqual(res_delete.status_code, 200)
    self.assertEqual(data_delete['success'], True)
    self.assertEqual(data_delete['delete'], movie_id)


# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()