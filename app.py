import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
from models import db, Actor, Movie

# create and configure the app
app = Flask(__name__)
app.config.from_object(Config) # connect app to a local postgresql database
db = SQLAlchemy(app) # initializing the instance with the app context
CORS(app)

# ROUTES

# Endpoint for index
@app.route('/')
def index():
  return jsonify({
    'app status': 'healthy'
  }), 200

# Endpoint route handler for GET request for actor
@app.route('/actors')
def get_actors():
  """
  Get details of all actors
  :return details of all actors
  """
  try:
    results = Actor.query.order_by(Actor.id).all()    
    if len(results) == 0:
      abort(404)
    actors = [row.format() for row in results]    
    return jsonify({
      'success': True,
      'actors': actors
    }), 200
  except Exception:
    abort(422)

# Endpoint route handler for GET request for movies
@app.route('/movies')
def get_movies():
  """
  Get details of all movies
  :return details of all movies
  """
  try:
    results = Movie.query.all()
    if len(results) == 0:
      abort(404)
    movies = [row.format() for row in results]
    return jsonify({
      'success': True,
      'movies': movies
    }), 200
  except Exception:
    abort(422)

# Endpoint route handler for POST request for actor
@app.route('/actors', methods=['POST'])
def create_actor():
  """
  Add new actor to database
  :return newly added actor
  """
  body = request.get_json(request)
  name = body.get('name')
  age = body.get('age')
  gender = body.get('gender')
  if name is None or age is None or gender is None:
    abort(400)
  try:
    new_actor = Actor(name=name, age=age, gender=gender)
    new_actor.insert()
    new_actor_formated = new_actor.format()

    # Return newly created actor
    return jsonify({
      'success': True,
      'actor':new_actor_formated
    }), 201
  except Exception:
    abort(422)

# Endpoint route handler for POST request for movie
@app.route('/movies', methods=['POST'])
def create_movie():
  """
  Add new movie to database
  :return newly added movie
  """
  body = request.get_json(request)
  title = body.get('title')
  release_date = body.get('release_date')
  
  if title is None or release_date is None:
    abort(400)
  try:
    new_movie = Movie(title=title, release_date=release_date)
    new_movie.insert()
    new_movie_formated = new_movie.format()

    # Return newly created movie
    return jsonify({
      'success': True,
      'movie':new_movie_formated
    }), 201
  except Exception:
    abort(422)

# Endpoint route handler for PATCH request for actor
@app.route('/actors/<int:actor_id>', methods=['PATCH'])
def update_actor(actor_id):
  """
  Edit information for given actor id
  :return updated actor information
  """
  actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
  if actor is None:
    abort(404)

  body = request.get_json(request)
  name = body.get('name', None)
  age = body.get('age', None)
  gender = body.get('gender',None)
  if name is None or age is None or gender is None:
    abort(400)  
  try:
    actor.name = name
    actor.age = age
    actor.gender = gender
    actor.update()
    actor_formated = actor.format()

    # Return edited actor
    return jsonify({
      'success': True,
      'actor':actor_formated
    }), 200
  except Exception:
    abort(422)

# Endpoint route handler for PATCH request for movie
@app.route('/movies/<int:movie_id>', methods=['PATCH'])
def update_movie(movie_id):
  """
  Edit information for given movie id
  :return updated movie information
  """
  movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
  if movie is None:
    abort(404)

  body = request.get_json(request)
  title = body.get('title')
  release_date = body.get('release_date')
  
  if title is None or release_date is None:
    abort(400)
  try:
    movie.title = title
    movie.release_date = release_date
    movie.update()
    movie_formated = movie.format()

    # Return edited movie
    return jsonify({
      'success': True,
      'movie':movie_formated
    }), 200
  except Exception:
    abort(422)

# Endpoint route handler for DELETE request for actor
@app.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
  """
  Delete actor using actor id
  :return id of actor being deleted
  """
  actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
  if actor is None:
    abort(404)
  try:
    actor.delete()
  # Return deleted actor id
    return jsonify({
      'success': True,
      'delete':actor_id
    }), 200
  except Exception:
    abort(422)

# Endpoint route handler for DELETE request for movie
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
  """
  Delete movie using movie id
  :return id of movie being deleted
  """
  movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
  if movie is None:
    abort(404)
  try:
    movie.delete()
  # Return deleted movie id
    return jsonify({
      'success': True,
      'delete':movie_id
    }), 200
  except Exception:
    abort(422)

# Error handling


@app.errorhandler(422)
def unprocessable(error):
  """
  Unprocessable Entity
  """
  return jsonify({
    "success": False,
    "error": 422,
    "message": "unprocessable"
  })

@app.errorhandler(404)
def not_found(error):
  """
  Not Found
  """
  return jsonify({
    "success": False,
    "error": 404,
    "message": "not found"
  })

@app.errorhandler(400)
def bad_request(error):
  """
  Bad request
  """
  return jsonify({
    "success": False,
    "error": 400,
    "message": "bad request"
  })
    

    
  
